---
symbol: "MIR583HG"
type: "gene"
col: 14700
ensembl_id: "ENSG00000250551"
name: ""
location: ""
module: 26
arm: "+"
pooled_cpm: 33.06
n_lines_expressing: 40
n_dd_up: 9
n_dd_down: 37
n_dd_up_clean: 7
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 3
direction_downstream: 7
tags: ["gene", "module/026"]
generated_by: "tahoemap"
---

# MIR583HG

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.46× (z +5.9, q 2e-06, up in 21 of 37 measured lines).
> Pooled over the cell lines (median), lowered significantly by 37 drug-doses (21 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.223× (z -16.4, q 0e+00, down in 37 of 38 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 0.400× (z -10.0, q 1e-21, down in 32 of 38 measured lines).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC01135]] (+0.57, fdr 2e-05), [[PKN2-AS1]] (+0.56, fdr 2e-05), [[TMEM232]] (+0.54, fdr 2e-05); moves opposite to [[NAA40]] (-0.56, fdr 3e-05), [[FAM118A]] (-0.53, fdr 5e-05), [[CRACD]] (-0.51, fdr 2e-05).
> It sits in the **+** arm of [[Module 026]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[NAALADL2]] → it (grade B ⚠); 7 go from it, the strongest it → [[TMEM232]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 2 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14700.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.46×** | +5.9 | 2e-06 | 21/37 (LoVo, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.51×** | +4.6 | 0.001 | 18/37 (NCI-H460, LS 180, …) | two highest doses |  |
| [[Trametinib (drug)]] 0.05 µM |  | **1.28×** | +3.8 | 0.024 | 17/38 (NCI-H23, SW480, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.40×** | +3.8 | 0.024 | 19/38 (LOX-IMVI, H4, …) | all doses, flat |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **1.38×** | +3.6 | 0.036 | 18/38 (SK-MEL-2, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.25×** | +3.5 | 0.037 | 16/38 (LS 180, NCI-H460, …) | two highest doses |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **1.24×** | +3.5 | 0.044 | 12/38 (HepG2/C3A, LoVo, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.35×** | +3.3 | 0.069 | 16/38 (LOX-IMVI, H4, …) | all doses, flat |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.34×** | +3.2 | 0.099 | 12/38 (NCI-H2030, A498, …) | top dose only |  |
| [[Afatinib (drug)]] 5 µM |  | 1.40× | +3.1 | 0.12 | 15/37 (CFPAC-1, HepG2/C3A, …) | rises with dose | noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 5 µM |  | 1.69× | +3.0 | 0.13 | 7/37 (NCI-H2347, SW480, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 21 with an alert ⚠; shown: the 15 strongest and the 12 next strongest without an alert. 37 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 21 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14700.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **0.223×** | -16.4 | 0e+00 | 37/38 (COLO 205, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.265×** | -13.9 | 9e-42 | 31/35 (NCI-H460, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.302×** | -13.1 | 6e-37 | 36/38 (PANC-1, HT-29, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.340×** | -11.8 | 7e-30 | 38/38 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~27% of this change | **0.362×** | -10.7 | 2e-24 | 32/36 (J82, hTERT-HPNE, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.400×** | -10.0 | 1e-21 | 32/38 (RPMI-7951, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.419×** | -9.5 | 2e-19 | 31/38 (RKO, A498, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.446×** | -8.8 | 8e-17 | 32/38 (COLO 205, SW480, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change | **0.415×** | -8.6 | 4e-16 | 24/35 (RKO, NCI-H460, …) | all doses, flat | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **0.458×** | -8.5 | 9e-16 | 31/38 (RKO, A498, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.460×** | -8.5 | 1e-15 | 33/38 (PANC-1, HCT15, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | **0.442×** | -8.2 | 8e-15 | 24/33 (LoVo, J82, …) | all doses, flat | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.475×** | -8.1 | 2e-14 | 29/38 (RKO, J82, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.295×** | -7.0 | 1e-10 | 34/38 (NCI-H23, HT-29, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~22% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~79% of this change | **0.515×** | -7.0 | 1e-10 | 18/28 (NCI-H460, J82, …) | all doses, flat | composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **0.535×** | -6.8 | 3e-10 | 27/38 (LoVo, SNU-423, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.505×** | -6.7 | 7e-10 | 29/38 (NCI-H460, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.572×** | -5.7 | 3e-07 | 24/37 (J82, HT-29, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.695×** | -5.6 | 7e-07 | 24/38 (RKO, SNU-423, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.609×** | -5.4 | 2e-06 | 21/37 (J82, HT-29, …) | two highest doses | cell-cycle shift (explains ~18% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.629×** | -5.0 | 1e-05 | 24/38 (HT-29, LOX-IMVI, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM |  | **0.648×** | -4.7 | 6e-05 | 22/37 (CFPAC-1, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.477×** | -4.2 | 5e-04 | 17/38 (RKO, C32, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Vilanterol (drug)]] 5 µM |  | **0.764×** | -4.1 | 7e-04 | 18/38 (hTERT-HPNE, NCI-H460, …) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.535×** | -3.6 | 0.007 | 15/37 (J82, HOP62, …) | rises with dose | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **0.728×** | -3.2 | 0.025 | 14/36 (HT-29, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Pasireotide (acetate) (drug)]] 5 µM |  | **0.813×** | -3.2 | 0.026 | 11/38 (LOX-IMVI, RPMI-7951, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.56 per unit of S-phase module lfc, -0.36 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14700. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[J82 (line)]] | alt | 161 | 0 | 18 (12 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0578× (z -17.6) ⚠ toxic; cell-cycle shift, explains ~27% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.260× (z -12.2) |
| [[HT-29 (line)]] | alt | 37.7 | 0 | 14 (12 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0684× (z -17.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.198× (z -10.5) |
| [[RKO (line)]] | wt | 244 | 0 | 12 (9 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0600× (z -22.0) ⚠ cell-cycle shift, explains ~51% of this change · without an alert: [[Selinexor (drug)]] 5 µM 0.392× (z -10.3) |
| [[NCI-H460 (line)]] | wt | 36.6 | 0 | 11 (10 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0690× (z -21.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~79% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.302× (z -9.8) |
| [[PANC-1 (line)]] | alt | 26.1 | 0 | 9 (7 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.128× (z -15.9) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.180× (z -13.2) |
| [[SNU-423 (line)]] | alt | 48.8 | 0 | 9 (7 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0994× (z -12.2) ⚠ toxic; cell-cycle shift, explains ~27% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.146× (z -10.6) |
| [[NCI-H1573 (line)]] | alt | 90.1 | 0 | 7 (7 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0950× (z -18.0) ⚠ toxic |
| [[A498 (line)]] | wt | 25.5 | 0 | 6 (5 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.140× (z -12.7) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.256× (z -8.8) |
| [[COLO 205 (line)]] | alt | 31.0 | 0 | 6 (6 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0419× (z -17.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[CFPAC-1 (line)]] | alt | 28.2 | 0 | 5 (4 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.165× (z -10.6) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.223× (z -8.8) |
| [[HS-578T (line)]] | alt | 55.3 | 0 | 5 (5 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.143× (z -12.0) ⚠ toxic; cell-cycle shift, explains ~27% of this change |
| [[NCI-H1792 (line)]] | alt | 34.0 | 0 | 5 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0833× (z -14.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[RPMI-7951 (line)]] | alt | 27.4 | 0 | 5 (4 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.0700× (z -12.5) |
| [[SW480 (line)]] | alt | 15.8 | 0 | 5 (5 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0808× (z -16.6) ⚠ cell-cycle shift, explains ~26% of this change |
| [[HOP62 (line)]] | alt | 52.0 | 0 | 4 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.215× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[LOX-IMVI (line)]] | wt | 79.0 | 3 | 1 (1 ⚠) | [[Clobetasol propionate (drug)]] 0.05 µM 5.50× (z +9.8) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.165× (z -10.0) ⚠ toxic |
| [[NCI-H23 (line)]] | alt | 33.8 | 0 | 4 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.166× (z -12.5) ⚠ toxic · without an alert: [[TAK-901 (drug)]] 5 µM 0.0506× (z -11.3) |
| [[A549 (line)]] | wt | 19.1 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.178× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.200× (z -8.7) |
| [[HCT15 (line)]] | alt | 30.0 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0327× (z -17.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.0963× (z -11.9) |
| [[LoVo (line)]] | wt | 17.8 | 1 | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.99× (z +14.1) | [[Dinaciclib (drug)]] 0.05 µM 0.118× (z -14.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change · without an alert: [[Belinostat (drug)]] 0.5 µM 0.217× (z -11.0) |
| [[SHP-77 (line)]] | alt | 32.2 | 0 | 3 (3 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.117× (z -9.1) ⚠ cell-cycle shift, explains ~26% of this change |
| [[HEC-1-A (line)]] | alt | 15.0 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.178× (z -10.6) ⚠ toxic |
| [[SW 1088 (line)]] | alt | 106 | 0 | 2 | — | [[Osimertinib (mesylate) (drug)]] 0.05 µM 0.0605× (z -9.6) |
| [[A-172 (line)]] | wt | 42.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0827× (z -12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change |
| [[A-427 (line)]] | wt | 13.6 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0704× (z -12.7) ⚠ cell-cycle shift, explains ~53% of this change |
| [[C32 (line)]] | wt | 13.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.73× (z +8.9) | — |
| [[H4 (line)]] | wt | 22.8 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.108× (z -9.7) ⚠ cell-cycle shift, explains ~31% of this change |
| [[hTERT-HPNE (line)]] | wt | 32.3 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0428× (z -15.5) ⚠ toxic; cell-cycle shift, explains ~27% of this change |
| [[LS 180 (line)]] | wt | 8.77 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.88× (z +8.5) | — |
| [[Panc 03.27 (line)]] | alt | 16.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.119× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[SW 900 (line)]] | alt | 13.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0617× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[AN3 CA (line)]] | alt | 5.52 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 4.65 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 5.41 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 5.84 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 9.62 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 18.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.75 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.99 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 27.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 36.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.16 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 39.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.83 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 49.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.12 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 6.75 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14700), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC01135]] | +0.57 | +0.47 / +0.47 | both halves | 2e-05 |  |
| [[PKN2-AS1]] | +0.56 | +0.48 / +0.48 | both halves | 2e-05 |  |
| [[TMEM232]] | +0.54 | +0.49 / +0.47 | both halves | 2e-05 |  |
| [[SAMSN1]] | +0.54 | +0.54 / +0.43 | both halves | 3e-05 |  |
| [[NAALADL2]] | +0.53 | +0.42 / +0.43 | both halves | 4e-05 |  |
| [[STXBP5-AS1]] | +0.53 | +0.39 / +0.49 | both halves | 5e-05 |  |
| [[NEPRO-AS1]] | +0.52 | +0.46 / +0.38 | both halves | 7e-05 |  |
| [[LINC01252]] | +0.51 | +0.41 / +0.47 | both halves | 4e-05 |  |
| [[TG]] | +0.51 | +0.43 / +0.36 | both halves | 1e-04 |  |
| [[SGO1-AS1]] | +0.50 | +0.41 / +0.40 | both halves | 5e-05 |  |
| [[USP38-DT]] | +0.50 | +0.41 / +0.37 | both halves | 8e-05 |  |
| [[METTL6]] | +0.50 | +0.54 / +0.22 | both halves | 6e-04 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NAA40]] | -0.56 | -0.52 / -0.43 | both halves | 3e-05 |  |
| [[FAM118A]] | -0.53 | -0.39 / -0.46 | both halves | 5e-05 |  |
| [[CRACD]] | -0.51 | -0.58 / -0.47 | both halves | 2e-05 |  |
| [[AP3M2]] | -0.51 | -0.52 / -0.27 | both halves | 3e-04 |  |
| [[SBK1]] | -0.49 | -0.46 / -0.27 | both halves | 3e-04 |  |
| [[PARD6G]] | -0.48 | -0.43 / -0.39 | both halves | 6e-05 |  |
| [[SGSM1]] | -0.48 | -0.49 / -0.29 | both halves | 2e-04 |  |
| [[CABLES2]] | -0.47 | -0.27 / -0.33 | both halves | 3e-04 |  |
| [[PPT2]] | -0.47 | -0.43 / -0.37 | both halves | 9e-05 |  |
| [[DNMT3B]] | -0.47 | -0.48 / -0.29 | both halves | 3e-04 |  |
| [[HDAC1]] | -0.46 | -0.42 / -0.32 | both halves | 2e-04 |  |
| [[CMTM8]] | -0.46 | -0.47 / -0.26 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NAALADL2]] | B | NAALADL2 activity raises MIR583HG's level | lines that do not express NAALADL2 (11) vs lines expressing it (39) | 2.69× lower at baseline in the lines without NAALADL2 | 0.020 | ⚠ within organs, on part of the lines; also absent: CA3, PCNX2, CA13 |
| [[ENOX1]] | B | ENOX1 activity raises MIR583HG's level | lines that do not express ENOX1 (12) vs lines expressing it (38) | 2.56× lower at baseline in the lines without ENOX1 | 0.073 | ⚠ within organs, on part of the lines; also absent: CYP1B1-AS1, HTR7, SLC1A3; maybe low, not absent |
| [[CA3]] | C | CA3 activity raises MIR583HG's level | lines that do not express CA3 (10) vs lines expressing it (40) | 3.60× lower at baseline in the lines without CA3 | 0.022 | ⚠ within organs, on part of the lines; also absent: CA13, NAALADL2, PLSCR2; co-absent with the target |

### Downstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 7, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TMEM232]] | B | MIR583HG activity raises TMEM232's level | lines that do not express MIR583HG (10) vs lines expressing it (40) | 1.97× lower at baseline in the lines without MIR583HG | 0.040 | ⚠ within organs, on part of the lines; co-absent genes; also absent: RGS17, GNAI1, KLF12; maybe low, not absent |
| [[NPR3]] | B | MIR583HG activity raises NPR3's level | lines that do not express MIR583HG (10) vs lines expressing it (40) | 1.95× lower at baseline in the lines without MIR583HG | 0.045 | ⚠ within organs, on part of the lines; co-absent genes; also absent: RGS17, GNAI1, KLF12; maybe low, not absent |
| [[CCDC122]] | B | MIR583HG activity raises CCDC122's level | lines that do not express MIR583HG (10) vs lines expressing it (40) | 2.75× lower at baseline in the lines without MIR583HG | 0.055 | ⚠ within organs, on part of the lines; co-absent genes; also absent: RGS17, GNAI1, KLF12; maybe low, not absent |
| [[ENOX1]] | B | MIR583HG activity raises ENOX1's level | lines that do not express MIR583HG (10) vs lines expressing it (40) | 1.53× lower at baseline in the lines without MIR583HG | 0.076 | ⚠ within organs, on part of the lines; co-absent genes; also absent: RGS17, GNAI1, KLF12; maybe low, not absent |
| [[SGO1-AS1]] | B | MIR583HG activity raises SGO1-AS1's level | lines that do not express MIR583HG (10) vs lines expressing it (40) | 1.98× lower at baseline in the lines without MIR583HG | 0.080 | ⚠ within organs, on part of the lines; co-absent genes; also absent: RGS17, GNAI1, KLF12; maybe low, not absent |
| [[PRR5]] | B | MIR583HG activity lowers PRR5's level | lines that do not express MIR583HG (10) vs lines expressing it (40) | 1.95× higher at baseline in the lines without MIR583HG | 0.095 | ⚠ within organs, on part of the lines; co-absent genes; also absent: RGS17, GNAI1, KLF12; maybe low, not absent |
| [[BOLA1]] | B | MIR583HG activity raises BOLA1's level | lines that do not express MIR583HG (10) vs lines expressing it (40) | 1.48× lower at baseline in the lines without MIR583HG | 0.095 | ⚠ within organs, on part of the lines; co-absent genes; also absent: RGS17, GNAI1, KLF12; maybe low, not absent |

## Where it sits

- **Module**: [[Module 026]]; 163 genes; this gene is in the **+** arm (projection on the module's main direction 0.440). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (9.8, 14.4); signed map (27.9, -9.0). **Vector** length 81.1, 19.8% of its response variance represented; |z| ≥ 3 in 1,332 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.3 | +5.9 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +5.5 | -4.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.2 | -5.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.7 | -0.4 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | +3.5 | -6.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.6 | +0.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.5 | +1.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.0 | +3.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.9 | +2.7 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +1.8 | +3.3 |
| fall | [[Selinexor (drug)]] 5 µM |  | -6.0 | -5.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -4.4 | -6.7 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -4.2 | -6.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -3.5 | -13.9 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | -3.4 | -9.5 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.1 | -1.1 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | -1.7 | -2.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | -1.6 | -3.2 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -1.4 | -1.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.4 | -8.5 |

## What is on record

> [!warning] No registry record
> MIR583HG has no HGNC entry matched to it: no approved name, no gene group, no cross-references. The quantification assigned reads to this identifier and that is what is known; nothing more is claimed.

## Data

Gene col 14700: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14700); `tables/drug_effects.parquet` (48 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14700, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14700]; `tensor/DDL_lfc|DDL_z.npy` [14700]; `embed/gene_vectors.npy` [14700]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14700 or target_col == 14700). Every well: [[MIR583HG — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MIR583HG.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
