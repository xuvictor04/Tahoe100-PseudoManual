---
symbol: "PPT2"
type: "gene"
col: 13327
ensembl_id: "ENSG00000221988"
name: "palmitoyl-protein thioesterase 2"
location: "6p21.32"
module: 30
arm: "+"
pooled_cpm: 6.52
n_lines_expressing: 49
n_dd_up: 15
n_dd_down: 20
n_dd_up_clean: 8
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/030"]
generated_by: "tahoemap"
---

# PPT2

*palmitoyl-protein thioesterase 2* — 6p21.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.20× (z +11.4, q 2e-27, up in 10 of 12 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.38× (z +6.9, q 1e-09, up in 18 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.408× (z -19.0, q 0e+00, down in 32 of 41 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KLHDC3]] (+0.67, fdr 7e-06), [[CNPY3]] (+0.66, fdr 1e-05), [[ENTREP3]] (+0.66, fdr 1e-05); moves opposite to [[NOTCH2NLB]] (-0.71, fdr 7e-06), [[NEPRO-AS1]] (-0.66, fdr 3e-05), [[NSRP1]] (-0.60, fdr 4e-05).
> It sits in the **+** arm of [[Module 030]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[LACC1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 7 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13327.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.20×** | +11.4 | 2e-27 | 10/12 (J82, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.93×** | +9.9 | 9e-21 | 17/26 (NCI-H460, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.38×** | +6.9 | 1e-09 | 18/47 (HOP62, LOX-IMVI, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.53×** | +5.3 | 2e-05 | 8/19 (J82, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.48×** | +4.3 | 0.002 | 5/37 (Hs 766T, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.73×** | +3.8 | 0.014 | 1/16 (NCI-H2030) | rises with dose | noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.40×** | +3.6 | 0.023 | 5/39 (HEC-1-A, Hs 766T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.26×** | +3.5 | 0.036 | 8/41 (A-427, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.26×** | +3.4 | 0.040 | 6/31 (A-427, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Vilanterol (drug)]] 0.5 µM |  | **1.25×** | +3.4 | 0.040 | 1/42 (SW480) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.25×** | +3.3 | 0.045 | 11/33 (J82, NCI-H23, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[Ritonavir (drug)]] 0.5 µM |  | **1.24×** | +3.3 | 0.045 | 6/42 (LOX-IMVI, HT-29, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~8% of this change | **1.24×** | +3.1 | 0.082 | 9/44 (J82, A-172, …) | top dose only |  |
| [[OTS514 (drug)]] 5 µM |  | **1.56×** | +3.1 | 0.082 | 2/28 (MIA PaCa-2, NCI-H1792) | top dose only | noisy plate (z scaled); position effect removed |
| [[ULK-101 (drug)]] 0.5 µM |  | **1.32×** | +3.0 | 0.098 | 2/42 (A-427, H4) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 5 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13327.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.408×** | -19.0 | 0e+00 | 32/41 (NCI-H2030, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.351×** | -15.7 | 0e+00 | 33/42 (HS-578T, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.479×** | -10.6 | 4e-24 | 27/45 (AsPC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.554×** | -8.9 | 1e-16 | 26/45 (NCI-H460, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.651×** | -6.4 | 2e-08 | 20/46 (NCI-H460, A498, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.489×** | -4.9 | 8e-05 | 12/44 (HS-578T, SW 900, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~1% here); composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~13% of this change | **0.807×** | -4.5 | 5e-04 | 17/42 (Hs 766T, SHP-77, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.769×** | -3.9 | 0.006 | 13/46 (SW1417, SW 900, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.770×** | -3.9 | 0.006 | 16/46 (LoVo, SW480, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.783×** | -3.7 | 0.014 | 11/46 (RKO, LS 180, …) | rises with dose | cell-cycle shift (explains ~5% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.790×** | -3.5 | 0.021 | 9/46 (SW 1088, RKO, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~13% of this change | **0.792×** | -3.5 | 0.022 | 13/40 (HS-578T, H4, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.603×** | -3.5 | 0.022 | 5/40 (SW480, RPMI-7951, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.797×** | -3.4 | 0.029 | 7/46 (LoVo, SW1417, …) | rises with dose |  |
| [[Bergenin (drug)]] 0.5 µM |  | **0.812×** | -3.1 | 0.069 | 7/42 (HepG2/C3A, C-33 A, …) | inconsistent across doses | position effect removed |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.804×** | -3.1 | 0.069 | 10/46 (BT-474, C-33 A, …) | inconsistent across doses |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.819×** | -3.0 | 0.085 | 9/46 (NCI-H2030, H4, …) | top dose only |  |
| [[Darinaparsin (drug)]] 0.05 µM |  | **0.819×** | -3.0 | 0.085 | 6/46 (SW 900, H4, …) | inconsistent across doses |  |
| [[Belzutifan (drug)]] 5 µM |  | **0.654×** | -2.9 | 0.099 | 7/33 (NCI-H460, AsPC-1, …) | top dose only | noisy plate (z scaled); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13327. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 6.00 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.123× (z -16.3) |
| [[AsPC-1 (line)]] | alt | 4.75 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.146× (z -9.9) |
| [[Hs 766T (line)]] | wt | 10.5 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.199× (z -11.4) ⚠ cell-cycle shift, explains ~13% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.266× (z -9.4) |
| [[HS-578T (line)]] | alt | 7.59 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0553× (z -13.2) |
| [[NCI-H2030 (line)]] | alt | 21.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.134× (z -21.6) |
| [[SW 900 (line)]] | alt | 6.44 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0575× (z -10.7) |
| [[LoVo (line)]] | wt | 7.52 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0564× (z -21.2) |
| [[LOX-IMVI (line)]] | wt | 6.52 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.103× (z -14.8) |
| [[NCI-H2347 (line)]] | alt | 4.90 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.152× (z -8.7) |
| [[PANC-1 (line)]] | alt | 4.93 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.277× (z -9.8) |
| [[RKO (line)]] | wt | 10.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0823× (z -11.5) |
| [[A-172 (line)]] | wt | 2.53 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 8.64 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 5.16 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.26 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 9.55 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.70 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 8.38 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.38 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.97 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.38 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.98 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.40 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.69 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.53 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.59 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.47 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.92 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.98 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.10 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.65 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 8.90 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.62 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 7.15 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.82 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 8.10 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.26 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.36 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 8.74 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.53 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 8.77 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.12 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.76 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.14 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.46 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 6.01 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13327), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*69 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KLHDC3]] | +0.67 | +0.67 / +0.62 | both halves | 7e-06 |  |
| [[CNPY3]] | +0.66 | +0.72 / +0.54 | both halves | 1e-05 |  |
| [[ENTREP3]] | +0.66 | +0.67 / +0.56 | both halves | 1e-05 |  |
| [[LAPTM4A]] | +0.65 | +0.66 / +0.55 | both halves | 1e-05 |  |
| [[TM9SF2]] | +0.64 | +0.67 / +0.52 | both halves | 1e-05 |  |
| [[PIK3R2]] | +0.62 | +0.69 / +0.47 | both halves | 2e-05 |  |
| [[SHQ1]] | +0.62 | +0.62 / +0.49 | both halves | 1e-05 |  |
| [[ADIPOR1]] | +0.62 | +0.58 / +0.60 | both halves | 7e-06 |  |
| [[IGSF8]] | +0.61 | +0.64 / +0.53 | both halves | 1e-05 |  |
| [[ATPAF2]] | +0.61 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[DHRS1]] | +0.60 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[MOGS]] | +0.60 | +0.65 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*31 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NOTCH2NLB]] | -0.71 | -0.63 / -0.61 | both halves | 7e-06 |  |
| [[NEPRO-AS1]] | -0.66 | -0.72 / -0.45 | both halves | 3e-05 |  |
| [[NSRP1]] | -0.60 | -0.66 / -0.42 | both halves | 4e-05 |  |
| [[ERCC6L2]] | -0.59 | -0.58 / -0.57 | both halves | 1e-05 |  |
| [[APLF]] | -0.59 | -0.65 / -0.44 | both halves | 3e-05 |  |
| [[KRCC1]] | -0.58 | -0.66 / -0.42 | both halves | 4e-05 |  |
| [[HELQ]] | -0.57 | -0.68 / -0.31 | both halves | 2e-04 |  |
| [[TRIP11]] | -0.57 | -0.65 / -0.35 | both halves | 1e-04 |  |
| [[DARS1]] | -0.56 | -0.63 / -0.38 | both halves | 6e-05 |  |
| [[LACC1]] | -0.56 | -0.67 / -0.36 | both halves | 9e-05 |  |
| [[SBF2-AS1]] | -0.56 | -0.66 / -0.26 | both halves | 4e-04 |  |
| [[NBPF10]] | -0.56 | -0.56 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LACC1]] | B | LACC1 activity lowers PPT2's level | lines that do not express LACC1 (6) vs lines expressing it (44) | 1.73× higher at baseline in the lines without LACC1 | 0.083 | ⚠ within organs, on part of the lines; also absent: CCDC122, IL1RAP, NABP1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 030]]; 146 genes; this gene is in the **+** arm (projection on the module's main direction 0.564). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (-9.0, -20.0); signed map (-47.7, -8.7). **Vector** length 51.3, 6.52% of its response variance represented; |z| ≥ 3 in 801 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +3.1 | +6.9 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +2.4 | +3.4 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +2.3 | +3.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +1.5 | +0.5 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +1.4 | -1.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.3 | -0.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.1 | +4.3 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.0 | +0.6 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +0.9 | +2.7 |
|  | [[Brivudine (drug)]] 5 µM |  | +0.9 | -0.6 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -4.9 | -19.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.4 | -15.7 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -4.0 | -8.9 |
|  | [[Harringtonine (drug)]] 5 µM |  | -3.8 | -10.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.3 | -6.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.9 | -2.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.6 | -3.0 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.2 | -1.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.2 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | palmitoyl-protein thioesterase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p21.32 — chr6:32,153,441-32,163,678 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Thioester hydrolases |
| Reactome | 3 pathways, smallest: Fatty acyl-CoA biosynthesis; Fatty acid metabolism; Metabolism of lipids |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UMR5](https://www.uniprot.org/uniprotkb/Q9UMR5) (Lysosomal thioesterase PPT2):

> Catalyzes the cleavage of thioester bonds from S-palmitoyl-CoA or S-palmitoyl-N-acetylcysteamine (unbranched structures) but does not have activity against palmitoylcysteine or palmitoylated proteins, branched structures or bulky head groups. Conversely, hydrolyzes both long and short chain fatty acyl-CoA substrate.; [Isoform 2]: Catalytically inactive due to lack of active site His-283.

**Summary**, from NCBI Gene [9374](https://www.ncbi.nlm.nih.gov/gene/9374):

> This gene encodes a member of the palmitoyl-protein thioesterase family. The encoded glycosylated lysosomal protein has palmitoyl-CoA hydrolase activity in vitro, but does not hydrolyze palmitate from cysteine residues in proteins. Alternative splicing results in multiple transcript variants. Read-through transcription also exists between this gene and the downstream EGFL8 (EGF-like-domain, multiple 8) gene. [provided by RefSeq, Feb 2011]

**Accessions** — [HGNC:9326](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9326) · Entrez [9374](https://www.ncbi.nlm.nih.gov/gene/9374) · UniProt [Q9UMR5](https://www.uniprot.org/uniprotkb/Q9UMR5) · Ensembl [ENSG00000221988](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000221988)

## Data

Gene col 13327: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13327); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13327, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13327]; `tensor/DDL_lfc|DDL_z.npy` [13327]; `embed/gene_vectors.npy` [13327]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13327 or target_col == 13327). Every well: [[PPT2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PPT2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
