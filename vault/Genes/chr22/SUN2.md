---
symbol: "SUN2"
type: "gene"
col: 1902
ensembl_id: "ENSG00000100242"
name: "Sad1 and UNC84 domain containing 2"
location: "22q13.1"
module: 22
arm: "+"
pooled_cpm: 33.45
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 18
n_dd_up_clean: 6
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/022"]
generated_by: "tahoemap"
---

# SUN2

*Sad1 and UNC84 domain containing 2* — 22q13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.71× (z +11.1, q 5e-26, up in 34 of 43 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ipatasertib (drug)]] 0.5 µM: 1.37× (z +4.7, q 3e-04, up in 19 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (5 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.529× (z -13.2, q 8e-37, down in 42 of 48 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Bortezomib (drug)]] 0.05 µM: 0.607× (z -9.7, q 5e-20, down in 35 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CNTROB]] (+0.62, fdr 1e-05), [[ACBD7]] (+0.60, fdr 3e-05), [[PRR11]] (+0.59, fdr 1e-05); moves opposite to [[SPR]] (-0.54, fdr 3e-05), [[COX10]] (-0.51, fdr 5e-05), [[PHF14]] (-0.50, fdr 3e-05).
> It is in [[Module 022]], a single-armed module (G2/M checkpoint).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[NAV2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 7 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1902.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.71×** | +11.1 | 5e-26 | 34/43 (A498, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.55×** | +8.8 | 4e-16 | 23/37 (A498, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.45×** | +7.1 | 2e-10 | 22/40 (HOP62, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~44% of this change | **1.35×** | +6.2 | 7e-08 | 23/46 (RPMI-7951, HS-578T, …) | inconsistent across doses | low cells (technical?) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.37×** | +4.7 | 3e-04 | 19/47 (A549, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 1.16× | +4.4 | 0.001 | 17/48 (RKO, SW1417, …) | top dose only | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | 1.14× | +3.9 | 0.007 | 10/48 (LS 180, KATO III, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.21×** | +3.9 | 0.007 | 15/48 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Canagliflozin (drug)]] 0.05 µM |  | **1.22×** | +3.8 | 0.009 | 10/47 (KATO III, SW480, …) | inconsistent across doses |  |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.39×** | +3.6 | 0.020 | 10/41 (HepG2/C3A, RKO, …) | top dose only | noisy plate (z scaled) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.24×** | +3.2 | 0.065 | 8/48 (SW1417, HCT15, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 0.5 µM |  | **1.24×** | +3.2 | 0.068 | 6/48 (RKO, NCI-H2030, …) | two highest doses | noisy plate (z scaled) |
| [[4EGI-1 (drug)]] 5 µM |  | **1.34×** | +3.1 | 0.072 | 4/47 (NCI-H460, C-33 A, …) | top dose only | noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | 1.17× | +3.1 | 0.082 | 10/47 (AsPC-1, RKO, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 9 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1902.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.529×** | -13.2 | 8e-37 | 42/48 (AsPC-1, PANC-1, …) | all doses, flat |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.607×** | -9.7 | 5e-20 | 35/48 (HT-29, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~20% here) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.656×** | -8.7 | 7e-16 | 28/48 (HOP62, NCI-H2347, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.657×** | -8.7 | 7e-16 | 37/48 (PANC-1, HOP62, …) | two highest doses |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.465×** | -8.3 | 2e-14 | 31/44 (HOP62, A-172, …) | all doses, flat | cell-cycle shift (explains ~19% here); noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.548×** | -6.5 | 7e-09 | 33/47 (Hs 766T, SW 900, …) | all doses, flat | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.549×** | -6.5 | 7e-09 | 29/48 (AsPC-1, NCI-H1792, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[EX229 (drug)]] 5 µM |  | **0.553×** | -6.4 | 1e-08 | 29/48 (SHP-77, PANC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.562×** | -6.2 | 3e-08 | 30/48 (MIA PaCa-2, PANC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.756×** | -5.8 | 4e-07 | 27/48 (HT-29, A-172, …) | rises with dose |  |
| [[Verteporfin (drug)]] 5 µM |  | **0.774×** | -5.1 | 2e-05 | 20/48 (HS-578T, A498, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~69% of this change | 0.841× | -5.0 | 2e-05 | 21/48 (HS-578T, NCI-H2347, …) | rises with dose | low cells (technical?) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.782×** | -4.8 | 8e-05 | 22/47 (NCI-H2030, C32, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.849× | -4.7 | 8e-05 | 20/48 (HEC-1-A, A549, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.792×** | -4.7 | 9e-05 | 23/47 (C32, HS-578T, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.798×** | -4.6 | 1e-04 | 21/48 (A-427, BT-474, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.803×** | -4.5 | 2e-04 | 21/48 (C32, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[venetoclax (drug)]] 5 µM |  | **0.679×** | -4.2 | 9e-04 | 18/48 (Hs 766T, NCI-H1792, …) | rises with dose | noisy plate (z scaled) |
| [[Amsacrine (drug)]] 5 µM |  | 0.870× | -4.1 | 0.001 | 14/48 (PANC-1, HOP62, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.808×** | -3.1 | 0.043 | 3/48 (NCI-H2030, AsPC-1, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.35 per unit of S-phase module lfc, +0.40 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1902. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 58.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.88× (z +11.9) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 45.9 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.22× (z +8.7) ⚠ toxic; transcription drop | [[Bortezomib (drug)]] 5 µM 0.149× (z -11.1) ⚠ toxic |
| [[PANC-1 (line)]] | alt | 23.7 | 0 | 2 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.425× (z -9.0) ⚠ unreliable plate only |
| [[RKO (line)]] | wt | 31.0 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.03× (z +12.1) ⚠ cell-cycle shift, would explain all of this change | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.213× (z -11.3) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[AsPC-1 (line)]] | alt | 34.1 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.333× (z -9.6) ⚠ unreliable plate only |
| [[HS-578T (line)]] | alt | 100 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.48× (z +9.7) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 28.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.434× (z -8.6) ⚠ cell-cycle shift, would explain all of this change |
| [[SW1417 (line)]] | alt | 29.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.14× (z +9.2) ⚠ cell-cycle shift, would explain all of this change | — |
| [[A-172 (line)]] | wt | 40.9 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 14.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 28.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 48.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 29.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 50.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 36.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 30.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 49.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 36.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 45.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 45.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 48.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 30.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 28.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 15.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 16.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 19.7 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 45.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 30.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 42.3 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 29.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 51.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 31.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 44.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 49.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 31.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 65.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 40.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 24.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 70.2 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 27.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1902), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CNTROB]] | +0.62 | +0.62 / +0.53 | both halves | 1e-05 | pathway: HALLMARK_MITOTIC_SPINDLE |
| [[ACBD7]] | +0.60 | +0.44 / +0.53 | both halves | 3e-05 |  |
| [[PRR11]] | +0.59 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[PTTG1]] | +0.57 | +0.51 / +0.51 | both halves | 1e-05 |  |
| [[ARHGAP33]] | +0.56 | +0.63 / +0.39 | both halves | 6e-05 |  |
| [[HMG20B]] | +0.56 | +0.38 / +0.54 | both halves | 7e-05 |  |
| [[PIF1]] | +0.55 | +0.56 / +0.51 | both halves | 1e-05 | pathway: HALLMARK_MITOTIC_SPINDLE |
| [[UBALD2]] | +0.55 | +0.55 / +0.57 | both halves | 1e-05 |  |
| [[CBX7]] | +0.54 | +0.43 / +0.46 | both halves | 3e-05 |  |
| [[NDE1]] | +0.54 | +0.50 / +0.51 | both halves | 1e-05 |  |
| [[NEK2]] | +0.54 | +0.51 / +0.46 | both halves | 3e-05 | pathway: HALLMARK_MITOTIC_SPINDLE |
| [[WDTC1]] | +0.54 | +0.38 / +0.60 | both halves | 6e-05 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPR]] | -0.54 | -0.57 / -0.46 | both halves | 3e-05 |  |
| [[COX10]] | -0.51 | -0.39 / -0.50 | both halves | 5e-05 |  |
| [[PHF14]] | -0.50 | -0.43 / -0.52 | both halves | 3e-05 |  |
| [[DNTTIP2]] | -0.49 | -0.43 / -0.48 | both halves | 3e-05 |  |
| [[NKRF]] | -0.49 | -0.45 / -0.53 | both halves | 3e-05 |  |
| [[COA6]] | -0.48 | -0.47 / -0.38 | both halves | 6e-05 |  |
| [[TSR1]] | -0.48 | -0.37 / -0.46 | both halves | 9e-05 |  |
| [[TRMT11]] | -0.48 | -0.47 / -0.42 | both halves | 4e-05 |  |
| [[LARS2]] | -0.48 | -0.38 / -0.51 | both halves | 7e-05 |  |
| [[MRM3]] | -0.47 | -0.36 / -0.42 | both halves | 1e-04 |  |
| [[PSMA4]] | -0.47 | -0.51 / -0.43 | both halves | 3e-05 |  |
| [[CCT6A]] | -0.47 | -0.43 / -0.47 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NAV2]] | B | NAV2 activity raises SUN2's level | lines that do not express NAV2 (17) vs lines expressing it (33) | 1.53× lower at baseline in the lines without NAV2 | 0.011 | ⚠ within organs, on part of the lines; also absent: NAV1, ROR1-AS1, CSF1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 022]] — G2/M checkpoint; 185 genes; every member is in the + arm (projection on the module's main direction 0.450). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-35.2, -58.2); signed map (-52.5, -40.8). **Vector** length 107, 25.4% of its response variance represented; |z| ≥ 3 in 881 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +4.8 | +4.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.6 | +8.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.5 | +7.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.4 | +11.1 |
|  | [[Panobinostat (drug)]] 5 µM |  | +3.9 | +3.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.5 | +4.7 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +2.5 | +2.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.5 | +1.9 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.4 | +2.3 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.4 | +1.1 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -8.0 | -13.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | -5.4 | -8.7 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -5.3 | -9.7 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | -4.9 | -8.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | -4.9 | -8.7 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -4.8 | -6.2 |
|  | [[TAK-733 (drug)]] 5 µM |  | -4.7 | -6.5 |
|  | [[EX229 (drug)]] 5 µM |  | -4.7 | -6.4 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -4.4 | -6.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.1 | -5.8 |

## What is on record

|  |  |
|---|---|
| Name | Sad1 and UNC84 domain containing 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q13.1 — chr22:38,733,290-38,794,143 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously UNC84B |
| Gene groups (HGNC) | SUN family |
| Hallmark sets | MITOTIC_SPINDLE |
| Reactome | 7 pathways, smallest: Meiotic synapsis; Meiosis; Dengue Virus Genome Translation and Replication |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UH99](https://www.uniprot.org/uniprotkb/Q9UH99) (SUN domain-containing protein 2):

> As a component of the LINC (LInker of Nucleoskeleton and Cytoskeleton) complex, involved in the connection between the nuclear lamina and the cytoskeleton. The nucleocytoplasmic interactions established by the LINC complex play an important role in the transmission of mechanical forces across the nuclear envelope and in nuclear movement and positioning. Specifically, SYNE2 and SUN2 assemble in arrays of transmembrane actin-associated nuclear (TAN) lines which are bound to F-actin cables and …

**Summary**, from NCBI Gene [25777](https://www.ncbi.nlm.nih.gov/gene/25777):

> SUN1 (MIM 607723) and SUN2 are inner nuclear membrane (INM) proteins that play a major role in nuclear-cytoplasmic connection by formation of a 'bridge' across the nuclear envelope, known as the LINC complex, via interaction with the conserved luminal KASH domain of nesprins (e.g., SYNE1; MIM 608441) located in the outer nuclear membrane (ONM). The LINC complex provides a direct connection between the nuclear lamina and the cytoskeleton, which contributes to nuclear positioning and cellular …

**Accessions** — [HGNC:14210](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14210) · Entrez [25777](https://www.ncbi.nlm.nih.gov/gene/25777) · UniProt [Q9UH99](https://www.uniprot.org/uniprotkb/Q9UH99) · Ensembl [ENSG00000100242](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100242)

## Data

Gene col 1902: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1902); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1902, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1902]; `tensor/DDL_lfc|DDL_z.npy` [1902]; `embed/gene_vectors.npy` [1902]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1902 or target_col == 1902). Every well: [[SUN2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SUN2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
