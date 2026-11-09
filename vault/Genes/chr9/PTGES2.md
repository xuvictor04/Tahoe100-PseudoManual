---
symbol: "PTGES2"
type: "gene"
col: 7265
ensembl_id: "ENSG00000148334"
name: "prostaglandin E synthase 2"
location: "9q34.11"
module: 33
arm: "+"
pooled_cpm: 14.16
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 3
n_dd_up_clean: 3
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/033"]
generated_by: "tahoemap"
---

# PTGES2

*prostaglandin E synthase 2* — 9q34.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.57× (z +11.8, q 2e-29, up in 35 of 38 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Belinostat (drug)]] 0.5 µM: 1.40× (z +4.2, q 0.003, up in 20 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.465× (z -13.6, q 2e-39, down in 39 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HEATR3]] (+0.70, fdr 7e-06), [[XPO5]] (+0.70, fdr 7e-06), [[SCAP]] (+0.70, fdr 1e-05); moves opposite to [[CFAP53]] (-0.61, fdr 1e-05), [[TRNAU1AP]] (-0.58, fdr 5e-05), [[MALINC1]] (-0.58, fdr 2e-05).
> It sits in the **+** arm of [[Module 033]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 7 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7265.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.57×** | +11.8 | 2e-29 | 35/38 (KATO III, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.39×** | +10.5 | 2e-23 | 21/23 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.04×** | +7.7 | 2e-12 | 25/30 (KATO III, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift; position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.53×** | +5.2 | 4e-05 | 26/43 (SNU-423, HS-578T, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.40×** | +4.2 | 0.003 | 20/47 (HOP62, Panc 03.27, …) | two highest doses | cell-cycle shift (explains ~14% here) |
| [[Belumosudil (drug)]] 5 µM |  | **1.39×** | +4.0 | 0.006 | 17/47 (LoVo, NCI-H460, …) | top dose only |  |
| [[Pralsetinib (drug)]] 5 µM |  | **1.89×** | +4.0 | 0.006 | 18/43 (PANC-1, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.09× | +3.5 | 0.031 | 0/48 | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.30×** | +3.3 | 0.071 | 14/47 (HOP62, HEC-1-A, …) | inconsistent across doses |  |
| [[venetoclax (drug)]] 5 µM |  | 1.65× | +3.1 | 0.11 | 9/42 (AsPC-1, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.27× | +3.0 | 0.12 | 12/47 (NCI-H1792, NCI-H460, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7265.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.465×** | -13.6 | 2e-39 | 39/44 (COLO 205, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.679×** | -6.9 | 2e-09 | 27/45 (RKO, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.699×** | -4.5 | 0.001 | 24/44 (MIA PaCa-2, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 5 µM |  | 0.610× | -3.1 | 0.28 | 9/46 (BT-474, NCI-H23, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | 0.778× | -3.0 | 0.28 | 13/45 (SK-MEL-2, BT-474, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.20 per unit of S-phase module lfc, +0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7265. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C-33 A (line)]] | alt | 23.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.265× (z -9.6) |
| [[COLO 205 (line)]] | alt | 51.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.141× (z -14.4) |
| [[KATO III (line)]] | alt | 24.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.51× (z +9.1) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 12.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.184× (z -9.6) |
| [[NCI-H460 (line)]] | wt | 12.3 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.85× (z +8.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.343× (z -9.9) |
| [[SW48 (line)]] | wt | 18.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.165× (z -11.3) |
| [[SW480 (line)]] | alt | 13.9 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 5.24× (z +11.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.429× (z -8.6) |
| [[A-427 (line)]] | wt | 15.2 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.324× (z -9.5) ⚠ cell-cycle shift, would explain all of this change |
| [[A498 (line)]] | wt | 15.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.415× (z -8.7) |
| [[BT-474 (line)]] | alt | 35.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.246× (z -12.3) |
| [[J82 (line)]] | alt | 17.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.188× (z -14.1) |
| [[LoVo (line)]] | wt | 14.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.231× (z -14.0) |
| [[LOX-IMVI (line)]] | wt | 11.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.342× (z -8.5) |
| [[LS 180 (line)]] | wt | 19.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.98× (z +9.0) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 8.40 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.252× (z -9.9) |
| [[NCI-H23 (line)]] | alt | 15.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.350× (z -8.5) |
| [[PANC-1 (line)]] | alt | 14.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.434× (z -9.5) |
| [[RKO (line)]] | wt | 33.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.220× (z -13.6) |
| [[RPMI-7951 (line)]] | alt | 8.51 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.123× (z -10.7) |
| [[A-172 (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 9.63 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 9.49 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.16 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 13.5 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.61 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.27 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.93 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 8.56 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 8.95 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.60 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.82 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 20.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7265), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HEATR3]] | +0.70 | +0.60 / +0.66 | both halves | 7e-06 |  |
| [[XPO5]] | +0.70 | +0.71 / +0.63 | both halves | 7e-06 |  |
| [[SCAP]] | +0.70 | +0.68 / +0.56 | both halves | 1e-05 |  |
| [[MRPL4]] | +0.69 | +0.58 / +0.64 | both halves | 7e-06 |  |
| [[FXN]] | +0.66 | +0.63 / +0.62 | both halves | 7e-06 |  |
| [[TRAF7]] | +0.65 | +0.64 / +0.53 | both halves | 1e-05 |  |
| [[C20orf27]] | +0.65 | +0.64 / +0.53 | both halves | 1e-05 |  |
| [[RPE]] | +0.64 | +0.70 / +0.55 | both halves | 1e-05 |  |
| [[TSEN2]] | +0.64 | +0.64 / +0.58 | both halves | 7e-06 |  |
| [[PGAM5]] | +0.63 | +0.62 / +0.57 | both halves | 8e-06 |  |
| [[UBAC2]] | +0.63 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[EEF1E1]] | +0.63 | +0.64 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CFAP53]] | -0.61 | -0.52 / -0.51 | both halves | 1e-05 |  |
| [[TRNAU1AP]] | -0.58 | -0.62 / -0.39 | both halves | 5e-05 |  |
| [[MALINC1]] | -0.58 | -0.47 / -0.49 | both halves | 2e-05 |  |
| [[C2orf92]] | -0.58 | -0.60 / -0.38 | both halves | 6e-05 |  |
| [[NDUFV2-AS1]] | -0.57 | -0.52 / -0.46 | both halves | 3e-05 |  |
| [[OSER1-DT]] | -0.57 | -0.57 / -0.48 | both halves | 2e-05 |  |
| [[ESR2]] | -0.57 | -0.62 / -0.41 | both halves | 4e-05 |  |
| [[ZNF846]] | -0.57 | -0.51 / -0.45 | both halves | 3e-05 |  |
| [[C12orf57]] | -0.56 | -0.55 / -0.45 | both halves | 3e-05 |  |
| [[ZNF490]] | -0.56 | -0.61 / -0.33 | both halves | 1e-04 |  |
| [[RSRP1]] | -0.56 | -0.59 / -0.43 | both halves | 3e-05 |  |
| [[MDGA1]] | -0.56 | -0.50 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers PTGES2's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 033]] — MYC targets v2; 139 genes; this gene is in the **+** arm (projection on the module's main direction 0.643). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-10.9, -39.8); signed map (-10.1, -52.4). **Vector** length 73.0, 14.2% of its response variance represented; |z| ≥ 3 in 737 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.0 | +3.0 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +3.1 | +4.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.1 | +11.8 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +2.9 | +2.7 |
|  | [[venetoclax (drug)]] 5 µM |  | +2.6 | +3.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.4 | +4.0 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +1.9 | +2.6 |
|  | [[TAK-733 (drug)]] 5 µM |  | +1.7 | +2.8 |
|  | [[Pralsetinib (drug)]] 5 µM |  | +1.6 | +4.0 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -6.0 | -13.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -4.7 | -6.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.5 | -4.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.4 | -2.3 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.1 | -3.1 |
|  | [[Cytarabine (drug)]] 0.05 µM |  | -1.4 | -1.2 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.3 | -1.0 |
|  | [[Filgotinib (drug)]] 5 µM |  | -1.2 | -0.3 |

## What is on record

|  |  |
|---|---|
| Name | prostaglandin E synthase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q34.11 — chr9:128,120,693-128,128,462 (-) |
| Ensembl biotype | protein_coding |
| Also known as | mPGES-2, FLJ14038; previously C9orf15 |
| Gene groups (HGNC) | Glutaredoxin domain containing; Prostaglandin E synthases |
| Reactome | 6 pathways, smallest: Synthesis of Prostaglandins (PG) and Thromboxanes (TX); Arachidonate metabolism; Fatty acid metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H7Z7](https://www.uniprot.org/uniprotkb/Q9H7Z7) (Prostaglandin E synthase 2):

> Isomerase that catalyzes the conversion of PGH2 into the more stable prostaglandin E2 (PGE2) (in vitro). The biological function and the GSH-dependent property of PTGES2 is still under debate. In vivo, PTGES2 could form a complex with GSH and heme and would not participate in PGE2 synthesis but would catalyze the degradation of prostaglandin E2 H2 (PGH2) to 12(S)-hydroxy-5(Z),8(E),10(E)-heptadecatrienoic acid (HHT) and malondialdehyde (MDA) (By similarity).

**Summary**, from NCBI Gene [80142](https://www.ncbi.nlm.nih.gov/gene/80142):

> The protein encoded by this gene is a membrane-associated prostaglandin E synthase, which catalyzes the conversion of prostaglandin H2 to prostaglandin E2. This protein also has been shown to activate the transcription regulated by a gamma-interferon-activated transcription element (GATE). Multiple transcript variants have been found for this gene. [provided by RefSeq, Jun 2009]

**Accessions** — [HGNC:17822](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17822) · Entrez [80142](https://www.ncbi.nlm.nih.gov/gene/80142) · UniProt [Q9H7Z7](https://www.uniprot.org/uniprotkb/Q9H7Z7) · Ensembl [ENSG00000148334](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000148334)

## Data

Gene col 7265: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7265); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7265, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7265]; `tensor/DDL_lfc|DDL_z.npy` [7265]; `embed/gene_vectors.npy` [7265]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7265 or target_col == 7265). Every well: [[PTGES2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PTGES2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
