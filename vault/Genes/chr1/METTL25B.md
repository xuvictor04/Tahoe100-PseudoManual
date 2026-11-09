---
symbol: "METTL25B"
type: "gene"
col: 6708
ensembl_id: "ENSG00000143303"
name: "methyltransferase like 25B"
location: "1q23.1"
module: 12
arm: "+"
pooled_cpm: 9.05
n_lines_expressing: 50
n_dd_up: 21
n_dd_down: 11
n_dd_up_clean: 18
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# METTL25B

*methyltransferase like 25B* — 1q23.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.88× (z +14.2, q 1e-42, up in 34 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (2 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 0.586× (z -8.5, q 9e-15, down in 30 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF585A]] (+0.72, fdr 1e-05), [[PEX12]] (+0.71, fdr 7e-06), [[STK16]] (+0.71, fdr 7e-06); moves opposite to [[HACD3]] (-0.72, fdr 1e-05), [[MAPK9]] (-0.66, fdr 7e-06), [[CACYBP]] (-0.64, fdr 7e-06).
> It sits in the **+** arm of [[Module 012]] (mRNA Splicing - Major Pathway).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 3 with an alert ⚠; shown: the 15 strongest. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6708.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.88×** | +14.2 | 1e-42 | 34/45 (NCI-H460, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.99×** | +11.0 | 2e-25 | 36/47 (A498, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.62×** | +10.8 | 6e-25 | 29/42 (PANC-1, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.88×** | +10.0 | 2e-21 | 26/42 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.76×** | +8.6 | 8e-16 | 27/46 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.66×** | +8.0 | 8e-14 | 25/47 (A498, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.30×** | +5.9 | 2e-07 | 13/48 (MIA PaCa-2, NCI-H2347, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.46×** | +5.8 | 5e-07 | 17/43 (PANC-1, J82, …) | rises with dose | cell-cycle shift (explains ~13% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **1.44×** | +5.8 | 5e-07 | 14/47 (A498, A-172, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.28×** | +5.5 | 2e-06 | 16/48 (A-427, SW 900, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~9% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.37×** | +4.8 | 1e-04 | 16/42 (AsPC-1, PANC-1, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.40×** | +3.8 | 0.007 | 4/39 (CFPAC-1, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.26×** | +3.6 | 0.013 | 8/46 (hTERT-HPNE, HEC-1-A, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.25×** | +3.6 | 0.013 | 11/46 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.37×** | +3.6 | 0.014 | 5/43 (A498, NCI-H460, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 3 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6708.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.586×** | -8.5 | 9e-15 | 30/47 (PANC-1, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.590×** | -8.4 | 1e-14 | 26/46 (PANC-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.633×** | -7.3 | 6e-11 | 27/44 (COLO 205, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.634×** | -6.9 | 1e-09 | 24/43 (Hs 766T, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.657×** | -6.7 | 3e-09 | 21/47 (PANC-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.685×** | -6.0 | 1e-07 | 19/46 (PANC-1, SW480, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.731×** | -5.0 | 5e-05 | 20/46 (BT-474, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.789×** | -3.8 | 0.012 | 14/46 (NCI-H460, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Quinidine (15% dihydroquinidine) (drug)]] 5 µM |  | **0.807×** | -3.3 | 0.065 | 7/45 (SK-MEL-2, A549, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.754×** | -3.2 | 0.075 | 5/48 (NCI-H460, SW 900, …) | all doses, flat | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.815×** | -3.1 | 0.088 | 13/37 (A498, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | 0.825× | -3.1 | 0.10 | 7/47 (HEC-1-A, HT-29, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.14 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6708. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 10.5 | 1 | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.17× (z +8.6) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.281× (z -10.1) |
| [[NCI-H460 (line)]] | wt | 10.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.39× (z +12.6) | — |
| [[AsPC-1 (line)]] | alt | 6.34 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.120× (z -8.6) |
| [[BT-474 (line)]] | alt | 5.65 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0861× (z -8.7) |
| [[COLO 205 (line)]] | alt | 14.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0912× (z -10.8) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 15.5 | 0 | 1 | — | [[Bortezomib (drug)]] 0.05 µM 0.185× (z -9.0) |
| [[LoVo (line)]] | wt | 8.81 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.189× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[LOX-IMVI (line)]] | wt | 3.39 | 0 | 1 (1 ⚠) | — | [[Pitavastatin (Calcium) (drug)]] 5 µM 0.0684× (z -8.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H2030 (line)]] | alt | 10.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.64× (z +10.7) | — |
| [[NCI-H23 (line)]] | alt | 16.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.86× (z +9.2) | — |
| [[A-172 (line)]] | wt | 8.39 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 15.5 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 8.88 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.77 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.57 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 8.46 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.14 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.78 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.65 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 8.41 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.55 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 7.36 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.17 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 8.20 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.22 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 6.64 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 7.51 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 7.10 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.83 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.52 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.17 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.25 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.84 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.34 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.65 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.03 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.75 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.99 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.07 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.55 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.09 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.81 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.37 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 10.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6708), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF585A]] | +0.72 | +0.79 / +0.54 | both halves | 1e-05 |  |
| [[PEX12]] | +0.71 | +0.73 / +0.61 | both halves | 7e-06 |  |
| [[STK16]] | +0.71 | +0.76 / +0.62 | both halves | 7e-06 |  |
| [[FAM200A]] | +0.68 | +0.81 / +0.56 | both halves | 1e-05 |  |
| [[NAIF1]] | +0.68 | +0.77 / +0.58 | both halves | 8e-06 |  |
| [[PAN2]] | +0.68 | +0.82 / +0.46 | both halves | 3e-05 |  |
| [[AMZ2P1-1]] | +0.68 | +0.70 / +0.63 | both halves | 7e-06 |  |
| [[HHLA3]] | +0.67 | +0.77 / +0.69 | both halves | 7e-06 |  |
| [[ZNF687]] | +0.66 | +0.71 / +0.55 | both halves | 1e-05 |  |
| [[ZNF213]] | +0.66 | +0.76 / +0.38 | both halves | 6e-05 |  |
| [[ENO3]] | +0.66 | +0.73 / +0.56 | both halves | 1e-05 |  |
| [[TMEM42]] | +0.65 | +0.69 / +0.64 | both halves | 7e-06 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HACD3]] | -0.72 | -0.69 / -0.57 | both halves | 1e-05 |  |
| [[MAPK9]] | -0.66 | -0.62 / -0.58 | both halves | 7e-06 |  |
| [[CACYBP]] | -0.64 | -0.60 / -0.58 | both halves | 7e-06 |  |
| [[FAM20B]] | -0.63 | -0.64 / -0.58 | both halves | 7e-06 |  |
| [[PACC1]] | -0.63 | -0.68 / -0.43 | both halves | 3e-05 |  |
| [[NUTF2]] | -0.61 | -0.64 / -0.50 | both halves | 1e-05 |  |
| [[PIP4K2A]] | -0.60 | -0.73 / -0.43 | both halves | 3e-05 |  |
| [[C1orf216]] | -0.60 | -0.69 / -0.46 | both halves | 3e-05 |  |
| [[AP3M2]] | -0.59 | -0.65 / -0.44 | both halves | 3e-05 |  |
| [[WNK2]] | -0.59 | -0.48 / -0.51 | both halves | 2e-05 |  |
| [[AHSA1]] | -0.59 | -0.58 / -0.62 | both halves | 7e-06 |  |
| [[SORD]] | -0.58 | -0.58 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers METTL25B's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.5% of all compounds | 0.026 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[CMTM8]] | B | CMTM8 activity raises METTL25B's level | lines that do not express CMTM8 (9) vs lines expressing it (41) | 1.35× lower at baseline in the lines without CMTM8 | 0.072 | ⚠ within organs, on part of the lines; also absent: ALDH5A1, NUP210, PLEKHG3; maybe low, not absent |
| [[PSMB5]] | B | PSMB5 activity raises METTL25B's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **+** arm (projection on the module's main direction 0.551). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-33.2, 2.2); signed map (5.1, -20.5). **Vector** length 60.1, 8.42% of its response variance represented; |z| ≥ 3 in 986 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +5.8 | +14.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.9 | +10.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | +4.4 | +8.6 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +3.4 | +3.6 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +2.6 | +3.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.0 | +2.1 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.7 | +3.8 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.4 | +3.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.3 | +5.9 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | +1.2 | +2.7 |
| fall | [[Ixazomib citrate (drug)]] 5 µM |  | -4.5 | -8.5 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -3.6 | -6.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.1 | -6.0 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -2.7 | -2.7 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.6 | -8.4 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -2.2 | -3.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.8 | -2.3 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.4 | +1.8 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.3 | -0.2 |

## What is on record

|  |  |
|---|---|
| Name | methyltransferase like 25B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q23.1 — chr1:156,728,442-156,736,960 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CGI-41; previously C1orf66, RRNAD1 |
| Gene groups (HGNC) | 7BS orphan methyltransferases |
| Matched by | ensembl_id |

UniProt [Q96FB5](https://www.uniprot.org/uniprotkb/Q96FB5) carries no function annotation.

**Summary**, from NCBI Gene [51093](https://www.ncbi.nlm.nih.gov/gene/51093):

> Predicted to enable rRNA (adenine-N6,N6-)-dimethyltransferase activity. Predicted to be involved in rRNA methylation. Predicted to be located in membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:24273](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24273) · Entrez [51093](https://www.ncbi.nlm.nih.gov/gene/51093) · UniProt [Q96FB5](https://www.uniprot.org/uniprotkb/Q96FB5) · Ensembl [ENSG00000143303](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000143303)

## Data

Gene col 6708: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6708); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6708, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6708]; `tensor/DDL_lfc|DDL_z.npy` [6708]; `embed/gene_vectors.npy` [6708]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6708 or target_col == 6708). Every well: [[METTL25B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/METTL25B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
