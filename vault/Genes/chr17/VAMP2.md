---
symbol: "VAMP2"
type: "gene"
col: 13300
ensembl_id: "ENSG00000220205"
name: "vesicle associated membrane protein 2"
location: "17p13.1"
module: 59
arm: "+"
pooled_cpm: 32.62
n_lines_expressing: 50
n_dd_up: 23
n_dd_down: 9
n_dd_up_clean: 15
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/059"]
generated_by: "tahoemap"
---

# VAMP2

*vesicle associated membrane protein 2* — 17p13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (8 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 2.38× (z +9.7, q 2e-19, up in 40 of 47 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.74× (z +8.7, q 7e-16, up in 41 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.515× (z -7.4, q 8e-11, down in 40 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PNISR]] (+0.77, fdr 7e-06), [[RAB9A]] (+0.71, fdr 7e-06), [[LUC7L3]] (+0.67, fdr 7e-06); moves opposite to [[CCT6A]] (-0.66, fdr 7e-06), [[EIF2S1]] (-0.66, fdr 7e-06), [[BLTP2]] (-0.61, fdr 1e-05).
> It sits in the **+** arm of [[Module 059]] (Amino acids regulate mTORC1).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 8 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13300.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.38×** | +9.7 | 2e-19 | 40/47 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.74×** | +8.7 | 7e-16 | 41/48 (SNU-1, Hs 766T, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **1.69×** | +8.3 | 2e-14 | 37/47 (LoVo, KATO III, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.98×** | +7.6 | 3e-12 | 36/48 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.03×** | +7.6 | 3e-12 | 42/47 (SNU-1, SW 900, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.72×** | +6.1 | 1e-07 | 33/43 (NCI-H460, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.68×** | +5.4 | 7e-06 | 33/42 (LoVo, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.57×** | +5.0 | 4e-05 | 28/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.51×** | +4.6 | 2e-04 | 31/48 (SNU-1, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.05 µM |  | **1.50×** | +4.5 | 4e-04 | 30/48 (MIA PaCa-2, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.64×** | +4.0 | 0.004 | 27/47 (SW480, HEC-1-A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.42×** | +3.9 | 0.005 | 23/48 (C-33 A, LOX-IMVI, …) | top dose only |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.62×** | +3.8 | 0.005 | 23/46 (HEC-1-A, AsPC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.41×** | +3.7 | 0.008 | 19/37 (AsPC-1, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.59×** | +3.7 | 0.009 | 28/48 (HEC-1-A, SHP-77, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.37×** | +3.5 | 0.017 | 22/48 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~12% here); position effect removed |
| [[Celecoxib (drug)]] 0.5 µM |  | **1.54×** | +3.5 | 0.017 | 21/48 (PANC-1, SW480, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.36×** | +3.4 | 0.021 | 20/48 (LS 180, A-427, …) | inconsistent across doses | position effect removed |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | **1.53×** | +3.4 | 0.021 | 24/48 (BT-474, A498, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.33×** | +3.2 | 0.040 | 23/48 (SNU-1, A-427, …) | top dose only |  |
| [[Arbutin (drug)]] 5 µM |  | **1.31×** | +2.9 | 0.094 | 15/48 (A498, HT-29, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 6 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13300.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.515×** | -7.4 | 8e-11 | 40/48 (HT-29, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.546×** | -6.8 | 4e-09 | 43/48 (SNU-423, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.602×** | -5.7 | 3e-06 | 35/48 (LOX-IMVI, SW1417, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.734×** | -4.9 | 2e-04 | 26/48 (AN3 CA, Hs 766T, …) | top dose only |  |
| [[GSK1059615 (drug)]] 5 µM |  | **0.407×** | -4.2 | 0.002 | 33/47 (C-33 A, RPMI-7951, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.766×** | -4.2 | 0.002 | 31/48 (AN3 CA, MIA PaCa-2, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.442×** | -3.8 | 0.011 | 24/40 (NCI-H460, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~21% here); noisy plate (z scaled); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.708×** | -3.6 | 0.020 | 21/48 (NCI-H460, SW480, …) | inconsistent across doses | position effect removed |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.716×** | -3.5 | 0.028 | 23/47 (RPMI-7951, SW480, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~49% of this change | 0.763× | -3.0 | 0.15 | 16/48 (Hs 766T, NCI-H661, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.39 per unit of S-phase module lfc, +0.46 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13300. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 34.0 | 5 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 4.89× (z +12.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 4.15× (z +11.6) | — |
| [[LoVo (line)]] | wt | 20.7 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.62× (z +12.9) ⚠ cell-cycle shift, explains ~50% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 4.84× (z +11.2) | — |
| [[KATO III (line)]] | alt | 48.4 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.12× (z +12.2) ⚠ cell-cycle shift, explains ~50% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.37× (z +9.2) | — |
| [[LS 180 (line)]] | wt | 24.2 | 2 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 5.51× (z +10.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 5.27× (z +10.4) | — |
| [[SNU-1 (line)]] | wt | 45.1 | 2 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 4.87× (z +9.1) ⚠ toxic · without an alert: [[Selinexor (drug)]] 5 µM 2.75× (z +8.6) | — |
| [[SW480 (line)]] | alt | 41.0 | 2 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.46× (z +10.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.13× (z +9.2) | — |
| [[AN3 CA (line)]] | alt | 33.2 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.121× (z -11.6) ⚠ cell-cycle shift, explains ~33% of this change |
| [[BT-474 (line)]] | alt | 21.9 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.213× (z -8.9) ⚠ cell-cycle shift, explains ~16% of this change |
| [[HCT15 (line)]] | alt | 52.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.77× (z +9.7) ⚠ cell-cycle shift, explains ~50% of this change | — |
| [[Hs 766T (line)]] | wt | 49.7 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.402× (z -9.5) ⚠ cell-cycle shift, explains ~33% of this change |
| [[NCI-H1573 (line)]] | alt | 22.3 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 6.69× (z +9.6) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 10.5 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 7.09× (z +8.8) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 27.1 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.93× (z +9.1) ⚠ toxic; transcription drop | — |
| [[SW 1271 (line)]] | alt | 48.8 | 0 | 1 (1 ⚠) | — | [[Ivabradine (hydrochloride) (drug)]] 0.5 µM 0.0699× (z -9.0) ⚠ transcription drop; unreliable plate only |
| [[SW 900 (line)]] | alt | 70.7 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 3.46× (z +8.9) ⚠ toxic | — |
| [[SW1417 (line)]] | alt | 29.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.71× (z +9.7) ⚠ cell-cycle shift, explains ~50% of this change | — |
| [[A-172 (line)]] | wt | 48.6 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 33.3 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 40.2 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 37.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 38.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 23.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 26.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 22.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 35.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 20.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 43.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 28.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 35.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 36.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 30.9 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 39.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 35.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 38.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 34.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 38.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 45.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 31.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 38.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 38.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 29.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 29.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 39.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13300), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*70 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PNISR]] | +0.77 | +0.69 / +0.72 | both halves | 7e-06 |  |
| [[RAB9A]] | +0.71 | +0.66 / +0.69 | both halves | 7e-06 |  |
| [[LUC7L3]] | +0.67 | +0.60 / +0.62 | both halves | 7e-06 |  |
| [[SAT2]] | +0.67 | +0.61 / +0.70 | both halves | 7e-06 |  |
| [[XPA]] | +0.65 | +0.58 / +0.64 | both halves | 8e-06 |  |
| [[KMT2E]] | +0.65 | +0.57 / +0.61 | both halves | 1e-05 |  |
| [[PABPN1]] | +0.64 | +0.61 / +0.58 | both halves | 7e-06 |  |
| [[RCHY1]] | +0.63 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[ABCA5]] | +0.62 | +0.61 / +0.56 | both halves | 1e-05 |  |
| [[ZNF226]] | +0.62 | +0.56 / +0.62 | both halves | 1e-05 |  |
| [[SRSF11]] ⚠ | +0.62 | +0.56 / +0.54 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[SPACA9]] | +0.61 | +0.68 / +0.51 | both halves | 1e-05 |  |
| [[ZSCAN16-AS1]] | +0.61 | +0.54 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*30 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCT6A]] | -0.66 | -0.60 / -0.67 | both halves | 7e-06 |  |
| [[EIF2S1]] | -0.66 | -0.65 / -0.59 | both halves | 7e-06 |  |
| [[BLTP2]] | -0.61 | -0.65 / -0.50 | both halves | 1e-05 |  |
| [[TPM3]] | -0.58 | -0.58 / -0.51 | both halves | 1e-05 |  |
| [[ACLY]] | -0.58 | -0.46 / -0.59 | both halves | 2e-05 | pathway: Integration of energy metabolism |
| [[PRKDC]] | -0.57 | -0.56 / -0.56 | both halves | 1e-05 |  |
| [[NOLC1]] | -0.57 | -0.48 / -0.54 | both halves | 2e-05 |  |
| [[STIP1]] | -0.57 | -0.57 / -0.52 | both halves | 1e-05 |  |
| [[TUBG1]] | -0.57 | -0.56 / -0.45 | both halves | 3e-05 |  |
| [[TOMM40]] | -0.56 | -0.54 / -0.52 | both halves | 1e-05 | pathway: Protein localization |
| [[LRRC59]] | -0.56 | -0.53 / -0.54 | both halves | 1e-05 |  |
| [[CCT5]] | -0.56 | -0.59 / -0.52 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises VAMP2's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 059]] — Amino acids regulate mTORC1; 80 genes; this gene is in the **+** arm (projection on the module's main direction 0.684). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-20.6, -4.3); signed map (-7.4, 2.1). **Vector** length 109, 31.5% of its response variance represented; |z| ≥ 3 in 881 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +10.6 | +8.7 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +6.8 | +4.6 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | +5.6 | +8.3 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.9 | +9.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.8 | +7.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.0 | +0.5 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +3.4 | +3.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.4 | +4.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.8 | +1.7 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.8 | +3.8 |
| fall | [[PH-797804 (drug)]] 5 µM |  | -5.0 | -2.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.3 | -2.1 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~34% of this change | -3.7 | -3.6 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | -3.6 | -3.8 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -3.6 | -0.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.9 | +0.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.4 | -4.2 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.3 | -1.2 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.0 | -0.1 |

## What is on record

|  |  |
|---|---|
| Name | vesicle associated membrane protein 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p13.1 — chr17:8,159,149-8,163,546 (-) |
| Ensembl biotype | protein_coding |
| Also known as | VAMP-2; previously SYB2 |
| Gene groups (HGNC) | Vesicle associated membrane proteins |
| Reactome | 36 pathways, smallest: Toxicity of botulinum toxin type D (botD); Toxicity of botulinum toxin type F (botF); Toxicity of botulinum toxin type G (botG) |
| Matched by | ensembl_id |

**Function**, from UniProt [P63027](https://www.uniprot.org/uniprotkb/P63027) (Vesicle-associated membrane protein 2):

> SNAREs (soluble N-ethylmaleimide-sensitive factor-attachment protein receptors) are essential proteins for intracellular membrane fusion. SNAREs localized on opposing membranes assemble to form a trans-SNARE complex, an extended, parallel four-helix bundle whose assembly releases energy that drives membrane fusion. The core SNARE complex typically consists of four alpha-helical domains, three from target membrane SNAREs (t-SNAREs) and one from a vesicle SNARE (v-SNARE). VAMP2 is a v-SNARE …

**Summary**, from NCBI Gene [6844](https://www.ncbi.nlm.nih.gov/gene/6844):

> The protein encoded by this gene is a member of the vesicle-associated membrane protein (VAMP)/synaptobrevin family. Synaptobrevins/VAMPs, syntaxins, and the 25-kD synaptosomal-associated protein SNAP25 are the main components of a protein complex involved in the docking and/or fusion of synaptic vesicles with the presynaptic membrane. This gene is thought to participate in neurotransmitter release at a step between docking and fusion. The protein forms a stable complex with syntaxin, …

**Accessions** — [HGNC:12643](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12643) · Entrez [6844](https://www.ncbi.nlm.nih.gov/gene/6844) · UniProt [P63027](https://www.uniprot.org/uniprotkb/P63027) · Ensembl [ENSG00000220205](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000220205)

## Data

Gene col 13300: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13300); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13300, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13300]; `tensor/DDL_lfc|DDL_z.npy` [13300]; `embed/gene_vectors.npy` [13300]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13300 or target_col == 13300). Every well: [[VAMP2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/VAMP2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
