---
symbol: "KRT10-AS1"
type: "gene"
col: 9558
ensembl_id: "ENSG00000167920"
name: "KRT10 antisense RNA 1"
location: "17q21.2"
module: 11
arm: "+"
pooled_cpm: 6.4
n_lines_expressing: 49
n_dd_up: 27
n_dd_down: 10
n_dd_up_clean: 20
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/011"]
generated_by: "tahoemap"
---

# KRT10-AS1

*KRT10 antisense RNA 1* — 17q21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.85× (z +8.9, q 4e-16, up in 8 of 11 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.49× (z +8.4, q 1e-14, up in 24 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (4 with an alert ⚠); the strongest is [[Doxorubicin (hydrochloride) (drug)]] 5 µM: 0.631× (z -6.6, q 2e-08, down in 20 of 41 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EPC1]] (+0.69, fdr 7e-06), [[THAP6]] (+0.67, fdr 1e-05), [[PEX12]] (+0.65, fdr 7e-06); moves opposite to [[LMBR1]] (-0.59, fdr 1e-05), [[DIAPH1]] (-0.53, fdr 1e-05), [[VAV2]] (-0.52, fdr 4e-05).
> It sits in the **+** arm of [[Module 011]] (Mitochondrial translation elongation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9558.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.85×** | +8.9 | 4e-16 | 8/11 (HT-29, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.49×** | +8.4 | 1e-14 | 24/47 (NCI-H2030, CFPAC-1, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.54×** | +6.2 | 1e-07 | 13/31 (CFPAC-1, A-427, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.43×** | +5.3 | 1e-05 | 11/40 (NCI-H23, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~22% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.57×** | +4.8 | 2e-04 | 5/34 (PANC-1, NCI-H1573, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.34×** | +4.4 | 9e-04 | 10/45 (A-427, SHP-77, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.34×** | +4.4 | 9e-04 | 11/44 (A-427, RKO, …) | inconsistent across doses |  |
| [[Canagliflozin (drug)]] 0.05 µM |  | **1.37×** | +4.4 | 9e-04 | 5/39 (HOP62, NCI-H2030, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.5 µM |  | **1.33×** | +4.3 | 0.001 | 6/44 (SNU-1, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.31×** | +4.0 | 0.004 | 8/45 (LS 180, SK-MEL-2, …) | all doses, flat |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.30×** | +4.0 | 0.004 | 7/45 (A-427, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~9% here) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.41×** | +3.7 | 0.010 | 3/40 (NCI-H460, A-427, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.30×** | +3.6 | 0.012 | 6/18 (NCI-H1573, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~9% of this change | 1.19× | +3.6 | 0.012 | 3/47 (SHP-77, H4, …) | rises with dose |  |
| [[Bendamustine (drug)]] 5 µM |  | **1.27×** | +3.5 | 0.018 | 4/41 (HEC-1-A, COLO 205, …) | top dose only |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.38×** | +3.4 | 0.021 | 7/42 (HT-29, CFPAC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.24×** | +3.3 | 0.036 | 4/44 (KATO III, A549, …) | all doses, flat |  |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.34×** | +3.1 | 0.049 | 5/44 (HEC-1-A, NCI-H460, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.05 µM |  | **1.23×** | +3.1 | 0.049 | 0/46 | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 4 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9558.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.631×** | -6.6 | 2e-08 | 20/41 (NCI-H23, A-427, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.656×** | -6.3 | 7e-08 | 18/46 (LS 180, H4, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.669×** | -6.0 | 3e-07 | 17/46 (SW480, AsPC-1, …) | all doses, flat | cell-cycle shift (explains ~5% here); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.714×** | -4.8 | 3e-04 | 18/43 (SK-MEL-2, A498, …) | inconsistent across doses | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.731×** | -4.7 | 3e-04 | 17/46 (NCI-H1792, SW1417, …) | all doses, flat | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.742×** | -4.5 | 7e-04 | 15/46 (NCI-H1792, SW1417, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.759×** | -4.1 | 0.003 | 11/44 (LS 180, J82, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.771×** | -3.7 | 0.013 | 9/41 (HS-578T, RPMI-7951, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.788×** | -3.6 | 0.022 | 10/44 (SW480, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.790×** | -3.5 | 0.023 | 9/45 (PANC-1, SW1417, …) | all doses, flat | position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | 0.860× | -3.2 | 0.067 | 10/47 (NCI-H2030, J82, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.22 per unit of S-phase module lfc, +0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9558. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SNU-423 (line)]] | alt | 6.71 | 0 | 2 | — | [[Hydroxyurea (drug)]] 0.05 µM 0.112× (z -8.5) |
| [[SW 900 (line)]] | alt | 5.00 | 0 | 2 | — | [[Clotrimazole (drug)]] 0.5 µM 0.0692× (z -9.6) |
| [[C32 (line)]] | wt | 5.83 | 0 | 1 | — | [[Dimethyl fumarate (drug)]] 0.05 µM 0.0584× (z -10.0) |
| [[HEC-1-A (line)]] | alt | 7.28 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.186× (z -9.1) ⚠ transcription drop; cell-cycle shift, explains ~53% of this change |
| [[J82 (line)]] | alt | 4.39 | 0 | 1 | — | [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM 0.0970× (z -8.9) |
| [[LS 180 (line)]] | wt | 3.75 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.0491× (z -10.9) |
| [[SK-MEL-2 (line)]] | alt | 8.03 | 0 | 1 | — | [[Bortezomib (drug)]] 0.05 µM 0.105× (z -9.0) |
| [[A-172 (line)]] | wt | 7.00 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 7.02 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 7.95 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 6.64 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.76 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.71 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.60 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.53 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.18 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.39 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.77 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.86 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.20 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.86 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.43 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.39 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.47 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.27 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.01 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.78 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 7.35 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 8.62 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.18 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.23 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 5.36 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.43 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.43 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 3.52 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 7.70 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 8.91 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.35 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.03 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.81 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.91 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.11 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.93 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 5.83 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9558), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EPC1]] | +0.69 | +0.69 / +0.67 | both halves | 7e-06 |  |
| [[THAP6]] | +0.67 | +0.67 / +0.57 | both halves | 1e-05 |  |
| [[PEX12]] | +0.65 | +0.66 / +0.65 | both halves | 7e-06 |  |
| [[PGGT1B]] | +0.64 | +0.54 / +0.61 | both halves | 1e-05 |  |
| [[SPOP]] | +0.62 | +0.65 / +0.60 | both halves | 7e-06 |  |
| [[CZIB]] | +0.61 | +0.52 / +0.59 | both halves | 1e-05 |  |
| [[ZNF226]] | +0.60 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[GIN1]] | +0.60 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[ZKSCAN4]] | +0.59 | +0.60 / +0.57 | both halves | 1e-05 |  |
| [[MED18]] | +0.59 | +0.62 / +0.54 | both halves | 1e-05 |  |
| [[FAM200A]] | +0.59 | +0.58 / +0.51 | both halves | 1e-05 |  |
| [[ASTE1]] | +0.59 | +0.62 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LMBR1]] | -0.59 | -0.58 / -0.50 | both halves | 1e-05 |  |
| [[DIAPH1]] | -0.53 | -0.51 / -0.52 | both halves | 1e-05 |  |
| [[VAV2]] | -0.52 | -0.56 / -0.40 | both halves | 4e-05 |  |
| [[PPM1G]] | -0.52 | -0.35 / -0.47 | both halves | 1e-04 |  |
| [[TCF3]] | -0.51 | -0.55 / -0.42 | both halves | 4e-05 |  |
| [[LRP8]] | -0.51 | -0.52 / -0.48 | both halves | 2e-05 |  |
| [[SRPK1]] | -0.51 | -0.51 / -0.50 | both halves | 1e-05 |  |
| [[PRR5-ARHGAP8]] | -0.51 | -0.51 / -0.39 | both halves | 5e-05 |  |
| [[TTL]] | -0.51 | -0.51 / -0.52 | both halves | 1e-05 |  |
| [[TPST2]] | -0.51 | -0.55 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises KRT10-AS1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[PSMB5]] | B | PSMB5 activity raises KRT10-AS1's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 011]] — Mitochondrial translation elongation; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.484). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-27.8, 17.0); signed map (5.1, -19.8). **Vector** length 52.2, 6.50% of its response variance represented; |z| ≥ 3 in 824 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +5.0 | +8.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.2 | +6.2 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +3.1 | +2.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.0 | +5.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.6 | +4.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.4 | +4.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.3 | +4.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.1 | +2.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.5 | +2.9 |
| fall | [[Ixazomib citrate (drug)]] 5 µM |  | -2.3 | -6.3 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -2.1 | -4.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | -2.0 | -3.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -1.9 | -6.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.8 | -4.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.1 | -1.9 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.0 | -1.4 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | -1.0 | -0.7 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.0 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | KRT10 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 17q21.2 — chr17:40,819,101-40,836,270 (+) |
| Ensembl biotype | lncRNA |
| Also known as | MGC21518; previously TMEM99 |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

UniProt [Q8N816](https://www.uniprot.org/uniprotkb/Q8N816) carries no function annotation.

**Summary**, from NCBI Gene [147184](https://www.ncbi.nlm.nih.gov/gene/147184):

> Predicted to be located in membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:28305](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28305) · Entrez [147184](https://www.ncbi.nlm.nih.gov/gene/147184) · UniProt [Q8N816](https://www.uniprot.org/uniprotkb/Q8N816) · Ensembl [ENSG00000167920](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000167920)

## Data

Gene col 9558: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9558); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9558, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9558]; `tensor/DDL_lfc|DDL_z.npy` [9558]; `embed/gene_vectors.npy` [9558]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9558 or target_col == 9558). Every well: [[KRT10-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KRT10-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
