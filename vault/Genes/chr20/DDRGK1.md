---
symbol: "DDRGK1"
type: "gene"
col: 12546
ensembl_id: "ENSG00000198171"
name: "DDRGK domain containing 1"
location: "20p13"
module: 30
arm: "+"
pooled_cpm: 26.82
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 6
n_dd_up_clean: 4
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/030"]
generated_by: "tahoemap"
---

# DDRGK1

*DDRGK domain containing 1* — 20p13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.71× (z +6.8, q 6e-09, up in 34 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ixazomib citrate (drug)]] 0.5 µM: 1.55× (z +5.6, q 6e-06, up in 33 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 0.734× (z -4.0, q 0.026, down in 22 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CC2D1A]] (+0.67, fdr 7e-06), [[MAP2K2]] (+0.65, fdr 7e-06), [[FLYWCH1]] (+0.64, fdr 7e-06); moves opposite to [[CCND1]] (-0.55, fdr 1e-05), [[F2RL1]] (-0.51, fdr 4e-05), [[FKBP1A]] (-0.51, fdr 4e-05).
> It sits in the **+** arm of [[Module 030]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 4 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12546.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.71×** | +6.8 | 6e-09 | 34/44 (LoVo, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift; position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.55×** | +5.6 | 6e-06 | 33/48 (HOP62, KATO III, …) | two highest doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.52×** | +5.1 | 5e-05 | 25/36 (KATO III, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.49×** | +5.0 | 7e-05 | 33/47 (C32, SNU-1, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.49×** | +4.6 | 6e-04 | 33/48 (MIA PaCa-2, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.39×** | +4.2 | 0.002 | 24/44 (NCI-H2347, CFPAC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~21% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.31×** | +3.4 | 0.055 | 20/47 (SW480, LoVo, …) | top dose only | cell-cycle shift (explains ~13% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.29×** | +3.3 | 0.079 | 18/48 (CFPAC-1, COLO 205, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12546.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.734×** | -4.0 | 0.026 | 22/48 (A-427, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~12% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.788×** | -3.8 | 0.026 | 27/47 (SNU-1, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.743×** | -3.8 | 0.026 | 24/48 (J82, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.750×** | -3.7 | 0.031 | 23/48 (NCI-H2030, NCI-H661, …) | all doses, flat | cell-cycle shift (explains ~11% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.754×** | -3.6 | 0.033 | 21/47 (NCI-H460, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.760×** | -3.5 | 0.041 | 20/48 (HS-578T, J82, …) | all doses, flat | cell-cycle shift (explains ~1% here); position effect removed |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 0.788× | -3.1 | 0.18 | 11/48 (SW480, HCT15, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.12 per unit of S-phase module lfc, +0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12546. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 20.7 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.255× (z -8.8) ⚠ cell-cycle shift, explains ~47% of this change |
| [[NCI-H1792 (line)]] | alt | 15.7 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.184× (z -10.6) ⚠ cell-cycle shift, explains ~47% of this change |
| [[NCI-H2122 (line)]] | alt | 29.5 | 0 | 1 | — | [[Relugolix (drug)]] 5 µM 0.245× (z -10.9) |
| [[NCI-H460 (line)]] | wt | 29.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.378× (z -8.5) |
| [[A-172 (line)]] | wt | 20.0 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 17.2 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 33.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 37.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 37.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 32.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 24.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 20.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 28.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 15.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 52.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 30.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 55.8 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 24.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 32.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 17.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 29.9 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 29.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 18.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 45.4 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 31.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 62.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 35.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 49.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 36.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 45.3 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 45.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12546), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CC2D1A]] | +0.67 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[MAP2K2]] | +0.65 | +0.60 / +0.65 | both halves | 7e-06 |  |
| [[FLYWCH1]] | +0.64 | +0.65 / +0.61 | both halves | 7e-06 |  |
| [[EGFL8]] | +0.62 | +0.61 / +0.55 | both halves | 1e-05 |  |
| [[MRPS5]] | +0.61 | +0.64 / +0.53 | both halves | 1e-05 |  |
| [[PFDN5]] | +0.59 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[TMEM94]] | +0.59 | +0.66 / +0.48 | both halves | 2e-05 |  |
| [[CRYZL1]] | +0.58 | +0.61 / +0.57 | both halves | 1e-05 |  |
| [[ZSWIM9]] | +0.56 | +0.45 / +0.58 | both halves | 3e-05 |  |
| [[UBE4B]] | +0.55 | +0.56 / +0.46 | both halves | 2e-05 |  |
| [[ERGIC3]] | +0.54 | +0.53 / +0.52 | both halves | 1e-05 |  |
| [[LYSMD1]] | +0.54 | +0.56 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCND1]] | -0.55 | -0.52 / -0.50 | both halves | 1e-05 |  |
| [[F2RL1]] | -0.51 | -0.40 / -0.51 | both halves | 4e-05 |  |
| [[FKBP1A]] | -0.51 | -0.41 / -0.55 | both halves | 4e-05 |  |
| [[C6orf120]] | -0.51 | -0.46 / -0.51 | both halves | 2e-05 |  |
| [[MGAT2]] | -0.50 | -0.49 / -0.42 | both halves | 4e-05 |  |
| [[CFL1]] | -0.50 | -0.51 / -0.49 | both halves | 1e-05 |  |
| [[SCHIP1]] | -0.50 | -0.43 / -0.48 | both halves | 3e-05 |  |
| [[CALM2]] | -0.50 | -0.48 / -0.52 | both halves | 2e-05 |  |
| [[YWHAZ]] | -0.49 | -0.41 / -0.48 | both halves | 4e-05 |  |
| [[TRIM59]] | -0.49 | -0.52 / -0.45 | both halves | 3e-05 |  |
| [[DCBLD2]] | -0.49 | -0.48 / -0.42 | both halves | 4e-05 |  |
| [[ENC1]] | -0.49 | -0.51 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises DDRGK1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[PSMB5]] | B | PSMB5 activity lowers DDRGK1's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 030]]; 146 genes; this gene is in the **+** arm (projection on the module's main direction 0.497). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (-3.9, -19.0); signed map (-32.5, -3.2). **Vector** length 64.8, 12.8% of its response variance represented; |z| ≥ 3 in 553 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM |  | +5.1 | +5.0 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +4.9 | +4.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.3 | +5.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.8 | +0.5 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +2.8 | +1.8 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.6 | +1.6 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.9 | +1.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.9 | +2.2 |
| fall | [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | -2.1 | -0.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -1.9 | -3.6 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -1.8 | -1.5 |
|  | [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | -1.7 | -3.1 |
|  | [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.7 | -1.1 |
|  | [[Palmatine (chloride) (drug)]] 0.05 µM |  | -1.6 | -0.8 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.5 | -0.5 |
|  | [[Larotrectinib (drug)]] 0.05 µM |  | -1.4 | -0.4 |
|  | [[Busulfan (drug)]] 0.05 µM |  | -1.3 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | DDRGK domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20p13 — chr20:3,190,350-3,204,685 (-) |
| Ensembl biotype | protein_coding |
| Also known as | dJ1187M17.3, UFBP1; previously C20orf116 |
| Gene groups (HGNC) | Atypical E3 ubiquitin ligases |
| Reactome | 4 pathways, smallest: RHOA GTPase cycle; RHO GTPase cycle; Signaling by Rho GTPases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96HY6](https://www.uniprot.org/uniprotkb/Q96HY6) (DDRGK domain-containing protein 1):

> Component of the UFM1 ribosome E3 ligase (UREL) complex, a multiprotein complex that catalyzes ufmylation of endoplasmic reticulum-docked proteins. The UREL complex plays a key role in ribosome recycling by mediating mono-ufmylation of the RPL26/uL24 subunit of the 60S ribosome following ribosome dissociation: ufmylation weakens the junction between post-termination 60S subunits and SEC61 translocons, promoting release and recycling of the large ribosomal subunit from the endoplasmic reticulum …

**Summary**, from NCBI Gene [65992](https://www.ncbi.nlm.nih.gov/gene/65992):

> The protein encoded by this gene interacts with components of the ubiquitin fold modifier 1 conjugation pathway and helps prevent apoptosis in ER-stressed secretory tissues. In addition, the encoded protein regulates nuclear factor-&#954;B activity. [provided by RefSeq, Dec 2015]

**Accessions** — [HGNC:16110](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16110) · Entrez [65992](https://www.ncbi.nlm.nih.gov/gene/65992) · UniProt [Q96HY6](https://www.uniprot.org/uniprotkb/Q96HY6) · Ensembl [ENSG00000198171](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198171)

## Data

Gene col 12546: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12546); `tables/drug_effects.parquet` (15 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12546, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12546]; `tensor/DDL_lfc|DDL_z.npy` [12546]; `embed/gene_vectors.npy` [12546]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12546 or target_col == 12546). Every well: [[DDRGK1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DDRGK1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
