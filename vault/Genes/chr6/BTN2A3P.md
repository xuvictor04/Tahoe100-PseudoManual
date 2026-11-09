---
symbol: "BTN2A3P"
type: "gene"
col: 4540
ensembl_id: "ENSG00000124549"
name: "butyrophilin subfamily 2 member A3, pseudogene"
location: "6p22.2"
module: 94
arm: "+"
pooled_cpm: 3.41
n_lines_expressing: 49
n_dd_up: 17
n_dd_down: 1
n_dd_up_clean: 13
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/094"]
generated_by: "tahoemap"
---

# BTN2A3P

*butyrophilin subfamily 2 member A3, pseudogene* — 6p22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.71× (z +15.5, q 0e+00, up in 30 of 35 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Ritonavir (drug)]] 0.5 µM: 0.695× (z -4.1, q 0.028, down in 10 of 38 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[LJI308 (drug)]] 0.05 µM in 1 line (PANC-1 0.0589×); [[Clotrimazole (drug)]] 0.5 µM in 1 line (NCI-H1792 0.0749×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BTN2A3P-1]] (+0.92, fdr 7e-06, ⚠ same locus), [[BTN2A2]] (+0.74, fdr 7e-06, ⚠ same locus), [[BTN2A1]] (+0.69, fdr 1e-05, ⚠ same locus), [[ZNF563]] (+0.65, fdr 1e-05), [[C7orf31]] (+0.64, fdr 3e-05), [[HLA-V-1]] (+0.61, fdr 2e-05); moves opposite to [[MAPK1]] (-0.63, fdr 1e-05), [[NOMO1]] (-0.62, fdr 2e-05), [[SLC25A39]] (-0.61, fdr 1e-05).
> It is in [[Module 094]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[IRAG2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 5 with an alert ⚠. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4540.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.71×** | +15.5 | 0e+00 | 30/35 (J82, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.15×** | +8.4 | 1e-14 | 19/36 (J82, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.17×** | +7.6 | 6e-12 | 23/39 (J82, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.62×** | +5.5 | 5e-06 | 2/12 (SNU-423, LoVo) | all doses, flat | cell-cycle shift (explains ~10% here); noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.61×** | +5.2 | 2e-05 | 13/39 (RPMI-7951, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.73×** | +4.9 | 1e-04 | 11/37 (NCI-H2347, KATO III, …) | all doses, flat | cell-cycle shift (explains ~16% here); noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.34×** | +4.5 | 4e-04 | 10/44 (HOP62, J82, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.53×** | +4.1 | 0.002 | 6/19 (A-172, J82, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.12× | +3.9 | 0.007 | 4/47 (MIA PaCa-2, NCI-H23, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.42×** | +3.8 | 0.007 | 4/44 (CFPAC-1, J82, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.42×** | +3.8 | 0.007 | 12/42 (A-427, RKO, …) | top dose only |  |
| [[Cysteamine (hydrochloride) (drug)]] 0.5 µM |  | **1.35×** | +3.2 | 0.053 | 5/36 (HCT15, NCI-H460, …) | inconsistent across doses |  |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.51×** | +3.2 | 0.053 | 3/10 (PANC-1, A-172, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM |  | **1.34×** | +3.2 | 0.053 | 7/40 (J82, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~17% here) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.48×** | +3.1 | 0.080 | 4/41 (SK-MEL-2, A-172, …) | all doses, flat | noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.32×** | +3.0 | 0.087 | 4/42 (SNU-423, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.32×** | +3.0 | 0.087 | 3/42 (SK-MEL-2, CFPAC-1, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.31×** | +3.0 | 0.095 | 11/39 (NCI-H2347, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~5% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4540.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[LJI308 (drug)]] 0.05 µM in 1 line (PANC-1 0.0589×); [[Clotrimazole (drug)]] 0.5 µM in 1 line (NCI-H1792 0.0749×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ritonavir (drug)]] 0.5 µM |  | **0.695×** | -4.1 | 0.028 | 10/38 (RPMI-7951, Hs 766T, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | 0.544× | -3.5 | 0.11 | 7/36 (SNU-423, Panc 03.27, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~14% here); composition shift; noisy plate (z scaled) |
| [[Olanzapine (drug)]] 5 µM |  | 0.811× | -3.3 | 0.17 | 6/43 (H4, RKO, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, -0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4540. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CFPAC-1 (line)]] | alt | 4.19 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.53× (z +10.1) | — |
| [[HOP62 (line)]] | alt | 4.13 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.50× (z +8.5) | — |
| [[J82 (line)]] | alt | 8.41 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.43× (z +11.7) | — |
| [[NCI-H1792 (line)]] | alt | 4.99 | 0 | 1 | — | [[Clotrimazole (drug)]] 0.5 µM 0.0749× (z -8.8) |
| [[PANC-1 (line)]] | alt | 2.46 | 0 | 1 | — | [[LJI308 (drug)]] 0.05 µM 0.0589× (z -9.2) |
| [[A-172 (line)]] | wt | 3.81 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.73 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.38 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.30 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.83 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.51 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.58 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.70 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.20 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.39 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.84 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.17 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.57 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.95 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.35 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.68 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.31 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.76 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.97 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.80 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 4.71 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.62 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.381 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.77 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.40 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.59 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.76 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.03 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.72 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.48 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.99 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.60 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.85 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.03 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.85 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.25 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.74 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.67 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 6.12 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.07 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.68 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.97 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.43 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.91 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4540), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 5 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BTN2A3P-1]] | +0.92 | +0.93 / +0.82 | both halves | 7e-06 | ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[BTN2A2]] | +0.74 | +0.78 / +0.69 | both halves | 7e-06 | same gene group; ⚠ same locus (27.2 kb, same strand: neighbours can correlate without regulation) |
| [[BTN2A1]] | +0.69 | +0.69 / +0.54 | both halves | 1e-05 | same gene group; ⚠ same locus (26.3 kb, same strand: neighbours can correlate without regulation) |
| [[ZNF563]] | +0.65 | +0.71 / +0.50 | both halves | 1e-05 |  |
| [[C7orf31]] | +0.64 | +0.70 / +0.45 | both halves | 3e-05 |  |
| [[HLA-V-1]] | +0.61 | +0.48 / +0.52 | both halves | 2e-05 |  |
| [[DUSP15]] | +0.60 | +0.67 / +0.53 | both halves | 1e-05 |  |
| [[PAXIP1-AS2]] | +0.60 | +0.68 / +0.44 | both halves | 3e-05 |  |
| [[MITD1]] | +0.60 | +0.66 / +0.48 | both halves | 2e-05 |  |
| [[ZNF442]] | +0.59 | +0.67 / +0.46 | both halves | 2e-05 |  |
| [[APBA3]] | +0.59 | +0.51 / +0.62 | both halves | 1e-05 |  |
| [[GPRASP3]] | +0.59 | +0.64 / +0.43 | both halves | 3e-05 |  |
| [[ZNF226]] | +0.59 | +0.59 / +0.48 | both halves | 2e-05 |  |
| [[OCIAD1]] | +0.58 | +0.62 / +0.42 | both halves | 4e-05 |  |
| [[CLK4]] | +0.58 | +0.59 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAPK1]] | -0.63 | -0.62 / -0.52 | both halves | 1e-05 |  |
| [[NOMO1]] | -0.62 | -0.58 / -0.49 | both halves | 2e-05 |  |
| [[SLC25A39]] | -0.61 | -0.52 / -0.51 | both halves | 1e-05 |  |
| [[CHID1]] | -0.60 | -0.58 / -0.50 | both halves | 1e-05 |  |
| [[CTXN1]] | -0.60 | -0.63 / -0.35 | both halves | 1e-04 |  |
| [[WRNIP1]] | -0.59 | -0.65 / -0.46 | both halves | 3e-05 |  |
| [[TRAPPC9]] | -0.58 | -0.46 / -0.42 | both halves | 4e-05 |  |
| [[CCNY]] | -0.58 | -0.56 / -0.58 | both halves | 1e-05 |  |
| [[NUTF2]] | -0.57 | -0.59 / -0.42 | both halves | 4e-05 |  |
| [[BLTP2]] | -0.56 | -0.60 / -0.42 | both halves | 4e-05 |  |
| [[RSU1]] | -0.56 | -0.59 / -0.31 | both halves | 2e-04 |  |
| [[HYAL2]] | -0.55 | -0.49 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IRAG2]] | B | IRAG2 activity raises BTN2A3P's level | lines that do not express IRAG2 (39) vs lines expressing it (11) | 1.36× lower at baseline in the lines without IRAG2 | 0.063 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CARMN, GDNF, LINC01411 |
| [[MR1]] | B | MR1 activity raises BTN2A3P's level | lines that do not express MR1 (5) vs lines expressing it (45) | 1.43× lower at baseline in the lines without MR1 | 0.090 | ⚠ within organs, on part of the lines; co-occurs with CTNNB1; also absent: GGT7, AGK, TCTN1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 094]]; 49 genes; every member is in the + arm (projection on the module's main direction 0.651). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.38; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (19.5, 6.6); signed map (17.8, -13.7). **Vector** length 52.6, 6.99% of its response variance represented; |z| ≥ 3 in 879 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +4.8 | +15.5 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | +3.6 | +4.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | +3.6 | +7.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.4 | +8.4 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +2.6 | +5.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.8 | +3.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.4 | +2.8 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.4 | +3.0 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.2 | +1.0 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.2 | +2.5 |
| fall | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.5 | -1.9 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.4 | -1.3 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.3 | -0.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.7 | -1.7 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -1.5 | -1.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.5 | -1.8 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.3 | -1.8 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.1 | -1.8 |
|  | [[Palmatine (chloride) (drug)]] 0.05 µM |  | -1.1 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | butyrophilin subfamily 2 member A3, pseudogene |
| Locus type | pseudogene |
| Location | 6p22.2 — chr6:26,422,119-26,431,615 (+) |
| Ensembl biotype | transcribed_unprocessed_pseudogene |
| Also known as | BTN2.3; previously BTN2A3 |
| Gene groups (HGNC) | Butyrophilins |
| Matched by | ensembl_id |

UniProt [Q96KV6](https://www.uniprot.org/uniprotkb/Q96KV6) carries no function annotation.

**Summary**, from NCBI Gene [54718](https://www.ncbi.nlm.nih.gov/gene/54718):

> The butyrophilin (BTN) genes are a group of major histocompatibility complex (MHC)-associated genes that encode type I membrane proteins with 2 extracellular immunoglobulin (Ig) domains and an intracellular B30.2 (PRYSPRY) domain. Three subfamilies of human BTN genes are located in the MHC class I region: the single-copy BTN1A1 gene (MIM 601610) and the BTN2 (e.g., BTN2A3) and BTN3 (e.g., BNT3A1; MIM 613593) genes, which have undergone tandem duplication, resulting in 3 copies of each (summary …

**Accessions** — [HGNC:13229](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13229) · Entrez [54718](https://www.ncbi.nlm.nih.gov/gene/54718) · UniProt [Q96KV6](https://www.uniprot.org/uniprotkb/Q96KV6) · Ensembl [ENSG00000124549](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000124549)

## Data

Gene col 4540: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4540); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4540, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4540]; `tensor/DDL_lfc|DDL_z.npy` [4540]; `embed/gene_vectors.npy` [4540]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4540 or target_col == 4540). Every well: [[BTN2A3P — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BTN2A3P.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
