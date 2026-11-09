---
symbol: "SLC38A4"
type: "gene"
col: 6279
ensembl_id: "ENSG00000139209"
name: "solute carrier family 38 member 4"
location: "12q13.11"
module: 102
arm: "+"
pooled_cpm: 2.69
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 1
n_dd_up_clean: 11
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/102"]
generated_by: "tahoemap"
---

# SLC38A4

*solute carrier family 38 member 4* — 12q13.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.87× (z +12.6, q 1e-33, up in 1 of 1 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.22× (z +11.0, q 2e-25, up in 13 of 27 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.670× (z -3.9, q 0.061, down in 11 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (Hs 766T 0.156×; ⚠ cell-cycle shift, explains ~27% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (SNU-1 0.214×); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (SNU-1 0.114×); [[Digitoxin (drug)]] 0.5 µM in 1 line (SNU-1 0.143×).
> Its strongest partners by |cos| (92 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 9 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMEM266]] (+0.65, fdr 1e-05), [[GPM6B]] (+0.58, fdr 5e-05), [[PRSS23-AS1]] (+0.56, fdr 1e-05).
> It is in [[Module 102]], a single-armed module (Neuronal System).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 7 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6279.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.87×** | +12.6 | 1e-33 | 1/1 (Hs 766T) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.22×** | +11.0 | 2e-25 | 13/27 (SW480, A549, …) | rises with dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.93×** | +10.4 | 4e-23 | 5/9 (HOP62, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.28×** | +7.4 | 2e-11 | 1/4 (Hs 766T) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.47×** | +5.2 | 2e-05 | 14/44 (NCI-H460, SW480, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.68×** | +5.0 | 5e-05 | 16/40 (PANC-1, NCI-H460, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.59×** | +4.5 | 6e-04 | 10/34 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.57×** | +4.4 | 9e-04 | 11/40 (SW480, RKO, …) | rises with dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[Cepharanthine (drug)]] 0.5 µM |  | **1.55×** | +4.2 | 0.001 | 1/23 (NCI-H1573) | two highest doses | position effect removed |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.78×** | +4.0 | 0.004 | 1/8 (SW480) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM |  | **1.54×** | +3.9 | 0.005 | 3/13 (NCI-H1573, PANC-1, …) | inconsistent across doses |  |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **2.14×** | +3.9 | 0.005 | 0/2 | top dose only | noisy plate (z scaled) |
| [[Pimozide (drug)]] 0.05 µM |  | **1.49×** | +3.9 | 0.005 | 0/14 | inconsistent across doses | low cells (technical?) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.46×** | +3.7 | 0.010 | 2/23 (HT-29, NCI-H661) | top dose only | position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **1.39×** | +3.2 | 0.047 | 16/44 (PANC-1, NCI-H460, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib (drug)]] 0.05 µM |  | **1.41×** | +3.1 | 0.058 | 0/21 | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6279.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (Hs 766T 0.156×; ⚠ cell-cycle shift, explains ~27% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (SNU-1 0.214×); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (SNU-1 0.114×); [[Digitoxin (drug)]] 0.5 µM in 1 line (SNU-1 0.143×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.670×** | -3.9 | 0.061 | 11/46 (SNU-1, BT-474, …) | rises with dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | 0.682× | -3.6 | 0.11 | 10/36 (SNU-1, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~8% here); composition shift; position effect removed |
| [[Auranofin (drug)]] 0.5 µM |  | 0.707× | -3.4 | 0.13 | 8/38 (HS-578T, NCI-H23, …) | inconsistent across doses |  |
| [[Lucanthone (drug)]] 0.05 µM |  | 0.690× | -3.3 | 0.13 | 6/45 (AsPC-1, C-33 A, …) | inconsistent across doses |  |
| [[Norepinephrine (hydrochloride) (drug)]] 0.5 µM |  | 0.715× | -3.2 | 0.13 | 2/39 (LS 180, NCI-H1792) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.725× | -3.1 | 0.17 | 8/45 (SNU-1, HT-29, …) | inconsistent across doses |  |
| [[Olanzapine (drug)]] 0.5 µM |  | 0.729× | -3.1 | 0.18 | 1/37 (NCI-H23) | inconsistent across doses |  |
| [[5-Azacytidine (drug)]] 5 µM |  | 0.732× | -3.0 | 0.18 | 4/42 (SNU-1, A-172, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6279. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SNU-1 (line)]] | wt | 65.3 | 0 | 8 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.214× (z -10.2) |
| [[Hs 766T (line)]] | wt | 27.6 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.156× (z -12.4) ⚠ cell-cycle shift, explains ~27% of this change |
| [[A-172 (line)]] | wt | 3.25 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.18 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.923 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.05 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.21 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.836 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.03 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.18 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.979 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.21 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.72 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.39 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.27 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.25 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.77 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.52 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.26 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.901 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.32 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.45 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.11 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.19 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.06 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.25 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.17 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.10 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.52 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.09 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.07 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.14 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.13 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.913 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.73 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.71 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.28 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.72 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.12 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.06 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.84 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.791 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.11 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.75 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.71 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.62 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.853 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.986 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.49 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6279), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 9 of them with an alert (⚠; 8 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM266]] | +0.65 | +0.52 / +0.65 | both halves | 1e-05 |  |
| [[GPM6B]] | +0.58 | +0.40 / +0.64 | both halves | 5e-05 |  |
| [[PRSS23-AS1]] | +0.56 | +0.50 / +0.52 | both halves | 1e-05 |  |
| [[CCDC39]] | +0.54 | +0.39 / +0.53 | both halves | 6e-05 |  |
| [[SLC13A4]] | +0.54 | +0.33 / +0.57 | both halves | 1e-04 | pathway: SLC-mediated transmembrane transport |
| [[SGCZ]] | +0.54 | +0.35 / +0.67 | both halves | 1e-04 |  |
| [[GRIA1]] | +0.52 | +0.29 / +0.70 | both halves | 3e-04 |  |
| [[USH2A]] | +0.52 | +0.30 / +0.69 | both halves | 2e-04 |  |
| [[LINC02099]] | +0.52 | +0.47 / +0.45 | both halves | 3e-05 |  |
| [[IL1RAPL2]] | +0.51 | +0.32 / +0.70 | both halves | 2e-04 |  |
| [[BMP10]] ⚠ | +0.51 | +0.50 / +0.40 | both halves | 5e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[ST8SIA1]] | +0.51 | +0.34 / +0.65 | both halves | 1e-04 |  |
| [[LINC02006]] | +0.51 | +0.38 / +0.66 | both halves | 6e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 102]] — Neuronal System; 45 genes; every member is in the + arm (projection on the module's main direction 0.291). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (16.4, 35.0); signed map (29.8, 21.4). **Vector** length 35.4, 3.39% of its response variance represented; |z| ≥ 3 in 1,071 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +2.5 | +5.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.4 | +11.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.3 | +7.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +2.1 | +4.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.0 | +12.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.5 | +0.1 |
|  | [[Brivudine (drug)]] 5 µM |  | +0.8 | +2.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +0.7 | +2.4 |
|  | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | +0.6 | +1.1 |
| fall | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.1 | -1.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -0.8 | -3.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -0.8 | -1.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -0.7 | -3.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | -0.6 | -2.0 |
|  | [[Pentamidine (isethionate) (drug)]] 5 µM |  | -0.5 | -0.1 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.5 | -3.3 |
|  | [[Dabrafenib (drug)]] 5 µM |  | -0.5 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 38 member 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q13.11 — chr12:46,764,761-46,832,408 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PAAT, NAT3, ATA3, SNAT4 |
| Gene groups (HGNC) | Solute carrier family 38 |
| Reactome | 4 pathways, smallest: Amino acid transport across the plasma membrane; SLC-mediated transport of amino acids; SLC-mediated transmembrane transport |
| Matched by | ensembl_id |

**Function**, from UniProt [Q969I6](https://www.uniprot.org/uniprotkb/Q969I6) (Sodium-coupled neutral amino acid transporter 4):

> Symporter that cotransports neutral amino acids and sodium ions from the extracellular to the intracellular side of the cell membrane. The transport is electrogenic, pH dependent and partially tolerates substitution of Na(+) by Li(+). Preferentially transports smaller amino acids, such as glycine, L-alanine, L-serine, L-asparagine and L-threonine, followed by L-cysteine, L-histidine, L-proline and L-glutamine and L-methionine.

**Summary**, from NCBI Gene [55089](https://www.ncbi.nlm.nih.gov/gene/55089):

> SLC38A4 is found predominantly in liver and transports both cationic and neutral amino acids. The transport of cationic amino acids by SLC38A4 is Na(+) and pH independent, while the transport of neutral amino acids is Na(+) and pH dependent (Hatanaka et al., 2001 [PubMed 11342143]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:14679](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14679) · Entrez [55089](https://www.ncbi.nlm.nih.gov/gene/55089) · UniProt [Q969I6](https://www.uniprot.org/uniprotkb/Q969I6) · Ensembl [ENSG00000139209](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000139209)

## Data

Gene col 6279: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6279); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6279, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6279]; `tensor/DDL_lfc|DDL_z.npy` [6279]; `embed/gene_vectors.npy` [6279]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6279 or target_col == 6279). Every well: [[SLC38A4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC38A4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
