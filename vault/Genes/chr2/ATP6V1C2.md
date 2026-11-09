---
symbol: "ATP6V1C2"
type: "gene"
col: 6819
ensembl_id: "ENSG00000143882"
name: "ATPase H+ transporting V1 subunit C2"
location: "2p25.1"
module: 21
arm: "+"
pooled_cpm: 6.6
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 0
n_dd_up_clean: 10
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/021"]
generated_by: "tahoemap"
---

# ATP6V1C2

*ATPase H+ transporting V1 subunit C2* — 2p25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (6 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 2.50× (z +15.3, q 0e+00, up in 35 of 46 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Bergenin (drug)]] 0.5 µM in 1 line (Hs 766T 0.0898×); [[Fumaric acid (drug)]] 0.05 µM in 1 line (BT-474 0.0610×); [[Ferulic acid (drug)]] 5 µM in 1 line (AsPC-1 0.0686×).
> Its strongest partners by |cos| (91 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 9 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC26A5]] (+0.69, fdr 1e-05), [[MTUS2]] (+0.67, fdr 1e-05), [[CRLF1]] (+0.64, fdr 4e-05); moves opposite to [[C17orf80]] (-0.52, fdr 7e-04), [[MAPKAPK5]] (-0.50, fdr 5e-05), [[PALB2]] (-0.50, fdr 7e-04).
> It is in [[Module 021]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 6 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6819.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **2.50×** | +15.3 | 0e+00 | 35/46 (SW480, SW1417, …) | rises with dose | position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.79×** | +12.1 | 2e-31 | 25/30 (KATO III, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.56×** | +10.7 | 2e-24 | 6/11 (HOP62, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift; position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **2.25×** | +9.6 | 1e-19 | 30/47 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.71×** | +9.0 | 4e-17 | 18/39 (HOP62, BT-474, …) | top dose only | cell-cycle shift (explains ~14% here); composition shift; position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **2.08×** | +8.7 | 4e-16 | 27/46 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~19% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.95×** | +7.9 | 2e-13 | 30/45 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.51×** | +6.9 | 4e-10 | 20/40 (HEC-1-A, A498, …) | top dose only | cell-cycle shift (explains ~12% here); position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.69×** | +6.2 | 4e-08 | 25/44 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **1.67×** | +5.6 | 1e-06 | 11/19 (J82, SW480, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.57×** | +5.3 | 6e-06 | 15/35 (HOP62, HEC-1-A, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~16% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.51×** | +4.9 | 4e-05 | 17/46 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.52×** | +4.8 | 7e-05 | 11/41 (A-427, HOP62, …) | top dose only | cell-cycle shift (explains ~20% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **1.40×** | +4.0 | 0.003 | 14/40 (NCI-H460, LOX-IMVI, …) | top dose only |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.74×** | +3.4 | 0.023 | 1/14 (A-427) | top dose only | noisy plate (z scaled) |
| [[Medroxyprogesterone acetate (drug)]] 5 µM |  | **1.20×** | +3.1 | 0.063 | 9/44 (SHP-77, A549, …) | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6819.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Bergenin (drug)]] 0.5 µM in 1 line (Hs 766T 0.0898×); [[Fumaric acid (drug)]] 0.05 µM in 1 line (BT-474 0.0610×); [[Ferulic acid (drug)]] 5 µM in 1 line (AsPC-1 0.0686×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Benproperine (phosphate) (drug)]] 0.5 µM |  | 0.758× | -3.3 | 0.33 | 5/46 (LoVo, NCI-H2030, …) | inconsistent across doses | position effect removed |
| [[Tofacitinib (drug)]] 5 µM |  | 0.823× | -3.2 | 0.33 | 13/44 (SW1417, Panc 03.27, …) | inconsistent across doses | position effect removed |
| [[Benproperine (phosphate) (drug)]] 0.05 µM |  | 0.755× | -3.1 | 0.41 | 7/45 (HT-29, NCI-H23, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.23 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6819. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 6.83 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 7.30× (z +11.9) | — |
| [[SW480 (line)]] | alt | 6.50 | 3 | 0 | [[Tucidinostat (drug)]] 5 µM 4.49× (z +12.2) | — |
| [[BT-474 (line)]] | alt | 7.19 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 8.58× (z +10.7) | [[Fumaric acid (drug)]] 0.05 µM 0.0610× (z -9.0) |
| [[HOP62 (line)]] | alt | 5.64 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.59× (z +12.0) | — |
| [[HT-29 (line)]] | alt | 7.81 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 4.39× (z +9.1) | — |
| [[NCI-H2030 (line)]] | alt | 5.59 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 4.54× (z +9.5) | — |
| [[PANC-1 (line)]] | alt | 4.31 | 2 | 0 | [[Belinostat (drug)]] 5 µM 7.80× (z +9.9) | — |
| [[AsPC-1 (line)]] | alt | 4.12 | 0 | 1 | — | [[Ferulic acid (drug)]] 5 µM 0.0686× (z -8.9) |
| [[Hs 766T (line)]] | wt | 7.03 | 0 | 1 | — | [[Bergenin (drug)]] 0.5 µM 0.0898× (z -9.6) |
| [[LS 180 (line)]] | wt | 5.29 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 5.50× (z +9.2) | — |
| [[SW1417 (line)]] | alt | 8.20 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 5.32× (z +11.1) | — |
| [[A-172 (line)]] | wt | 6.20 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 6.72 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 4.45 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.68 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.00 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.58 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.67 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.03 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.51 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.71 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.18 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.61 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.33 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.17 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.25 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.91 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 7.53 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 14.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.01 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.05 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.50 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.12 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.58 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.86 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.31 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.97 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.91 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.31 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.49 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.38 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.57 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.98 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.78 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.43 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.14 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.88 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6819), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 9 of them with an alert (⚠; 9 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC26A5]] | +0.69 | +0.55 / +0.83 | both halves | 1e-05 |  |
| [[MTUS2]] | +0.67 | +0.51 / +0.81 | both halves | 1e-05 |  |
| [[CRLF1]] | +0.64 | +0.42 / +0.72 | both halves | 4e-05 |  |
| [[IL3RA]] | +0.63 | +0.41 / +0.77 | both halves | 4e-05 |  |
| [[CYP2U1-AS1]] | +0.62 | +0.65 / +0.63 | both halves | 7e-06 |  |
| [[SYN3]] | +0.62 | +0.48 / +0.68 | both halves | 2e-05 |  |
| [[TMEM266]] | +0.62 | +0.48 / +0.69 | both halves | 2e-05 |  |
| [[CCDC39]] | +0.62 | +0.45 / +0.67 | both halves | 3e-05 |  |
| [[EFCAB14-AS1]] | +0.61 | +0.46 / +0.58 | both halves | 3e-05 |  |
| [[SPTBN1-AS2]] | +0.60 | +0.45 / +0.55 | both halves | 3e-05 |  |
| [[SYN1]] | +0.59 | +0.29 / +0.74 | both halves | 2e-04 |  |
| [[AKAP13-AS1]] | +0.59 | +0.50 / +0.58 | both halves | 1e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C17orf80]] | -0.52 | -0.21 / -0.39 | both halves | 7e-04 |  |
| [[MAPKAPK5]] | -0.50 | -0.40 / -0.45 | both halves | 5e-05 |  |
| [[PALB2]] | -0.50 | -0.21 / -0.47 | both halves | 7e-04 |  |
| [[ZNF507]] | -0.50 | -0.24 / -0.52 | both halves | 5e-04 |  |
| [[GTF3C4]] | -0.48 | -0.23 / -0.43 | both halves | 5e-04 |  |
| [[PATZ1]] | -0.48 | -0.30 / -0.50 | both halves | 2e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 021]]; 188 genes; every member is in the + arm (projection on the module's main direction 0.536). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (20.3, 33.2); signed map (28.7, 17.9). **Vector** length 55.7, 7.32% of its response variance represented; |z| ≥ 3 in 895 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +8.3 | +15.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.6 | +6.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.3 | +12.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.9 | +10.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | +5.2 | +5.6 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.0 | +1.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.8 | +2.1 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.7 | +1.8 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.4 | +2.3 |
| fall | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.0 | -0.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.7 | +0.5 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.7 | -1.9 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.5 | -2.1 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -1.4 | -1.4 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.3 | -1.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.2 | -2.1 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.2 | -0.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.1 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | ATPase H+ transporting V1 subunit C2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p25.1 — chr2:10,721,100-10,785,110 (+) |
| Ensembl biotype | protein_coding |
| Also known as | VMA5, ATP6C2 |
| Gene groups (HGNC) | V-type ATPase subunits |
| Reactome | 13 pathways, smallest: Insulin receptor recycling; ROS and RNS production in phagocytes; Transferrin endocytosis and recycling |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NEY4](https://www.uniprot.org/uniprotkb/Q8NEY4) (V-type proton ATPase subunit C 2):

> Subunit of the V1 complex of vacuolar(H+)-ATPase (V-ATPase), a multisubunit enzyme composed of a peripheral complex (V1) that hydrolyzes ATP and a membrane integral complex (V0) that translocates protons (By similarity). V-ATPase is responsible for acidifying and maintaining the pH of intracellular compartments and in some cell types, is targeted to the plasma membrane, where it is responsible for acidifying the extracellular environment (By similarity). Subunit C is necessary for the assembly …

**Summary**, from NCBI Gene [245973](https://www.ncbi.nlm.nih.gov/gene/245973):

> This gene encodes a component of vacuolar ATPase (V-ATPase), a multisubunit enzyme that mediates acidification of eukaryotic intracellular organelles. V-ATPase dependent organelle acidification is necessary for such intracellular processes as protein sorting, zymogen activation, receptor-mediated endocytosis, and synaptic vesicle proton gradient generation. V-ATPase is composed of a cytosolic V1 domain and a transmembrane V0 domain. The V1 domain consists of three A,three B, and two G subunits, …

**Accessions** — [HGNC:18264](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18264) · Entrez [245973](https://www.ncbi.nlm.nih.gov/gene/245973) · UniProt [Q8NEY4](https://www.uniprot.org/uniprotkb/Q8NEY4) · Ensembl [ENSG00000143882](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000143882)

## Data

Gene col 6819: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6819); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6819, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6819]; `tensor/DDL_lfc|DDL_z.npy` [6819]; `embed/gene_vectors.npy` [6819]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6819 or target_col == 6819). Every well: [[ATP6V1C2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ATP6V1C2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
