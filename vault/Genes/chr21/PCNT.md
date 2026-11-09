---
symbol: "PCNT"
type: "gene"
col: 8336
ensembl_id: "ENSG00000160299"
name: "pericentrin"
location: "21q22.3"
module: 22
arm: "+"
pooled_cpm: 81.36
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 21
n_dd_up_clean: 4
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/022"]
generated_by: "tahoemap"
---

# PCNT

*pericentrin* — 21q22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.69× (z +10.4, q 1e-22, up in 34 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.55× (z +9.0, q 3e-17, up in 35 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (5 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.650× (z -12.5, q 6e-33, down in 46 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GEN1]] (+0.65, fdr 1e-05), [[MCM7]] (+0.65, fdr 1e-05), [[SMC1A]] (+0.64, fdr 7e-06); moves opposite to [[MFSD9]] (-0.61, fdr 4e-05), [[PELO]] (-0.60, fdr 1e-05), [[SLIRP]] (-0.57, fdr 8e-05).
> It is in [[Module 022]], a single-armed module (G2/M checkpoint).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 8 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8336.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.69×** | +10.4 | 1e-22 | 34/44 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.60×** | +9.6 | 3e-19 | 35/49 (SW1417, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.55×** | +9.0 | 3e-17 | 35/48 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.36×** | +8.9 | 1e-16 | 31/48 (NCI-H2030, NCI-H2347, …) | rises with dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.33×** | +8.3 | 1e-14 | 30/49 (SW480, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.36×** | +6.0 | 1e-07 | 29/48 (NCI-H460, COLO 205, …) | top dose only | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **1.32×** | +5.7 | 1e-06 | 28/48 (SW480, NCI-H460, …) | all doses, flat |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **1.28×** | +5.1 | 2e-05 | 26/48 (NCI-H460, SW480, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **1.27×** | +5.0 | 4e-05 | 25/48 (NCI-H460, SW480, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.54×** | +4.6 | 2e-04 | 27/49 (PANC-1, C-33 A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~21% of this change | **1.23×** | +4.2 | 0.001 | 24/47 (SW480, NCI-H460, …) | all doses, flat |  |
| [[RMC-6236 (drug)]] 5 µM |  | **1.34×** | +3.1 | 0.085 | 13/48 (LOX-IMVI, J82, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8336.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.650×** | -12.5 | 6e-33 | 46/48 (NCI-H460, J82, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.596×** | -10.6 | 7e-24 | 45/49 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.723×** | -9.4 | 1e-18 | 33/48 (SK-MEL-2, HT-29, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Belinostat (drug)]] 5 µM |  | **0.688×** | -7.6 | 3e-12 | 37/48 (J82, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **0.692×** | -7.6 | 5e-12 | 38/48 (NCI-H460, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.698×** | -7.4 | 2e-11 | 36/48 (J82, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.700×** | -7.0 | 2e-10 | 35/47 (LOX-IMVI, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.745×** | -6.0 | 1e-07 | 36/48 (J82, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Abemaciclib (drug)]] 5 µM |  | **0.594×** | -5.6 | 1e-06 | 34/48 (NCI-H1792, HOP62, …) | rises with dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.762×** | -5.6 | 2e-06 | 34/48 (MIA PaCa-2, SW480, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.786×** | -4.9 | 4e-05 | 26/48 (J82, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **0.805×** | -4.4 | 4e-04 | 25/48 (J82, SW 1088, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.666×** | -4.4 | 6e-04 | 22/45 (A-427, H4, …) | inconsistent across doses | cell-cycle shift (explains ~18% here); noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.677×** | -4.2 | 0.001 | 21/48 (Hs 766T, HT-29, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[venetoclax (drug)]] 5 µM |  | **0.685×** | -4.0 | 0.002 | 28/48 (SHP-77, Hs 766T, …) | top dose only | noisy plate (z scaled) |
| [[Belzutifan (drug)]] 5 µM |  | **0.686×** | -4.0 | 0.002 | 22/47 (SW480, NCI-H2347, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.694×** | -3.9 | 0.003 | 22/48 (MIA PaCa-2, HEC-1-A, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.777×** | -3.7 | 0.007 | 19/48 (NCI-H1792, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.782×** | -3.6 | 0.009 | 19/48 (NCI-H2347, SK-MEL-2, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, +0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8336. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 88.4 | 7 (5 ⚠) | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.90× (z +13.9) | [[Tucidinostat (drug)]] 5 µM 0.638× (z -9.8) |
| [[NCI-H460 (line)]] | wt | 56.8 | 7 (6 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.53× (z +12.8) | [[Tucidinostat (drug)]] 5 µM 0.570× (z -10.9) |
| [[J82 (line)]] | alt | 95.7 | 1 (1 ⚠) | 5 | [[Homoharringtonine (drug)]] 5 µM 1.60× (z +8.9) ⚠ cell-cycle shift, explains ~37% of this change | [[Belinostat (drug)]] 5 µM 0.332× (z -14.8) |
| [[LS 180 (line)]] | wt | 85.2 | 4 (3 ⚠) | 2 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.79× (z +10.8) | [[Selinexor (drug)]] 5 µM 0.506× (z -10.1) ⚠ cell-cycle shift, explains ~23% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 0.541× (z -9.1) |
| [[NCI-H2347 (line)]] | alt | 54.4 | 3 (2 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.35× (z +14.9) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.36× (z +10.6) | [[Tucidinostat (drug)]] 0.5 µM 0.489× (z -8.8) |
| [[SW1417 (line)]] | alt | 84.8 | 3 (3 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.05 µM 2.73× (z +10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | [[Selinexor (drug)]] 5 µM 0.535× (z -10.3) ⚠ cell-cycle shift, explains ~23% of this change |
| [[A-427 (line)]] | wt | 107 | 0 | 3 (2 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.561× (z -10.3) |
| [[CFPAC-1 (line)]] | alt | 59.1 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.40× (z +12.8) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.56× (z +9.8) | — |
| [[COLO 205 (line)]] | alt | 43.7 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.33× (z +14.6) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 4.40× (z +10.4) | — |
| [[LOX-IMVI (line)]] | wt | 152 | 0 | 3 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.400× (z -10.8) ⚠ toxic · without an alert: [[Tucidinostat (drug)]] 5 µM 0.573× (z -9.7) |
| [[MIA PaCa-2 (line)]] | alt | 151 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.492× (z -12.1) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.428× (z -10.3) |
| [[NCI-H1792 (line)]] | alt | 58.6 | 1 (1 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 1.87× (z +8.9) ⚠ cell-cycle shift, explains ~37% of this change | [[Panobinostat (drug)]] 5 µM 0.365× (z -10.0) |
| [[RKO (line)]] | wt | 77.2 | 3 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.62× (z +12.5) | — |
| [[A498 (line)]] | wt | 100 | 0 | 2 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.588× (z -8.9) ⚠ cell-cycle shift, explains ~23% of this change |
| [[H4 (line)]] | wt | 118 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.308× (z -9.7) ⚠ toxic |
| [[HEC-1-A (line)]] | alt | 84.5 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.72× (z +9.1) | — |
| [[HOP62 (line)]] | alt | 119 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.21× (z +8.7) ⚠ toxic; transcription drop | [[Tucidinostat (drug)]] 0.5 µM 0.449× (z -9.2) |
| [[KATO III (line)]] | alt | 45.9 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.03× (z +9.3) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.69× (z +9.2) | — |
| [[NCI-H1573 (line)]] | alt | 71.9 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.76× (z +8.8) ⚠ cell-cycle shift, explains ~37% of this change | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.387× (z -9.9) ⚠ toxic |
| [[Panc 03.27 (line)]] | alt | 62.1 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.28× (z +12.4) | — |
| [[A-172 (line)]] | wt | 109 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.415× (z -9.5) ⚠ toxic |
| [[A549 (line)]] | wt | 50.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.23× (z +12.4) ⚠ cell-cycle shift, explains ~37% of this change | — |
| [[HCT15 (line)]] | alt | 188 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.37× (z +8.6) | — |
| [[Hs 766T (line)]] | wt | 49.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.99× (z +8.8) | — |
| [[HT-29 (line)]] | alt | 57.8 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.477× (z -10.6) ⚠ cell-cycle shift, explains ~23% of this change |
| [[LoVo (line)]] | wt | 79.2 | 0 | 1 | — | [[Tucidinostat (drug)]] 5 µM 0.600× (z -8.7) |
| [[NCI-H2030 (line)]] | alt | 107 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.65× (z +16.9) ⚠ cell-cycle shift, explains ~37% of this change | — |
| [[NCI-H23 (line)]] | alt | 87.1 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.595× (z -9.1) ⚠ cell-cycle shift, explains ~23% of this change |
| [[NCI-H661 (line)]] | alt | 85.7 | 0 | 1 | — | [[Brimonidine (drug)]] 0.5 µM 0.167× (z -8.6) |
| [[PANC-1 (line)]] | alt | 64.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 1.95× (z +9.2) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 94.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +11.3) ⚠ cell-cycle shift, explains ~37% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 75.4 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.483× (z -10.6) ⚠ cell-cycle shift, explains ~23% of this change |
| [[SNU-1 (line)]] | wt | 95.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.322× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[SNU-423 (line)]] | alt | 54.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.63× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[SW 1088 (line)]] | alt | 85.0 | 0 | 1 | — | [[Tazarotene (drug)]] 0.05 µM 0.0640× (z -9.4) |
| [[AN3 CA (line)]] | alt | 91.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 47.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 47.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 112 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 55.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 66.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 31.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 91.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 76.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 64.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 62.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 90.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 77.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 54.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 119 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8336), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*66 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GEN1]] | +0.65 | +0.57 / +0.67 | both halves | 1e-05 |  |
| [[MCM7]] | +0.65 | +0.50 / +0.68 | both halves | 1e-05 |  |
| [[SMC1A]] | +0.64 | +0.65 / +0.60 | both halves | 7e-06 | pathway: HALLMARK_MITOTIC_SPINDLE |
| [[SAE1]] | +0.63 | +0.58 / +0.60 | both halves | 8e-06 |  |
| [[PRC1]] | +0.63 | +0.57 / +0.66 | both halves | 1e-05 | pathway: HALLMARK_MITOTIC_SPINDLE |
| [[HNRNPUL1]] | +0.62 | +0.32 / +0.70 | both halves | 2e-04 |  |
| [[NEMP1]] | +0.62 | +0.47 / +0.65 | both halves | 2e-05 |  |
| [[CENPN]] | +0.61 | +0.56 / +0.64 | both halves | 1e-05 | pathway: Mitotic Prometaphase |
| [[FOXM1]] | +0.59 | +0.47 / +0.63 | both halves | 2e-05 | pathway: G2/M Transition |
| [[NUSAP1]] | +0.59 | +0.55 / +0.57 | both halves | 1e-05 | pathway: HALLMARK_MITOTIC_SPINDLE |
| [[TMPO]] | +0.59 | +0.47 / +0.62 | both halves | 2e-05 |  |
| [[SMC4]] | +0.59 | +0.60 / +0.58 | both halves | 7e-06 | pathway: HALLMARK_MITOTIC_SPINDLE |

## Genes that move opposite

*34 of its nearest partners move opposite, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MFSD9]] | -0.61 | -0.40 / -0.66 | both halves | 4e-05 |  |
| [[PELO]] | -0.60 | -0.52 / -0.51 | both halves | 1e-05 |  |
| [[SLIRP]] | -0.57 | -0.37 / -0.58 | both halves | 8e-05 |  |
| [[NDUFA12]] | -0.57 | -0.51 / -0.54 | both halves | 1e-05 |  |
| [[SCRN2]] | -0.57 | -0.39 / -0.57 | both halves | 5e-05 |  |
| [[FAM104A]] | -0.56 | -0.51 / -0.51 | both halves | 1e-05 |  |
| [[MRPL21]] | -0.56 | -0.36 / -0.60 | both halves | 1e-04 |  |
| [[LSM10]] | -0.56 | -0.33 / -0.56 | both halves | 1e-04 |  |
| [[RBIS]] | -0.56 | -0.37 / -0.59 | both halves | 7e-05 |  |
| [[GPR160]] | -0.55 | -0.46 / -0.53 | both halves | 2e-05 |  |
| [[MINCR]] | -0.55 | -0.40 / -0.54 | both halves | 5e-05 |  |
| [[NDUFB4]] | -0.55 | -0.34 / -0.59 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 022]] — G2/M checkpoint; 185 genes; every member is in the + arm (projection on the module's main direction 0.481). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-37.5, -41.9); signed map (-36.0, -48.6). **Vector** length 141, 43.5% of its response variance represented; |z| ≥ 3 in 1,277 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +8.7 | +10.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +8.3 | +9.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +6.7 | +9.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.6 | +8.3 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | +6.4 | +8.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.4 | -1.2 |
|  | [[Filgotinib (drug)]] 5 µM |  | +3.1 | +1.1 |
|  | [[Demeclocycline (drug)]] 5 µM |  | +3.0 | +2.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.9 | +2.8 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +2.7 | +4.6 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -10.5 | -12.5 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | -9.6 | -9.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -9.0 | -10.6 |
|  | [[Selinexor (drug)]] 0.5 µM |  | -7.0 | -7.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -4.9 | -7.0 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -4.6 | -5.6 |
|  | [[Belzutifan (drug)]] 5 µM |  | -4.4 | -4.0 |
|  | [[EX229 (drug)]] 5 µM |  | -4.0 | -1.2 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -3.6 | -3.9 |

## What is on record

|  |  |
|---|---|
| Name | pericentrin |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 21q22.3 — chr21:46,324,124-46,445,769 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KEN, KIAA0402, PCN, PCNTB, SCKL4; previously PCNT2 |
| Gene groups (HGNC) | Centriolar satellite proteins |
| Hallmark sets | MITOTIC_SPINDLE |
| Reactome | 23 pathways, smallest: Chaperone Mediated Autophagy; Late endosomal microautophagy; Aggrephagy |
| Matched by | ensembl_id |

**Function**, from UniProt [O95613](https://www.uniprot.org/uniprotkb/O95613) (Pericentrin):

> Integral component of the filamentous matrix of the centrosome involved in the initial establishment of organized microtubule arrays in both mitosis and meiosis. Plays a role, together with DISC1, in the microtubule network formation. Is an integral component of the pericentriolar material (PCM). May play an important role in preventing premature centrosome splitting during interphase by inhibiting NEK2 kinase activity at the centrosome.

**Summary**, from NCBI Gene [5116](https://www.ncbi.nlm.nih.gov/gene/5116):

> The protein encoded by this gene binds to calmodulin and is expressed in the centrosome. It is an integral component of the pericentriolar material (PCM). The protein contains a series of coiled-coil domains and a highly conserved PCM targeting motif called the PACT domain near its C-terminus. The protein interacts with the microtubule nucleation component gamma-tubulin and is likely important to normal functioning of the centrosomes, cytoskeleton, and cell-cycle progression. Mutations in this …

**Accessions** — [HGNC:16068](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16068) · Entrez [5116](https://www.ncbi.nlm.nih.gov/gene/5116) · UniProt [O95613](https://www.uniprot.org/uniprotkb/O95613) · Ensembl [ENSG00000160299](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000160299)

## Data

Gene col 8336: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8336); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8336, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8336]; `tensor/DDL_lfc|DDL_z.npy` [8336]; `embed/gene_vectors.npy` [8336]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8336 or target_col == 8336). Every well: [[PCNT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PCNT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
