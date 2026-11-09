---
symbol: "CSF2"
type: "gene"
col: 8941
ensembl_id: "ENSG00000164400"
name: "colony stimulating factor 2"
location: "5q31.1"
module: 112
arm: "+"
pooled_cpm: 5.57
n_lines_expressing: 24
n_dd_up: 24
n_dd_down: 16
n_dd_up_clean: 14
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 25
direction_downstream: 34
tags: ["gene", "module/112"]
generated_by: "tahoemap"
---

# CSF2

*colony stimulating factor 2* — 5q31.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (10 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 4.78× (z +10.1, q 2e-21, up in 16 of 20 measured lines) ⚠ cell-cycle shift, explains ~33% of this change. The strongest without an alert is [[Harringtonine (drug)]] 5 µM: 9.96× (z +10.1, q 2e-21, up in 21 of 21 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.408× (z -4.1, q 0.025, down in 16 of 22 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MIR3142HG]] (+0.75, fdr 7e-06), [[TRAF1]] (+0.75, fdr 7e-06), [[IL1A]] (+0.74, fdr 7e-06); moves opposite to [[NPR3]] (-0.53, fdr 2e-05), [[LOX]] (-0.50, fdr 3e-05).
> It is in [[Module 112]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 25 arrows point to it, the strongest [[CXCL3]] → it (grade B ⚠); 34 go from it, the strongest it → [[CD82]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 10 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8941.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **4.78×** | +10.1 | 2e-21 | 16/20 (CFPAC-1, Panc 03.27, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **9.96×** | +10.1 | 2e-21 | 21/21 (HOP62, A-172, …) | rises with dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **6.80×** | +8.8 | 4e-16 | 16/17 (HOP62, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **6.24×** | +8.4 | 9e-15 | 18/20 (HOP62, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **5.19×** | +7.2 | 5e-11 | 11/13 (SW 900, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~17% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **5.28×** | +7.0 | 2e-10 | 7/8 (HOP62, J82, …) | all doses, flat | cell-cycle shift (explains ~18% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **4.40×** | +6.8 | 1e-09 | 20/22 (HOP62, SW 900, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **4.37×** | +6.7 | 1e-09 | 2/10 (HS-578T, SNU-423) | all doses, flat | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **4.23×** | +6.6 | 3e-09 | 16/22 (A-172, A498, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **3.32×** | +5.5 | 2e-06 | 15/20 (HOP62, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **9.93×** | +5.5 | 2e-06 | 16/19 (NCI-H2347, Panc 03.27, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~14% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **3.04×** | +4.9 | 5e-05 | 1/8 (HS-578T) | all doses, flat | composition shift |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **6.41×** | +4.4 | 4e-04 | 4/7 (HOP62, SW 900, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **2.51×** | +4.2 | 0.001 | 15/20 (SW 900, HOP62, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **5.70×** | +4.2 | 0.001 | 11/18 (HS-578T, NCI-H2347, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.76×** | +3.7 | 0.008 | 6/22 (Panc 03.27, NCI-H1792, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Vilanterol (drug)]] 5 µM |  | **1.74×** | +3.6 | 0.010 | 6/21 (HOP62, A-172, …) | all doses, stronger at high dose | position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **2.17×** | +3.5 | 0.012 | 12/21 (A-172, A498, …) | all doses, stronger at high dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **2.22×** | +3.5 | 0.013 | 13/20 (NCI-H1792, SNU-423, …) | top dose only |  |
| [[Vilanterol (drug)]] 0.5 µM |  | **2.07×** | +3.3 | 0.023 | 5/20 (NCI-H1792, SW 900, …) | all doses, stronger at high dose | position effect removed |
| [[Cytarabine (hydrochloride) (drug)]] 5 µM |  | **2.11×** | +3.3 | 0.027 | 10/20 (HS-578T, SNU-423, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.97×** | +3.1 | 0.049 | 7/20 (HS-578T, J82, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.59×** | +3.0 | 0.064 | 3/19 (J82, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~5% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 1 with an alert ⚠. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8941.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.408×** | -4.1 | 0.025 | 16/22 (A498, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.424×** | -3.9 | 0.027 | 10/21 (H4, SW 900, …) | all doses, flat |  |
| [[Trametinib (drug)]] 5 µM |  | **0.429×** | -3.8 | 0.027 | 14/22 (SW 900, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~20% here); noisy plate (z scaled) |
| [[Budesonide (drug)]] 5 µM |  | **0.444×** | -3.7 | 0.027 | 12/22 (NCI-H1792, H4, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.504×** | -3.7 | 0.027 | 13/21 (SW 900, NCI-H1792, …) | all doses, flat | noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.454×** | -3.6 | 0.030 | 13/20 (NCI-H1792, H4, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.05 µM |  | **0.575×** | -3.5 | 0.034 | 10/21 (SW 900, J82, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.468×** | -3.5 | 0.034 | 15/20 (NCI-H1792, SW 900, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.468×** | -3.5 | 0.034 | 15/21 (A498, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Binimetinib (drug)]] 0.05 µM |  | **0.582×** | -3.4 | 0.040 | 11/22 (NCI-H2347, SW 900, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.568×** | -3.2 | 0.071 | 11/21 (SW 900, NCI-H2347, …) | all doses, flat | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **0.504×** | -3.1 | 0.084 | 11/22 (SW 900, HOP62, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **0.828×** | -3.1 | 0.091 | 3/22 (NCI-H1792, HOP62, …) | inconsistent across doses |  |
| [[Omeprazole (drug)]] 5 µM |  | **0.513×** | -3.0 | 0.092 | 8/22 (RPMI-7951, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Berbamine (dihydrochloride) (drug)]] 5 µM |  | **0.501×** | -3.0 | 0.092 | 8/20 (NCI-H2030, NCI-H2347, …) | rises with dose | plate-row cell shift |
| [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | **0.519×** | -3.0 | 0.098 | 13/20 (H4, A549, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.22 per unit of S-phase module lfc, +0.73 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8941. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 20.6 | 5 (3 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 72.5× (z +10.7) | — |
| [[NCI-H1792 (line)]] | alt | 11.8 | 1 | 4 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 34.1× (z +9.0) | [[Clobetasol propionate (drug)]] 0.05 µM 0.0121× (z -11.8) |
| [[A-172 (line)]] | wt | 3.48 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 80.8× (z +12.3) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 149× (z +9.9) | — |
| [[H4 (line)]] | wt | 10.5 | 0 | 3 | — | [[Budesonide (drug)]] 0.5 µM 0.0188× (z -9.5) |
| [[A498 (line)]] | wt | 32.0 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.0455× (z -9.5) |
| [[AsPC-1 (line)]] | alt | 1.44 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 26.3× (z +8.8) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[CFPAC-1 (line)]] | alt | 15.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 55.0× (z +13.8) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[NCI-H2347 (line)]] | alt | 21.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.95× (z +10.0) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[Panc 03.27 (line)]] | alt | 6.16 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 43.1× (z +12.8) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[SNU-423 (line)]] | alt | 3.13 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 40.2× (z +10.5) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[SW 900 (line)]] | alt | 50.6 | 0 | 1 | — | [[Cobimetinib (drug)]] 0.5 µM 0.0738× (z -8.7) |
| [[A-427 (line)]] | wt | 0.334 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 2.55 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.803 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.407 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.448 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.436 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.616 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.895 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.582 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.38 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.08 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.33 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 4.73 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.40 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.56 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.83 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.409 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.765 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.558 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.534 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.642 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.01 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 3.99 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.48 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.380 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.667 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 4.37 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.509 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.511 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.456 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.94 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.412 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.16 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.516 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.46 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.03 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.542 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.05 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8941), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MIR3142HG]] | +0.75 | +0.80 / +0.67 | both halves | 7e-06 | **novel candidate** |
| [[TRAF1]] | +0.75 | +0.73 / +0.72 | both halves | 7e-06 | pathway: HALLMARK_IL2_STAT5_SIGNALING |
| [[IL1A]] | +0.74 | +0.67 / +0.77 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB; STRING 997 |
| [[MIR155HG]] | +0.74 | +0.74 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[CXCL8]] | +0.71 | +0.68 / +0.74 | both halves | 7e-06 | pathway: Interleukin-10 signaling; STRING 972 |
| [[LINC00973]] | +0.71 | +0.65 / +0.70 | both halves | 7e-06 |  |
| [[ROR1-AS1]] | +0.68 | +0.71 / +0.63 | both halves | 7e-06 |  |
| [[PLAU]] | +0.67 | +0.62 / +0.68 | both halves | 7e-06 | pathway: HALLMARK_KRAS_SIGNALING_UP; STRING 446 |
| [[LIF]] | +0.67 | +0.63 / +0.65 | both halves | 7e-06 | pathway: HALLMARK_IL2_STAT5_SIGNALING; STRING 780 |
| [[G0S2]] | +0.66 | +0.68 / +0.66 | both halves | 7e-06 | pathway: HALLMARK_KRAS_SIGNALING_UP |
| [[ADORA2A]] | +0.63 | +0.61 / +0.57 | both halves | 9e-06 |  |
| [[TNFRSF9]] | +0.62 | +0.54 / +0.62 | both halves | 1e-05 | pathway: HALLMARK_IL2_STAT5_SIGNALING; STRING 681 |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NPR3]] | -0.53 | -0.49 / -0.56 | both halves | 2e-05 |  |
| [[LOX]] | -0.50 | -0.45 / -0.48 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*25 arrows, 25 of them with an alert ⚠; grade A 0, B 4, C 21. Shown: the 12 strongest; 13 more arrows (13 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CXCL3]] | B | CXCL3 activity raises CSF2's level | lines that do not express CXCL3 (14) vs lines expressing it (36) | 2.73× lower at baseline in the lines without CXCL3 | 0.018 | ⚠ within organs, on part of the lines; also absent: MGLL, SPTLC3, PCED1B |
| [[CD82]] | B | CD82 activity raises CSF2's level | lines that do not express CD82 (11) vs lines expressing it (39) | 2.62× lower at baseline in the lines without CD82 | 0.050 | ⚠ within organs, on part of the lines; also absent: ITGA3, GBP3, CXCL3; maybe low, not absent |
| [[DUSP10]] | B | DUSP10 activity raises CSF2's level | lines that do not express DUSP10 (11) vs lines expressing it (39) | 2.57× lower at baseline in the lines without DUSP10 | 0.084 | ⚠ within organs, on part of the lines; also absent: GLRX, GBP2, TMEM92-AS1; maybe low, not absent |
| [[SOX9]] | B | SOX9 activity raises CSF2's level | lines that do not express SOX9 (8) vs lines expressing it (42) | 2.44× lower at baseline in the lines without SOX9 | 0.096 | ⚠ within organs, on part of the lines; also absent: CXCL3, SMOX, TRIM38 |
| [[G0S2]] | C | G0S2 activity raises CSF2's level | lines that do not express G0S2 (33) vs lines expressing it (17) | 3.99× lower at baseline in the lines without G0S2 | 0.002 | ⚠ within organs, on part of the lines; also absent: IL6, EDNRA, RRAD; co-absent with the target |
| [[EVA1A]] | C | EVA1A activity raises CSF2's level | lines that do not express EVA1A (21) vs lines expressing it (29) | 2.94× lower at baseline in the lines without EVA1A | 0.003 | ⚠ within organs, on part of the lines; also absent: NLRP1, MILR1, SNAI2; co-absent with the target |
| [[RRAD]] | C | RRAD activity raises CSF2's level | lines that do not express RRAD (31) vs lines expressing it (19) | 3.16× lower at baseline in the lines without RRAD | 0.003 | ⚠ within organs, on part of the lines; also absent: LOX, IL6, EDNRA; co-absent with the target |
| [[IL6]] | C | IL6 activity raises CSF2's level | lines that do not express IL6 (32) vs lines expressing it (18) | 4.54× lower at baseline in the lines without IL6 | 0.003 | ⚠ within organs, on part of the lines; also absent: ENSG00000232949, STEAP1B-AS1, G0S2; co-absent with the target |
| [[MIR3142HG]] | C | MIR3142HG activity raises CSF2's level | lines that do not express MIR3142HG (26) vs lines expressing it (24) | 3.22× lower at baseline in the lines without MIR3142HG | 0.003 | ⚠ within organs, on part of the lines; also absent: CTHRC1, IL6, ENSG00000291130; co-absent with the target |
| [[LOX]] | C | LOX activity raises CSF2's level | lines that do not express LOX (31) vs lines expressing it (19) | 3.79× lower at baseline in the lines without LOX | 0.003 | ⚠ within organs, on part of the lines; also absent: C5orf46, RRAD, LINC01411; co-absent with the target |
| [[LINC00973]] | C | LINC00973 activity raises CSF2's level | lines that do not express LINC00973 (23) vs lines expressing it (27) | 3.05× lower at baseline in the lines without LINC00973 | 0.004 | ⚠ within organs, on part of the lines; also absent: ENSG00000239462, IL11, BICC1; co-absent with the target |
| [[SLC43A3]] | C | SLC43A3 activity raises CSF2's level | lines that do not express SLC43A3 (28) vs lines expressing it (22) | 2.64× lower at baseline in the lines without SLC43A3 | 0.008 | ⚠ within organs, on part of the lines; also absent: ENSG00000254979, FN1, ENSG00000234261; co-absent with the target |

### Downstream of this gene

*34 arrows, 34 of them with an alert ⚠; grade A 0, B 16, C 18. Shown: the 12 strongest; 22 more arrows (22 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CD82]] | B | CSF2 activity raises CD82's level | lines that do not express CSF2 (26) vs lines expressing it (24) | 3.56× lower at baseline in the lines without CSF2 | 0.002 | ⚠ within organs, on part of the lines; co-occurs with ARID1A; also absent: IL6, CCBE1, G0S2 |
| [[NFKBIE]] | B | CSF2 activity raises NFKBIE's level | lines that do not express CSF2 (26) vs lines expressing it (24) | 1.69× lower at baseline in the lines without CSF2 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with ARID1A; also absent: IL6, CCBE1, G0S2 |
| [[CXCL3]] | B | CSF2 activity raises CXCL3's level | lines that do not express CSF2 (26) vs lines expressing it (24) | 3.05× lower at baseline in the lines without CSF2 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with ARID1A; also absent: IL6, CCBE1, G0S2 |
| [[EHD1]] | B | CSF2 activity raises EHD1's level | lines that do not express CSF2 (26) vs lines expressing it (24) | 1.50× lower at baseline in the lines without CSF2 | 0.010 | ⚠ within organs, on part of the lines; co-occurs with ARID1A; also absent: IL6, CCBE1, G0S2 |
| [[IRAK2]] | B | CSF2 activity raises IRAK2's level | lines that do not express CSF2 (26) vs lines expressing it (24) | 2.94× lower at baseline in the lines without CSF2 | 0.013 | ⚠ within organs, on part of the lines; co-occurs with ARID1A; also absent: IL6, CCBE1, G0S2 |
| [[DUSP10]] | B | CSF2 activity raises DUSP10's level | lines that do not express CSF2 (26) vs lines expressing it (24) | 2.72× lower at baseline in the lines without CSF2 | 0.013 | ⚠ within organs, on part of the lines; co-occurs with ARID1A; also absent: IL6, CCBE1, G0S2 |
| [[NINJ1]] | B | CSF2 activity raises NINJ1's level | lines that do not express CSF2 (26) vs lines expressing it (24) | 2.26× lower at baseline in the lines without CSF2 | 0.015 | ⚠ within organs, on part of the lines; co-occurs with ARID1A; also absent: IL6, CCBE1, G0S2 |
| [[B4GALT6]] | B | CSF2 activity lowers B4GALT6's level | lines that do not express CSF2 (26) vs lines expressing it (24) | 1.50× higher at baseline in the lines without CSF2 | 0.023 | ⚠ within organs, on part of the lines; co-occurs with ARID1A; also absent: IL6, CCBE1, G0S2 |
| [[HBEGF]] | B | CSF2 activity raises HBEGF's level | lines that do not express CSF2 (26) vs lines expressing it (24) | 1.75× lower at baseline in the lines without CSF2 | 0.026 | ⚠ within organs, on part of the lines; co-occurs with ARID1A; also absent: IL6, CCBE1, G0S2 |
| [[LINC02605]] | B | CSF2 activity raises LINC02605's level | lines that do not express CSF2 (26) vs lines expressing it (24) | 2.47× lower at baseline in the lines without CSF2 | 0.040 | ⚠ within organs, on part of the lines; co-occurs with ARID1A; also absent: IL6, CCBE1, G0S2 |
| [[RNF215]] | B | CSF2 activity lowers RNF215's level | lines that do not express CSF2 (26) vs lines expressing it (24) | 1.53× higher at baseline in the lines without CSF2 | 0.053 | ⚠ within organs, on part of the lines; co-occurs with ARID1A; also absent: IL6, CCBE1, G0S2 |
| [[GEM]] | B | CSF2 activity raises GEM's level | lines that do not express CSF2 (26) vs lines expressing it (24) | 2.34× lower at baseline in the lines without CSF2 | 0.057 | ⚠ within organs, on part of the lines; co-occurs with ARID1A; also absent: IL6, CCBE1, G0S2 |

## Where it sits

- **Module**: [[Module 112]] — TNF-alpha signaling via NF-kB; 43 genes; every member is in the + arm (projection on the module's main direction 0.789). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (30.4, 1.6); signed map (41.6, 12.0). **Vector** length 77.8, 26.9% of its response variance represented; |z| ≥ 3 in 691 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *inflammatory response* (hallmark, mean cos +0.62 to 6); *Interleukin-4 and Interleukin-13 signaling* (reactome, mean cos +0.64 to 5).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +4.1 | +10.1 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +3.4 | +6.6 |
|  | [[Selinexor (drug)]] 5 µM |  | +3.0 | +3.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +2.9 | +8.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.4 | +3.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.0 | +1.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.7 | +3.5 |
|  | [[Amsacrine (drug)]] 5 µM |  | +1.4 | +1.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.2 | +1.5 |
| fall | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -3.0 | -1.2 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.6 | -2.9 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -2.3 | -2.2 |
|  | [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | -2.3 | -3.0 |
|  | [[Betamethasone dipropionate (drug)]] 0.05 µM |  | -2.3 | -3.0 |
|  | [[Budesonide (drug)]] 0.05 µM |  | -2.2 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | colony stimulating factor 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q31.1 — chr5:132,073,789-132,076,170 (+) |
| Ensembl biotype | protein_coding |
| Also known as | GM-CSF, GMCSF |
| Gene groups (HGNC) | Colony stimulating factors |
| Hallmark sets | IL6_JAK_STAT3_SIGNALING, KRAS_SIGNALING_UP, IL2_STAT5_SIGNALING, TNFA_SIGNALING_VIA_NFKB |
| Reactome | 11 pathways, smallest: RUNX1 regulates transcription of genes involved in differentiation of myeloid cells; Interleukin receptor SHC signaling; Interleukin-10 signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [P04141](https://www.uniprot.org/uniprotkb/P04141) (Granulocyte-macrophage colony-stimulating factor):

> Cytokine that stimulates the growth and differentiation of hematopoietic precursor cells from various lineages, including granulocytes, macrophages, eosinophils and erythrocytes.

**Summary**, from NCBI Gene [1437](https://www.ncbi.nlm.nih.gov/gene/1437):

> The protein encoded by this gene is a cytokine that controls the production, differentiation, and function of granulocytes and macrophages. The active form of the protein is found extracellularly as a homodimer. This gene has been localized to a cluster of related genes at chromosome region 5q31, which is known to be associated with interstitial deletions in the 5q- syndrome and acute myelogenous leukemia. Other genes in the cluster include those encoding interleukins 4, 5, and 13. This gene …

**Accessions** — [HGNC:2434](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2434) · Entrez [1437](https://www.ncbi.nlm.nih.gov/gene/1437) · UniProt [P04141](https://www.uniprot.org/uniprotkb/P04141) · Ensembl [ENSG00000164400](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164400)

## Data

Gene col 8941: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8941); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8941, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8941]; `tensor/DDL_lfc|DDL_z.npy` [8941]; `embed/gene_vectors.npy` [8941]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8941 or target_col == 8941). Every well: [[CSF2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CSF2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
