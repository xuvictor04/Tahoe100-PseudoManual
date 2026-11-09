---
symbol: "MSL3"
type: "gene"
col: 78
ensembl_id: "ENSG00000005302"
name: "MSL complex subunit 3"
location: "Xp22.2"
module: 29
arm: "+"
pooled_cpm: 13.17
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 5
n_dd_up_clean: 11
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/029"]
generated_by: "tahoemap"
---

# MSL3

*MSL complex subunit 3* — Xp22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.12× (z +20.2, q 0e+00, up in 34 of 36 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.88× (z +15.8, q 0e+00, up in 40 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.671× (z -10.1, q 5e-21, down in 29 of 47 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CERS2]] (+0.68, fdr 7e-06), [[STRADB]] (+0.68, fdr 1e-05), [[ZNF514]] (+0.67, fdr 2e-05); moves opposite to [[PILRB]] (-0.62, fdr 1e-05), [[LRRC8E]] (-0.60, fdr 2e-05), [[ZNF10]] (-0.59, fdr 3e-05).
> It sits in the **+** arm of [[Module 029]] (Neutrophil degranulation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 78.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.12×** | +20.2 | 0e+00 | 34/36 (PANC-1, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.06×** | +19.1 | 0e+00 | 22/24 (NCI-H1792, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.88×** | +15.8 | 0e+00 | 40/44 (A-172, A498, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.59×** | +15.6 | 0e+00 | 27/29 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.64×** | +8.8 | 2e-16 | 29/46 (RKO, A-172, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.67×** | +8.8 | 2e-16 | 29/47 (SW480, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.57×** | +7.6 | 2e-12 | 21/45 (SW480, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.54×** | +7.4 | 1e-11 | 24/41 (NCI-H2030, KATO III, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.41×** | +6.1 | 6e-08 | 18/42 (HEC-1-A, Panc 03.27, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~16% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.27×** | +6.0 | 9e-08 | 20/48 (A-172, HEC-1-A, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **1.24×** | +5.3 | 7e-06 | 21/48 (NCI-H1792, SNU-423, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.34×** | +5.0 | 2e-05 | 17/41 (A-427, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.40×** | +4.2 | 1e-03 | 12/45 (NCI-H1792, HT-29, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.22×** | +3.5 | 0.020 | 11/46 (J82, LS 180, …) | top dose only | position effect removed |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.31×** | +3.4 | 0.025 | 6/43 (HEC-1-A, SNU-423, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Drospirenone (drug)]] 0.5 µM |  | **1.21×** | +3.3 | 0.029 | 6/45 (NCI-H1792, CFPAC-1, …) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.28×** | +3.1 | 0.056 | 4/44 (J82, NCI-H460, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | 1.20× | +3.1 | 0.066 | 9/46 (NCI-H23, C32, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.20×** | +3.0 | 0.081 | 10/44 (NCI-H1792, LoVo, …) | inconsistent across doses | low cells (technical?); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 2 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 78.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.671×** | -10.1 | 5e-21 | 29/47 (hTERT-HPNE, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.709×** | -6.1 | 2e-07 | 21/47 (SW48, HEC-1-A, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.778×** | -4.5 | 0.001 | 20/48 (A-427, SW480, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~8% of this change | **0.824×** | -3.5 | 0.073 | 9/45 (A-172, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Posaconazole (drug)]] 5 µM |  | **0.820×** | -3.4 | 0.073 | 6/47 (LS 180, NCI-H1792, …) | top dose only | plate-row cell shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.07 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 78. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 9.16 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.22× (z +10.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.355× (z -10.8) |
| [[SW480 (line)]] | alt | 20.6 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.72× (z +9.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.517× (z -9.1) |
| [[A-172 (line)]] | wt | 18.4 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.91× (z +11.2) | — |
| [[NCI-H1792 (line)]] | alt | 26.6 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.96× (z +11.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.28× (z +8.7) | — |
| [[HS-578T (line)]] | alt | 19.2 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.64× (z +8.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.349× (z -9.9) |
| [[KATO III (line)]] | alt | 13.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.92× (z +9.8) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 12.8 | 2 (2 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 4.09× (z +9.3) ⚠ toxic | — |
| [[Panc 03.27 (line)]] | alt | 16.7 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.89× (z +9.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.349× (z -8.8) |
| [[A498 (line)]] | wt | 12.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.36× (z +8.9) | — |
| [[AN3 CA (line)]] | alt | 17.2 | 0 | 1 | — | [[Canagliflozin (drug)]] 0.5 µM 0.0622× (z -8.7) |
| [[BT-474 (line)]] | alt | 19.2 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.220× (z -9.2) |
| [[HEC-1-A (line)]] | alt | 17.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.88× (z +8.5) ⚠ toxic; transcription drop | — |
| [[HepG2_C3A (line)]] | wt | 7.96 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.186× (z -8.7) |
| [[HOP62 (line)]] | alt | 9.47 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.22× (z +9.5) ⚠ toxic; transcription drop | — |
| [[hTERT-HPNE (line)]] | wt | 12.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.133× (z -12.8) |
| [[J82 (line)]] | alt | 18.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.381× (z -9.8) |
| [[LOX-IMVI (line)]] | wt | 7.57 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.281× (z -8.9) |
| [[MIA PaCa-2 (line)]] | alt | 15.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.43× (z +8.7) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 25.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.316× (z -11.0) |
| [[RPMI-7951 (line)]] | alt | 14.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.38× (z +8.9) | — |
| [[SNU-423 (line)]] | alt | 22.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.92× (z +9.5) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 12.8 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 12.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.16 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 7.77 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 9.51 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 12.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 8.73 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 14.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 19.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.37 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 4.56 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 9.66 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 8.91 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 8.97 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.25 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.69 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 11.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 78), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CERS2]] | +0.68 | +0.58 / +0.58 | both halves | 7e-06 |  |
| [[STRADB]] | +0.68 | +0.50 / +0.59 | both halves | 1e-05 |  |
| [[ZNF514]] | +0.67 | +0.48 / +0.58 | both halves | 2e-05 |  |
| [[SAP30L-AS1]] | +0.66 | +0.47 / +0.48 | both halves | 2e-05 |  |
| [[NIPBL-DT]] | +0.65 | +0.42 / +0.49 | both halves | 4e-05 |  |
| [[CTSZ]] | +0.64 | +0.50 / +0.65 | both halves | 1e-05 |  |
| [[BCL2L2]] | +0.63 | +0.55 / +0.54 | both halves | 1e-05 |  |
| [[NAXD]] | +0.62 | +0.47 / +0.54 | both halves | 2e-05 |  |
| [[C1D]] | +0.62 | +0.41 / +0.66 | both halves | 4e-05 |  |
| [[STMP1]] | +0.62 | +0.48 / +0.47 | both halves | 2e-05 |  |
| [[LDB1]] | +0.62 | +0.50 / +0.46 | both halves | 3e-05 |  |
| [[EMB]] | +0.61 | +0.56 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PILRB]] | -0.62 | -0.53 / -0.51 | both halves | 1e-05 |  |
| [[LRRC8E]] | -0.60 | -0.48 / -0.55 | both halves | 2e-05 |  |
| [[ZNF10]] | -0.59 | -0.57 / -0.44 | both halves | 3e-05 |  |
| [[MRPL14]] | -0.59 | -0.32 / -0.53 | both halves | 1e-04 |  |
| [[ASL]] | -0.57 | -0.58 / -0.32 | both halves | 2e-04 |  |
| [[TUBB2B]] | -0.57 | -0.41 / -0.48 | both halves | 4e-05 |  |
| [[TPST1]] | -0.54 | -0.47 / -0.40 | both halves | 5e-05 |  |
| [[CRTC1]] | -0.53 | -0.48 / -0.37 | both halves | 8e-05 |  |
| [[JUND]] | -0.53 | -0.43 / -0.46 | both halves | 3e-05 |  |
| [[KLHL26]] | -0.52 | -0.41 / -0.43 | both halves | 4e-05 |  |
| [[VPS37C]] | -0.52 | -0.35 / -0.45 | both halves | 1e-04 |  |
| [[TTC38]] | -0.52 | -0.36 / -0.36 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers MSL3's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.5% of all compounds | 0.026 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises MSL3's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 029]] — Neutrophil degranulation; 148 genes; this gene is in the **+** arm (projection on the module's main direction 0.588). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-4.9, 21.4); signed map (-18.2, -35.6). **Vector** length 72.2, 12.0% of its response variance represented; |z| ≥ 3 in 907 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.5 | +15.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.3 | +20.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +7.3 | +15.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.3 | +19.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +5.1 | +7.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.0 | +6.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.6 | +8.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.2 | +2.9 |
|  | [[Glycyrrhizic acid (drug)]] 0.5 µM |  | +1.3 | +1.2 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +1.3 | +1.0 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -4.6 | -10.1 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -4.0 | -2.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.5 | -2.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.3 | -6.1 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -2.2 | -4.5 |
|  | [[venetoclax (drug)]] 5 µM |  | -1.7 | -2.9 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.5 | -2.6 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.5 | -1.4 |
|  | [[EX229 (drug)]] 5 µM |  | -1.5 | -0.2 |
|  | [[EX229 (drug)]] 0.5 µM |  | -1.4 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | MSL complex subunit 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xp22.2 — chrX:11,758,159-11,775,772 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously MSL3L1 |
| Gene groups (HGNC) | MSL histone acetyltransferase complex |
| Reactome | 3 pathways, smallest: HATs acetylate histones; Chromatin modifying enzymes; Chromatin organization |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N5Y2](https://www.uniprot.org/uniprotkb/Q8N5Y2) (MSL complex subunit 3):

> Non-catalytic component of the MSL histone acetyltransferase complex, a multiprotein complex that mediates the majority of histone H4 acetylation at 'Lys-16' (H4K16ac), an epigenetic mark that prevents chromatin compaction. The MSL complex is required for chromosome stability and genome integrity by maintaining homeostatic levels of H4K16ac. The MSL complex is also involved in gene dosage by promoting up-regulation of genes expressed by the X chromosome (By similarity). X up-regulation is …

**Summary**, from NCBI Gene [10943](https://www.ncbi.nlm.nih.gov/gene/10943):

> This gene encodes a nuclear protein that is similar to the product of the Drosophila male-specific lethal-3 gene. The Drosophila protein plays a critical role in a dosage-compensation pathway, which equalizes X-linked gene expression in males and females. Thus, the human protein is thought to play a similar function in chromatin remodeling and transcriptional regulation, and it has been found as part of a complex that is responsible for histone H4 lysine-16 acetylation. This gene can undergo X …

**Accessions** — [HGNC:7370](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7370) · Entrez [10943](https://www.ncbi.nlm.nih.gov/gene/10943) · UniProt [Q8N5Y2](https://www.uniprot.org/uniprotkb/Q8N5Y2) · Ensembl [ENSG00000005302](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000005302)

## Data

Gene col 78: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 78); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 78, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 78]; `tensor/DDL_lfc|DDL_z.npy` [78]; `embed/gene_vectors.npy` [78]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 78 or target_col == 78). Every well: [[MSL3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MSL3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
