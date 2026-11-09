---
symbol: "LRIF1"
type: "gene"
col: 4307
ensembl_id: "ENSG00000121931"
name: "ligand dependent nuclear receptor interacting factor 1"
location: "1p13.3"
module: 38
arm: "+"
pooled_cpm: 54.64
n_lines_expressing: 45
n_dd_up: 18
n_dd_down: 12
n_dd_up_clean: 16
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 2
direction_downstream: 2
tags: ["gene", "module/038"]
generated_by: "tahoemap"
---

# LRIF1

*ligand dependent nuclear receptor interacting factor 1* — 1p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (2 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 2.81× (z +21.0, q 0e+00, up in 42 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.557× (z -11.5, q 1e-27, down in 28 of 38 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Belinostat (drug)]] 5 µM: 0.650× (z -8.8, q 3e-16, down in 32 of 43 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[C6orf62]] (+0.78, fdr 7e-06), [[ZNF546]] (+0.70, fdr 1e-05), [[ZNF432]] (+0.69, fdr 7e-06); moves opposite to [[PXMP4]] (-0.65, fdr 2e-05), [[NUDT21]] (-0.63, fdr 1e-05), [[NUP93]] (-0.61, fdr 1e-05).
> It is in [[Module 038]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[NPL]] → it (grade B ⚠); 2 go from it, the strongest it → [[CAVIN4]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 7 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4307.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **2.81×** | +21.0 | 0e+00 | 42/43 (HEC-1-A, LoVo, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.78×** | +16.6 | 0e+00 | 34/42 (NCI-H460, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.42×** | +10.1 | 1e-21 | 32/44 (AsPC-1, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.55×** | +8.9 | 8e-17 | 32/42 (NCI-H460, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.51×** | +7.9 | 3e-13 | 32/43 (LoVo, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~14% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.10× | +7.1 | 1e-10 | 0/44 | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.43×** | +7.0 | 2e-10 | 27/43 (NCI-H460, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.26×** | +6.6 | 3e-09 | 27/43 (SW1417, SW480, …) | all doses, stronger at high dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.36×** | +6.3 | 2e-08 | 28/43 (LoVo, SW 900, …) | rises with dose | position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.33×** | +5.8 | 3e-07 | 26/43 (LoVo, NCI-H2347, …) | two highest doses |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.31×** | +5.5 | 2e-06 | 25/44 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.30×** | +5.2 | 1e-05 | 22/43 (HS-578T, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.59×** | +4.9 | 4e-05 | 22/38 (LoVo, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~12% here); noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.27×** | +4.8 | 5e-05 | 21/43 (SK-MEL-2, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **1.25×** | +4.6 | 2e-04 | 20/42 (SW 900, NCI-H460, …) | top dose only |  |
| [[Infigratinib (drug)]] 5 µM |  | **1.53×** | +4.5 | 2e-04 | 20/43 (NCI-H23, NCI-H2030, …) | top dose only | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.16× | +4.2 | 1e-03 | 17/43 (NCI-H2030, NCI-H2347, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 11 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4307.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.557×** | -11.5 | 1e-27 | 28/38 (RPMI-7951, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.619×** | -9.8 | 4e-20 | 32/42 (NCI-H1792, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.650×** | -8.8 | 3e-16 | 32/43 (BT-474, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **0.691×** | -7.5 | 7e-12 | 30/44 (SNU-423, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.677×** | -7.3 | 2e-11 | 26/39 (A-427, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.728×** | -6.5 | 9e-09 | 22/43 (LoVo, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.732×** | -6.4 | 2e-08 | 26/43 (COLO 205, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Radotinib (drug)]] 5 µM |  | **0.820×** | -5.7 | 7e-07 | 18/43 (C32, BT-474, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **0.769×** | -5.4 | 5e-06 | 23/43 (SW480, NCI-H1792, …) | all doses, flat |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.773×** | -5.2 | 9e-06 | 22/43 (BT-474, A-172, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~30% of this change | **0.816×** | -4.0 | 0.004 | 20/42 (SNU-423, NCI-H1792, …) | inconsistent across doses |  |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.875× | -3.8 | 0.006 | 3/43 (J82, SK-MEL-2, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | 0.847× | -3.4 | 0.027 | 12/43 (COLO 205, BT-474, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~17% of this change | 0.847× | -3.4 | 0.027 | 15/43 (COLO 205, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | 0.848× | -3.4 | 0.027 | 13/42 (C32, NCI-H1573, …) | top dose only |  |
| [[Fusidic acid (drug)]] 5 µM |  | 0.893× | -3.3 | 0.039 | 4/43 (Hs 766T, Panc 03.27, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4307. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 49.2 | 6 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.40× (z +20.9) | [[Digitoxin (drug)]] 5 µM 0.437× (z -10.1) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 54.4 | 5 (1 ⚠) | 2 (1 ⚠) | [[Auranofin (drug)]] 5 µM 5.60× (z +17.7) | [[Digitoxin (drug)]] 5 µM 0.307× (z -12.1) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.362× (z -10.4) |
| [[MIA PaCa-2 (line)]] | alt | 108 | 4 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 3.73× (z +12.6) | [[Dinaciclib (drug)]] 5 µM 0.266× (z -12.3) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 75.5 | 2 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.29× (z +12.1) | [[Dinaciclib (drug)]] 5 µM 0.370× (z -9.9) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 110 | 0 | 5 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.210× (z -14.7) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.346× (z -10.0) |
| [[PANC-1 (line)]] | alt | 102 | 1 | 4 (4 ⚠) | [[Auranofin (drug)]] 5 µM 2.13× (z +8.8) | [[Digitoxin (drug)]] 5 µM 0.286× (z -14.5) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 131 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.53× (z +20.0) | [[Dinaciclib (drug)]] 5 µM 0.286× (z -13.5) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 60.5 | 3 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 3.51× (z +12.7) | [[Dinaciclib (drug)]] 5 µM 0.255× (z -13.3) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 60.6 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.172× (z -15.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[SW480 (line)]] | alt | 39.7 | 3 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 3.02× (z +12.7) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.430× (z -9.8) ⚠ cell-cycle shift, explains ~22% of this change |
| [[A-427 (line)]] | wt | 75.9 | 2 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 2.56× (z +9.8) | [[Dinaciclib (drug)]] 0.05 µM 0.141× (z -18.9) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 40.3 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.93× (z +12.6) | — |
| [[J82 (line)]] | alt | 60.8 | 1 | 2 (2 ⚠) | [[Auranofin (drug)]] 5 µM 2.35× (z +8.5) | [[Digitoxin (drug)]] 5 µM 0.367× (z -9.9) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 56.7 | 3 | 0 | [[Auranofin (drug)]] 5 µM 3.56× (z +12.9) | — |
| [[LS 180 (line)]] | wt | 63.4 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.99× (z +14.5) | — |
| [[A549 (line)]] | wt | 63.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.364× (z -10.1) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 67.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.75× (z +16.7) | — |
| [[BT-474 (line)]] | alt | 52.6 | 1 | 1 | [[Auranofin (drug)]] 5 µM 3.50× (z +10.9) | [[Belinostat (drug)]] 5 µM 0.367× (z -8.7) |
| [[C32 (line)]] | wt | 55.9 | 2 | 0 | [[Auranofin (drug)]] 5 µM 4.26× (z +11.6) | — |
| [[COLO 205 (line)]] | alt | 60.5 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.58× (z +11.3) | [[Panobinostat (drug)]] 5 µM 0.299× (z -10.3) |
| [[NCI-H2030 (line)]] | alt | 19.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.69× (z +15.0) | — |
| [[NCI-H2347 (line)]] | alt | 29.0 | 2 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 3.76× (z +10.4) | — |
| [[RPMI-7951 (line)]] | alt | 89.6 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.94× (z +8.8) | [[Dinaciclib (drug)]] 5 µM 0.0396× (z -29.4) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 53.6 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 4.14× (z +12.9) | [[Dinaciclib (drug)]] 5 µM 0.170× (z -15.5) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 62.1 | 1 | 0 | [[Auranofin (drug)]] 5 µM 4.15× (z +15.1) | — |
| [[A498 (line)]] | wt | 32.6 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.96× (z +9.5) | — |
| [[CFPAC-1 (line)]] | alt | 95.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.12× (z +11.7) | — |
| [[CHP-212 (line)]] | wt | 40.2 | 0 | 1 | — | [[Pimozide (drug)]] 0.05 µM 0.0960× (z -9.9) |
| [[HCT15 (line)]] | alt | 44.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0909× (z -14.8) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 51.9 | 1 | 0 | [[Auranofin (drug)]] 5 µM 5.19× (z +17.7) | — |
| [[Hs 766T (line)]] | wt | 32.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.70× (z +11.1) | — |
| [[HT-29 (line)]] | alt | 55.6 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.63× (z +11.8) | — |
| [[hTERT-HPNE (line)]] | wt | 38.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.276× (z -9.1) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 76.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.73× (z +13.0) | — |
| [[SW1417 (line)]] | alt | 37.2 | 1 | 0 | [[Auranofin (drug)]] 5 µM 4.13× (z +12.6) | — |
| [[SW48 (line)]] | wt | 28.6 | 0 | 1 | — | [[Topotecan (hydrochloride) (drug)]] 0.05 µM 0.0688× (z -12.6) |
| [[AN3 CA (line)]] | alt | 32.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 28.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.54 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 65.5 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 9.33 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 4.07 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 71.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 50.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 46.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 41.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.58 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 4.91 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 48.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 53.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4307), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C6orf62]] | +0.78 | +0.82 / +0.59 | both halves | 7e-06 |  |
| [[ZNF546]] | +0.70 | +0.71 / +0.52 | both halves | 1e-05 |  |
| [[ZNF432]] | +0.69 | +0.63 / +0.67 | both halves | 7e-06 |  |
| [[GCNA]] | +0.68 | +0.68 / +0.53 | both halves | 1e-05 |  |
| [[EIF5]] | +0.67 | +0.63 / +0.45 | both halves | 3e-05 |  |
| [[UBE2D3-AS1]] | +0.67 | +0.68 / +0.48 | both halves | 2e-05 |  |
| [[SLC22A1]] | +0.65 | +0.73 / +0.51 | both halves | 1e-05 |  |
| [[THUMPD3-AS1]] | +0.65 | +0.62 / +0.54 | both halves | 1e-05 |  |
| [[ZNF222]] | +0.64 | +0.69 / +0.56 | both halves | 1e-05 |  |
| [[PARD6G-AS1]] | +0.64 | +0.68 / +0.44 | both halves | 3e-05 |  |
| [[MYOCOS]] | +0.63 | +0.68 / +0.43 | both halves | 3e-05 |  |
| [[IDI2-AS1]] | +0.63 | +0.66 / +0.41 | both halves | 4e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PXMP4]] | -0.65 | -0.46 / -0.46 | both halves | 2e-05 |  |
| [[NUDT21]] | -0.63 | -0.57 / -0.58 | both halves | 1e-05 |  |
| [[NUP93]] | -0.61 | -0.50 / -0.57 | both halves | 1e-05 |  |
| [[TMEM245]] | -0.60 | -0.45 / -0.52 | both halves | 3e-05 |  |
| [[NOMO3]] | -0.58 | -0.50 / -0.48 | both halves | 2e-05 |  |
| [[MED14]] | -0.58 | -0.58 / -0.51 | both halves | 1e-05 |  |
| [[GUSB]] | -0.57 | -0.44 / -0.44 | both halves | 3e-05 |  |
| [[NHP2]] | -0.57 | -0.58 / -0.25 | both halves | 4e-04 |  |
| [[BRAT1]] | -0.57 | -0.58 / -0.31 | both halves | 2e-04 |  |
| [[SCAP]] | -0.57 | -0.43 / -0.54 | both halves | 3e-05 |  |
| [[POLD2]] | -0.56 | -0.51 / -0.36 | both halves | 1e-04 |  |
| [[RPA1]] | -0.56 | -0.57 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NPL]] | B | NPL activity raises LRIF1's level | lines that do not express NPL (7) vs lines expressing it (43) | 2.57× lower at baseline in the lines without NPL | 0.060 | ⚠ within organs, on part of the lines; also absent: IQCJ-SCHIP1, NPR2, CAPS2; maybe low, not absent; its own permutation p |
| [[TOP2A]] | B | TOP2A activity lowers LRIF1's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.4% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CAVIN4]] | B | LRIF1 activity raises CAVIN4's level | lines that do not express LRIF1 (5) vs lines expressing it (45) | 1.03× lower at baseline in the lines without LRIF1 | 0.077 | ⚠ within organs, on part of the lines; co-absent genes; also absent: RAP1GAP2, PPFIA4, AP1S3 |
| [[MSANTD3-TMEFF1]] | B | LRIF1 activity lowers MSANTD3-TMEFF1's level | lines that do not express LRIF1 (5) vs lines expressing it (45) | 1.07× higher at baseline in the lines without LRIF1 | 0.090 | ⚠ within organs, on part of the lines; co-absent genes; also absent: RAP1GAP2, PPFIA4, AP1S3 |

## Where it sits

- **Module**: [[Module 038]]; 122 genes; every member is in the + arm (projection on the module's main direction 0.605). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (32.2, -21.2); signed map (10.3, 11.5). **Vector** length 124, 33.6% of its response variance represented; |z| ≥ 3 in 1,042 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +12.0 | +21.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.6 | +16.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.7 | +8.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.5 | +10.1 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +5.5 | +7.9 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +5.1 | +6.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.0 | +6.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.6 | +5.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.3 | +4.2 |
| fall | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -7.2 | -9.8 |
|  | [[Belinostat (drug)]] 5 µM |  | -6.8 | -8.8 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -6.2 | -6.5 |
|  | [[Panobinostat (drug)]] 5 µM |  | -5.8 | -6.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | -5.5 | -5.4 |
|  | [[Radotinib (drug)]] 5 µM |  | -4.2 | -5.7 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.4 | -2.8 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -2.7 | -2.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.5 | -1.8 |
|  | [[Flumatinib (mesylate) (drug)]] 5 µM |  | -2.2 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | ligand dependent nuclear receptor interacting factor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p13.3 — chr1:110,947,190-110,963,965 (-) |
| Ensembl biotype | protein_coding |
| Also known as | RIF1, FLJ11269; previously C1orf103 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5T3J3](https://www.uniprot.org/uniprotkb/Q5T3J3) (Ligand-dependent nuclear receptor-interacting factor 1):

> Together with SMCHD1, involved in chromosome X inactivation in females by promoting the compaction of heterochromatin. Also able to repress the ligand-induced transcriptional activity of retinoic acid receptor alpha (RARA), possibly through direct recruitment of histone deacetylases. Also required for silencing of the DUX4 locus in somatic cells.

**Summary**, from NCBI Gene [55791](https://www.ncbi.nlm.nih.gov/gene/55791):

> Predicted to enable nuclear retinoic acid receptor binding activity. Involved in dosage compensation by inactivation of X chromosome. Located in Barr body; chromosome, telomeric region; and nucleoplasm. Implicated in facioscapulohumeral muscular dystrophy 3. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:30299](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30299) · Entrez [55791](https://www.ncbi.nlm.nih.gov/gene/55791) · UniProt [Q5T3J3](https://www.uniprot.org/uniprotkb/Q5T3J3) · Ensembl [ENSG00000121931](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000121931)

## Data

Gene col 4307: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4307); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4307, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4307]; `tensor/DDL_lfc|DDL_z.npy` [4307]; `embed/gene_vectors.npy` [4307]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4307 or target_col == 4307). Every well: [[LRIF1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LRIF1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
