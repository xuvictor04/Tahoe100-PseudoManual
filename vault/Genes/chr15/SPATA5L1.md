---
symbol: "SPATA5L1"
type: "gene"
col: 10158
ensembl_id: "ENSG00000171763"
name: "AAA ATPase AFG2B"
location: "15q21.1"
module: 198
arm: "+"
pooled_cpm: 18.55
n_lines_expressing: 50
n_dd_up: 25
n_dd_down: 13
n_dd_up_clean: 18
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/198"]
generated_by: "tahoemap"
---

# SPATA5L1

*AAA ATPase AFG2B* — 15q21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (7 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 4.12× (z +11.3, q 7e-27, up in 41 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.464× (z -11.7, q 5e-29, down in 28 of 39 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Filgotinib (drug)]] 5 µM: 0.719× (z -5.0, q 9e-05, down in 16 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RCHY1]] (+0.70, fdr 7e-06), [[MRPL39]] (+0.64, fdr 7e-06), [[MRPL44]] (+0.62, fdr 1e-05); moves opposite to [[SPTAN1]] (-0.59, fdr 2e-05), [[KPNA4]] (-0.56, fdr 4e-05), [[RNF123]] (-0.55, fdr 3e-05).
> It is in [[Module 198]], a single-armed module (Antigen processing: Ubiquitination & Proteasome degradation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 7 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10158.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **4.12×** | +11.3 | 7e-27 | 41/48 (A-172, NCI-H1573, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.91×** | +9.9 | 1e-20 | 32/46 (A-172, HOP62, …) | two highest doses | cell-cycle shift (explains ~3% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.89×** | +9.4 | 1e-18 | 34/43 (NCI-H2030, NCI-H460, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.77×** | +8.1 | 6e-14 | 29/46 (SW480, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.43×** | +7.8 | 1e-12 | 27/46 (NCI-H2030, HS-578T, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.40×** | +7.2 | 4e-11 | 28/48 (HOP62, HEC-1-A, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.61×** | +7.0 | 2e-10 | 26/47 (LoVo, A-172, …) | rises with dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.54×** | +6.6 | 3e-09 | 26/46 (NCI-H1573, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~14% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.56×** | +6.5 | 6e-09 | 24/45 (LoVo, NCI-H460, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.51×** | +6.1 | 7e-08 | 27/46 (NCI-H23, A-427, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.32×** | +6.0 | 8e-08 | 22/47 (A-172, HOP62, …) | two highest doses | cell-cycle shift (explains ~16% here); composition shift |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.01×** | +5.6 | 1e-06 | 14/24 (NCI-H1573, SW480, …) | top dose only | noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.42×** | +5.1 | 1e-05 | 22/47 (HOP62, HS-578T, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.39×** | +5.0 | 2e-05 | 21/48 (PANC-1, LS 180, …) | all doses, flat | cell-cycle shift (explains ~17% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.35×** | +4.3 | 7e-04 | 15/48 (NCI-H460, PANC-1, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.32×** | +4.2 | 1e-03 | 18/48 (PANC-1, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~12% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.31×** | +4.1 | 0.002 | 17/46 (SW480, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~15% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.30×** | +4.0 | 0.002 | 18/48 (HEC-1-A, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.27×** | +3.7 | 0.007 | 15/48 (A-172, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Entecavir (monohydrate) (drug)]] 0.5 µM |  | **1.27×** | +3.7 | 0.007 | 8/48 (NCI-H1573, HOP62, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 3 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10158.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.464×** | -11.7 | 5e-29 | 28/39 (NCI-H460, NCI-H1573, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.606×** | -7.4 | 5e-11 | 20/30 (NCI-H1573, KATO III, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Filgotinib (drug)]] 5 µM |  | **0.719×** | -5.0 | 9e-05 | 16/48 (SW 1088, NCI-H1573, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 0.05 µM |  | **0.763×** | -4.1 | 0.005 | 17/48 (HOP62, NCI-H661, …) | inconsistent across doses |  |
| [[Mifepristone (drug)]] 0.5 µM |  | **0.783×** | -3.8 | 0.020 | 11/48 (NCI-H1573, SW1417, …) | inconsistent across doses |  |
| [[Apalutamide (drug)]] 0.5 µM |  | **0.793×** | -3.5 | 0.036 | 14/48 (HOP62, A549, …) | inconsistent across doses |  |
| [[Esmolol (hydrochloride) (drug)]] 5 µM |  | **0.795×** | -3.5 | 0.036 | 10/48 (HOP62, A-427, …) | top dose only |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.803×** | -3.4 | 0.054 | 8/48 (A498, HS-578T, …) | inconsistent across doses |  |
| [[Diphenhydramine (drug)]] 0.5 µM |  | **0.805×** | -3.3 | 0.055 | 7/48 (HOP62, J82, …) | inconsistent across doses |  |
| [[L-Eflornithine (monohydrochloride) (drug)]] 5 µM |  | **0.810×** | -3.2 | 0.068 | 7/48 (CFPAC-1, AsPC-1, …) | top dose only |  |
| [[Omeprazole (drug)]] 0.05 µM |  | **0.813×** | -3.2 | 0.078 | 6/48 (NCI-H1792, KATO III, …) | inconsistent across doses |  |
| [[Tirabrutinib (drug)]] 0.5 µM |  | **0.816×** | -3.1 | 0.083 | 12/48 (J82, LOX-IMVI, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~8% of this change | **0.817×** | -3.1 | 0.083 | 9/48 (CHP-212, NCI-H1573, …) | inconsistent across doses |  |
| [[Tofacitinib (drug)]] 5 µM |  | 0.869× | -3.0 | 0.093 | 9/48 (SNU-1, MIA PaCa-2, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.07 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10158. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 16.1 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.76× (z +11.2) | [[Dinaciclib (drug)]] 5 µM 0.141× (z -11.3) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 43.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.127× (z -12.9) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 27.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.235× (z -9.0) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 16.5 | 0 | 1 | — | [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.5 µM 0.0957× (z -8.7) |
| [[HCT15 (line)]] | alt | 15.0 | 0 | 1 | — | [[Saquinavir (drug)]] 0.5 µM 0.116× (z -9.4) |
| [[HOP62 (line)]] | alt | 18.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.44× (z +8.5) | — |
| [[KATO III (line)]] | alt | 19.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.185× (z -11.4) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 22.8 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 3.41× (z +9.5) ⚠ toxic | — |
| [[LS 180 (line)]] | wt | 17.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.207× (z -10.1) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 23.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.200× (z -9.1) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 26.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.268× (z -8.9) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 13.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.167× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 22.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.326× (z -9.8) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 19.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.261× (z -10.9) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 21.7 | 0 | 1 (1 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.145× (z -8.7) ⚠ toxic |
| [[SNU-423 (line)]] | alt | 14.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.179× (z -9.2) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 9.39 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 28.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 12.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 20.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 9.28 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 9.38 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 13.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 13.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 31.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 20.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 20.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 17.1 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 21.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10158), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RCHY1]] | +0.70 | +0.59 / +0.67 | both halves | 7e-06 |  |
| [[MRPL39]] | +0.64 | +0.59 / +0.62 | both halves | 7e-06 |  |
| [[MRPL44]] | +0.62 | +0.51 / +0.63 | both halves | 1e-05 |  |
| [[NUP54]] | +0.61 | +0.48 / +0.63 | both halves | 2e-05 |  |
| [[RWDD3]] | +0.61 | +0.48 / +0.59 | both halves | 2e-05 |  |
| [[ASB7]] | +0.60 | +0.46 / +0.66 | both halves | 2e-05 |  |
| [[VPS13B-DT]] | +0.60 | +0.56 / +0.55 | both halves | 1e-05 |  |
| [[TMEM68]] | +0.60 | +0.59 / +0.48 | both halves | 2e-05 |  |
| [[FBXO9]] | +0.59 | +0.58 / +0.48 | both halves | 2e-05 |  |
| [[MORN4]] | +0.59 | +0.43 / +0.61 | both halves | 3e-05 |  |
| [[MTX2]] | +0.59 | +0.56 / +0.59 | both halves | 1e-05 |  |
| [[SNRPA1]] | +0.58 | +0.52 / +0.60 | both halves | 1e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPTAN1]] | -0.59 | -0.48 / -0.52 | both halves | 2e-05 |  |
| [[KPNA4]] | -0.56 | -0.42 / -0.63 | both halves | 4e-05 |  |
| [[RNF123]] | -0.55 | -0.43 / -0.46 | both halves | 3e-05 |  |
| [[ZSWIM6]] | -0.55 | -0.55 / -0.54 | both halves | 1e-05 |  |
| [[DIAPH1]] | -0.54 | -0.44 / -0.50 | both halves | 3e-05 |  |
| [[UBR4]] | -0.54 | -0.48 / -0.57 | both halves | 2e-05 |  |
| [[SYAP1]] | -0.54 | -0.41 / -0.49 | both halves | 4e-05 |  |
| [[DNAJB1]] | -0.53 | -0.52 / -0.48 | both halves | 2e-05 |  |
| [[ERCC1]] | -0.53 | -0.47 / -0.51 | both halves | 2e-05 |  |
| [[EGR1]] | -0.52 | -0.41 / -0.48 | both halves | 4e-05 |  |
| [[ARC]] | -0.52 | -0.38 / -0.47 | both halves | 7e-05 |  |
| [[FOS]] | -0.52 | -0.48 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 198]] — Antigen processing: Ubiquitination & Proteasome degradation; 16 genes; every member is in the + arm (projection on the module's main direction 0.726). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.41; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-9.8, -1.3); signed map (-30.0, -13.4). **Vector** length 80.5, 15.8% of its response variance represented; |z| ≥ 3 in 905 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +4.6 | +7.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.4 | +9.4 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +3.3 | +4.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +3.2 | +6.1 |
|  | [[TAK-901 (drug)]] 5 µM |  | +3.0 | +11.3 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +2.9 | +3.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.9 | +2.2 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.5 | +2.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.2 | +8.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +1.8 | +1.0 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -6.2 | -11.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -6.1 | -7.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -3.3 | -0.5 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.9 | -0.2 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.8 | +0.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.6 | -0.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.2 | +1.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.0 | -1.2 |
|  | [[Filgotinib (drug)]] 5 µM |  | -1.9 | -5.0 |
|  | [[Apalutamide (drug)]] 0.5 µM |  | -1.8 | -3.5 |

## What is on record

|  |  |
|---|---|
| Name | AAA ATPase AFG2B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q21.1 — chr15:45,402,336-45,421,415 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC5347, FLJ12286; previously SPATA5L1 |
| Gene groups (HGNC) | AAA ATPases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BVQ7](https://www.uniprot.org/uniprotkb/Q9BVQ7) (ATPase family gene 2 protein homolog B):

> ATP-dependent chaperone part of the 55LCC heterohexameric ATPase complex which is chromatin-associated and promotes replisome proteostasis to maintain replication fork progression and genome stability. Required for replication fork progression, sister chromatid cohesion, and chromosome stability. The ATPase activity is specifically enhanced by replication fork DNA and is coupled to cysteine protease-dependent cleavage of replisome substrates in response to replication fork damage. Uses ATPase …

**Summary**, from NCBI Gene [79029](https://www.ncbi.nlm.nih.gov/gene/79029):

> Enables identical protein binding activity and preribosome binding activity. Involved in DNA replication; regulation of ribosome biogenesis; and ribosomal large subunit biogenesis. Located in cytoplasm; nucleus; and spindle. Implicated in autosomal recessive nonsyndromic deafness. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:28762](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28762) · Entrez [79029](https://www.ncbi.nlm.nih.gov/gene/79029) · UniProt [Q9BVQ7](https://www.uniprot.org/uniprotkb/Q9BVQ7) · Ensembl [ENSG00000171763](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000171763)

## Data

Gene col 10158: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10158); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10158, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10158]; `tensor/DDL_lfc|DDL_z.npy` [10158]; `embed/gene_vectors.npy` [10158]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10158 or target_col == 10158). Every well: [[SPATA5L1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SPATA5L1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
