---
symbol: "FST"
type: "gene"
col: 5554
ensembl_id: "ENSG00000134363"
name: "follistatin"
location: "5q11.2"
module: 81
arm: "+"
pooled_cpm: 9.35
n_lines_expressing: 24
n_dd_up: 13
n_dd_down: 5
n_dd_up_clean: 5
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 2
direction_downstream: 5
tags: ["gene", "module/081"]
generated_by: "tahoemap"
---

# FST

*follistatin* — 5q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.94× (z +9.2, q 1e-17, up in 6 of 13 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.85× (z +6.0, q 2e-07, up in 7 of 20 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.589× (z -5.3, q 8e-05, down in 15 of 19 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GNG11]] (+0.64, fdr 1e-05), [[SERPIND1]] (+0.64, fdr 7e-06), [[SEMA3A]] (+0.63, fdr 1e-05); moves opposite to [[ACSL1]] (-0.50, fdr 6e-05), [[TRAM2]] (-0.48, fdr 2e-04), [[TSC22D3]] (-0.47, fdr 4e-05).
> It is in [[Module 081]], a single-armed module (KRAS signaling up).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[COL4A6]] → it (grade C ⚠); 5 go from it, the strongest it → [[MAOA]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 8 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5554.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.94×** | +9.2 | 1e-17 | 6/13 (hTERT-HPNE, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.72×** | +9.2 | 1e-17 | 12/18 (hTERT-HPNE, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.36×** | +7.8 | 9e-13 | 8/13 (hTERT-HPNE, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.85×** | +6.0 | 2e-07 | 7/20 (A-172, J82, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **2.00×** | +4.8 | 2e-04 | 6/20 (HOP62, hTERT-HPNE, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.04×** | +4.8 | 2e-04 | 8/15 (NCI-H2347, Panc 03.27, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **3.06×** | +4.1 | 0.003 | 1/8 (NCI-H2347) | top dose only | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **1.74×** | +3.7 | 0.014 | 9/20 (hTERT-HPNE, NCI-H2347, …) | top dose only |  |
| [[vincristine (drug)]] 0.5 µM |  | **2.66×** | +3.6 | 0.019 | 9/20 (SW 900, LoVo, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.66×** | +3.5 | 0.024 | 5/20 (A-172, LoVo, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~45% of this change | **1.65×** | +3.5 | 0.024 | 5/17 (SW 900, HS-578T, …) | inconsistent across doses | low cells (technical?) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.41×** | +3.4 | 0.037 | 7/20 (SW 900, HOP62, …) | top dose only |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **2.33×** | +3.1 | 0.076 | 5/20 (HepG2/C3A, HOP62, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, none with an alert. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5554.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.589×** | -5.3 | 8e-05 | 15/19 (NCI-H460, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.508×** | -4.8 | 6e-04 | 16/21 (HepG2/C3A, Hs 766T, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.541×** | -4.3 | 0.003 | 14/21 (Hs 766T, HOP62, …) | all doses, stronger at high dose | position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.610×** | -3.5 | 0.070 | 11/20 (NCI-H460, HepG2/C3A, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.592×** | -3.4 | 0.074 | 6/20 (NCI-H460, NCI-H1792, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM |  | 0.630× | -3.3 | 0.11 | 12/21 (Hs 766T, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, +0.50 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5554. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[Hs 766T (line)]] | wt | 43.3 | 0 | 7 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0423× (z -14.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.0587× (z -12.9) |
| [[NCI-H460 (line)]] | wt | 45.5 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.130× (z -17.4) |
| [[HepG2_C3A (line)]] | wt | 48.9 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0432× (z -14.8) |
| [[SHP-77 (line)]] | alt | 8.60 | 0 | 3 (1 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.0385× (z -9.3) ⚠ cell-cycle shift, explains ~48% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.121× (z -9.1) |
| [[A549 (line)]] | wt | 19.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.171× (z -9.3) |
| [[hTERT-HPNE (line)]] | wt | 46.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 10.5× (z +9.0) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 18.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.227× (z -10.0) |
| [[A-172 (line)]] | wt | 5.40 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.07 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.984 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 2.02 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.02 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.844 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.40 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 5.90 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.52 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.74 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.831 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 8.20 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.63 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.952 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.17 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 2.51 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.803 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 23.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.97 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.804 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.711 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.70 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 5.29 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.846 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.871 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 194 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 29.4 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.959 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.908 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.27 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.26 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.963 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.86 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 3.60 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.35 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.828 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.15 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.774 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5554), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GNG11]] | +0.64 | +0.65 / +0.55 | both halves | 1e-05 | **novel candidate** |
| [[SERPIND1]] | +0.64 | +0.61 / +0.68 | both halves | 7e-06 |  |
| [[SEMA3A]] | +0.63 | +0.55 / +0.63 | both halves | 1e-05 |  |
| [[SMOC1]] | +0.61 | +0.54 / +0.56 | both halves | 1e-05 | STRING 786 |
| [[ESM1]] | +0.60 | +0.45 / +0.64 | both halves | 3e-05 |  |
| [[AMIGO2]] | +0.57 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[AADACP1]] | +0.56 | +0.40 / +0.62 | both halves | 5e-05 |  |
| [[COL4A6]] | +0.56 | +0.48 / +0.55 | both halves | 2e-05 |  |
| [[EYA2]] | +0.56 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[PRDM8]] | +0.56 | +0.49 / +0.57 | both halves | 1e-05 |  |
| [[TFPI2]] | +0.56 | +0.53 / +0.52 | both halves | 1e-05 |  |
| [[FAM107B]] | +0.55 | +0.54 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ACSL1]] | -0.50 | -0.38 / -0.60 | both halves | 6e-05 | pathway: HALLMARK_MYOGENESIS |
| [[TRAM2]] | -0.48 | -0.32 / -0.60 | both halves | 2e-04 |  |
| [[TSC22D3]] | -0.47 | -0.42 / -0.51 | both halves | 4e-05 |  |
| [[ALDH2]] | -0.45 | -0.43 / -0.44 | both halves | 3e-05 |  |
| [[COPS8]] | -0.44 | -0.36 / -0.51 | both halves | 1e-04 |  |
| [[GLUL]] | -0.43 | -0.35 / -0.54 | both halves | 1e-04 |  |
| [[IRAK3]] | -0.43 | -0.33 / -0.48 | both halves | 1e-04 |  |
| [[MAOA]] | -0.43 | -0.36 / -0.49 | both halves | 9e-05 |  |
| [[HSD17B4]] | -0.43 | -0.36 / -0.47 | both halves | 1e-04 |  |
| [[TNS2]] | -0.43 | -0.34 / -0.44 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[COL4A6]] | C | COL4A6 activity raises FST's level | lines that do not express COL4A6 (36) vs lines expressing it (14) | 4.11× lower at baseline in the lines without COL4A6 | 0.064 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SOX7, ENSG00000238054, LINC01035; co-absent with the target |
| [[IL1B]] | C | IL1B activity raises FST's level | lines that do not express IL1B (30) vs lines expressing it (20) | 2.76× lower at baseline in the lines without IL1B | 0.094 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: IL7R, ADAMTS12, EDNRA; co-absent with the target |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAOA]] | B | FST activity strengthens MAOA's drug response | lines that do not express FST (18) vs lines expressing it (16) | the lines without FST respond 0.44× as strongly (z diff +1.33); strongest at Clobetasol propionate 0.5 µM: 1.67x vs 4.28x (z diff +2.4) | 0.011 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: IDO1, FN1, CDH2; target measured in part of the lines; the reference differs |
| [[DENND5B-AS1]] | B | FST activity lowers DENND5B-AS1's level | lines that do not express FST (26) vs lines expressing it (24) | 1.21× higher at baseline in the lines without FST | 0.038 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: IDO1, FN1, CDH2 |
| [[CLDN10-AS1]] | B | FST activity raises CLDN10-AS1's level | lines that do not express FST (26) vs lines expressing it (24) | 1.94× lower at baseline in the lines without FST | 0.086 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: IDO1, FN1, CDH2 |
| [[BIN1]] | B | FST activity strengthens BIN1's drug response | lines that do not express FST (24) vs lines expressing it (20) | the lines without FST respond 0.81× as strongly (z diff +0.61); strongest at Idarubicin (hydrochloride) 5 µM: 1.06x vs 1.62x (z diff +3.0) | 0.096 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: IDO1, FN1, CDH2; target measured in part of the lines; artifact flags |
| [[IL33]] | C | FST activity raises IL33's level | lines that do not express FST (26) vs lines expressing it (24) | 2.01× lower at baseline in the lines without FST | 0.085 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: IDO1, FN1, CDH2; co-absent with the target |

## Where it sits

- **Module**: [[Module 081]] — KRAS signaling up; 55 genes; every member is in the + arm (projection on the module's main direction 0.506). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (45.1, 15.5); signed map (18.6, 52.6). **Vector** length 60.5, 16.2% of its response variance represented; |z| ≥ 3 in 574 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.6 | +9.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.4 | +9.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.2 | +7.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.8 | +6.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.4 | +4.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.7 | +2.0 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.5 | +2.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.5 | +2.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.4 | -0.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.4 | +2.7 |
| fall | [[Dexamethasone (drug)]] 0.5 µM |  | -2.5 | -2.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.3 | -3.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~75% of this change | -2.2 | -1.4 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -2.2 | -4.3 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -2.1 | -2.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.0 | -3.5 |

## What is on record

|  |  |
|---|---|
| Name | follistatin |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q11.2 — chr5:53,480,626-53,487,134 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FS |
| Hallmark sets | MYOGENESIS |
| Reactome | 3 pathways, smallest: Antagonism of Activin by Follistatin; Signaling by Activin; Signaling by TGFB family members |
| Matched by | ensembl_id |

**Function**, from UniProt [P19883](https://www.uniprot.org/uniprotkb/P19883) (Follistatin):

> Multifunctional regulatory protein whose primary function is to antagonize members of the transforming growth factor beta (TGF-beta) superfamily including activin, myostatin, GDF11 or bone morphogenetic proteins (BMPs). Mechanistically, binds to these ligands in the extracellular space, blocking their type II receptor-binding site to inhibit downstream signaling. Plays an essential role in muscle fiber formation and growth both by preventing the repressive effects of myostatin and through …

**Summary**, from NCBI Gene [10468](https://www.ncbi.nlm.nih.gov/gene/10468):

> Follistatin is a single-chain gonadal protein that specifically inhibits follicle-stimulating hormone release. The single FST gene encodes two isoforms, FST317 and FST344 containing 317 and 344 amino acids respectively, resulting from alternative splicing of the precursor mRNA. In a study in which 37 candidate genes were tested for linkage and association with polycystic ovary syndrome (PCOS) or hyperandrogenemia in 150 families, evidence was found for linkage between PCOS and follistatin. …

**Accessions** — [HGNC:3971](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3971) · Entrez [10468](https://www.ncbi.nlm.nih.gov/gene/10468) · UniProt [P19883](https://www.uniprot.org/uniprotkb/P19883) · Ensembl [ENSG00000134363](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000134363)

## Data

Gene col 5554: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5554); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5554, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5554]; `tensor/DDL_lfc|DDL_z.npy` [5554]; `embed/gene_vectors.npy` [5554]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5554 or target_col == 5554). Every well: [[FST — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FST.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
