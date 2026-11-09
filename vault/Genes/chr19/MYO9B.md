---
symbol: "MYO9B"
type: "gene"
col: 1795
ensembl_id: "ENSG00000099331"
name: "myosin IXB"
location: "19p13.11"
module: 136
arm: "+"
pooled_cpm: 176.89
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 22
n_dd_up_clean: 7
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/136"]
generated_by: "tahoemap"
---

# MYO9B

*myosin IXB* — 19p13.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.60× (z +10.9, q 1e-24, up in 37 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.380× (z -31.7, q 0e+00, down in 45 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ARID3B]] (+0.75, fdr 1e-05), [[MAP2K1]] (+0.75, fdr 7e-06), [[TMEM184B]] (+0.74, fdr 7e-06); moves opposite to [[FUBP1]] (-0.74, fdr 1e-05), [[ZNF280D]] (-0.71, fdr 7e-06), [[DIS3L]] (-0.69, fdr 1e-05).
> It is in [[Module 136]], a single-armed module (heme metabolism).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[F11R]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 5 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1795.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.60×** | +10.9 | 1e-24 | 37/48 (SW480, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.56×** | +10.3 | 1e-22 | 38/48 (Panc 03.27, SW480, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.53×** | +9.9 | 1e-20 | 37/48 (SW480, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.28×** | +5.8 | 1e-06 | 27/48 (SW480, MIA PaCa-2, …) | top dose only |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.24×** | +4.9 | 1e-04 | 25/47 (NCI-H1573, PANC-1, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | **1.23×** | +4.8 | 2e-04 | 25/48 (SW480, LoVo, …) | top dose only |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.22×** | +4.5 | 4e-04 | 23/47 (H4, hTERT-HPNE, …) | rises with dose | low cells (technical?) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.21×** | +4.5 | 6e-04 | 26/48 (PANC-1, NCI-H1573, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.21×** | +4.3 | 0.001 | 24/47 (H4, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PF-06260933 (drug)]] 5 µM |  | **1.39×** | +4.0 | 0.004 | 28/48 (SW480, C32, …) | top dose only | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.12× | +3.6 | 0.016 | 14/49 (CHP-212, NCI-H1573, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~17% of this change | **1.31×** | +3.2 | 0.058 | 21/45 (SW480, NCI-H2030, …) | all doses, flat | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 5 µM |  | 1.15× | +3.1 | 0.072 | 21/47 (NCI-H1573, PANC-1, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~1% of this change | 1.14× | +3.1 | 0.080 | 15/48 (Panc 03.27, NCI-H2030, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 38 in all, 9 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1795.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.380×** | -31.7 | 0e+00 | 45/48 (NCI-H1792, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.396×** | -20.7 | 0e+00 | 44/48 (LOX-IMVI, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.475×** | -17.3 | 0e+00 | 46/48 (A-427, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.457×** | -16.8 | 0e+00 | 40/45 (A-172, HS-578T, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.504×** | -15.9 | 0e+00 | 42/49 (HS-578T, A-172, …) | all doses, flat | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.534×** | -14.0 | 2e-42 | 38/44 (A-172, SHP-77, …) | all doses, flat | cell-cycle shift (explains ~1% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.616×** | -11.2 | 2e-27 | 35/48 (A-172, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.727×** | -10.5 | 1e-23 | 38/48 (SK-MEL-2, RKO, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **0.745×** | -6.8 | 6e-10 | 35/48 (NCI-H23, HOP62, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.747×** | -6.5 | 4e-09 | 27/47 (MIA PaCa-2, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.834× | -6.0 | 1e-07 | 25/48 (RPMI-7951, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.773×** | -6.0 | 1e-07 | 31/49 (RPMI-7951, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.839× | -5.8 | 3e-07 | 18/48 (A-172, HOP62, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.802×** | -5.1 | 1e-05 | 26/48 (A549, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.806×** | -4.8 | 6e-05 | 25/47 (RKO, BT-474, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.808×** | -4.8 | 7e-05 | 28/48 (PANC-1, RKO, …) | all doses, flat |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.815×** | -4.8 | 7e-05 | 25/48 (HOP62, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.824×** | -4.5 | 2e-04 | 24/47 (AsPC-1, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 0.858× | -4.2 | 8e-04 | 20/48 (AsPC-1, PANC-1, …) | all doses, flat | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1795. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 320 | 0 | 13 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.273× (z -27.7) |
| [[HOP62 (line)]] | alt | 321 | 0 | 10 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.212× (z -22.2) |
| [[A-427 (line)]] | wt | 118 | 3 | 6 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 1.94× (z +9.2) | [[Homoharringtonine (drug)]] 0.5 µM 0.183× (z -23.6) |
| [[A549 (line)]] | wt | 178 | 0 | 9 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.185× (z -27.8) |
| [[AsPC-1 (line)]] | alt | 234 | 0 | 9 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.342× (z -20.5) |
| [[HS-578T (line)]] | alt | 399 | 0 | 9 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.214× (z -28.3) |
| [[NCI-H1792 (line)]] | alt | 230 | 0 | 9 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.156× (z -33.2) |
| [[J82 (line)]] | alt | 220 | 0 | 8 (4 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.568× (z -11.6) |
| [[LOX-IMVI (line)]] | wt | 247 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.198× (z -32.5) |
| [[MIA PaCa-2 (line)]] | alt | 240 | 1 | 7 (4 ⚠) | [[Auranofin (drug)]] 5 µM 2.07× (z +8.9) | [[Homoharringtonine (drug)]] 5 µM 0.334× (z -18.9) |
| [[SW480 (line)]] | alt | 134 | 5 (1 ⚠) | 3 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 3.08× (z +17.6) | [[Harringtonine (drug)]] 5 µM 0.439× (z -12.4) |
| [[H4 (line)]] | wt | 239 | 1 | 6 (2 ⚠) | [[Pitavastatin (Calcium) (drug)]] 5 µM 2.68× (z +10.9) | [[Homoharringtonine (drug)]] 5 µM 0.426× (z -13.8) |
| [[HEC-1-A (line)]] | alt | 132 | 2 | 5 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 1.87× (z +9.7) | [[Harringtonine (drug)]] 0.5 µM 0.470× (z -11.6) |
| [[hTERT-HPNE (line)]] | wt | 254 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.137× (z -22.3) |
| [[LoVo (line)]] | wt | 108 | 3 | 4 | [[Panobinostat (drug)]] 5 µM 2.31× (z +12.0) | [[Homoharringtonine (drug)]] 5 µM 0.291× (z -24.9) |
| [[NCI-H2030 (line)]] | alt | 140 | 3 | 4 (1 ⚠) | [[Belinostat (drug)]] 5 µM 2.39× (z +11.1) | [[Homoharringtonine (drug)]] 5 µM 0.280× (z -23.0) |
| [[NCI-H460 (line)]] | wt | 112 | 1 | 6 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 1.98× (z +8.9) | [[Homoharringtonine (drug)]] 5 µM 0.385× (z -17.4) |
| [[C32 (line)]] | wt | 211 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.387× (z -15.6) |
| [[CFPAC-1 (line)]] | alt | 136 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.381× (z -14.2) |
| [[Panc 03.27 (line)]] | alt | 196 | 3 | 3 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.85× (z +16.6) | [[Dinaciclib (drug)]] 0.05 µM 0.444× (z -11.8) ⚠ toxic; transcription drop · without an alert: [[Selinexor (drug)]] 5 µM 0.644× (z -9.7) |
| [[SK-MEL-2 (line)]] | alt | 291 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.296× (z -26.0) |
| [[HCT15 (line)]] | alt | 184 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.292× (z -19.1) |
| [[KATO III (line)]] | alt | 64.5 | 3 | 2 | [[Panobinostat (drug)]] 5 µM 3.05× (z +12.7) | [[Homoharringtonine (drug)]] 5 µM 0.432× (z -13.5) |
| [[PANC-1 (line)]] | alt | 166 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.441× (z -18.4) |
| [[RPMI-7951 (line)]] | alt | 255 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.291× (z -22.4) |
| [[SNU-423 (line)]] | alt | 213 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.313× (z -22.6) |
| [[SW 900 (line)]] | alt | 138 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.372× (z -17.4) |
| [[CHP-212 (line)]] | wt | 146 | 1 | 3 (2 ⚠) | [[Vinblastine (sulfate) (drug)]] 5 µM 2.59× (z +9.5) | [[Dinaciclib (drug)]] 0.05 µM 0.197× (z -10.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.287× (z -8.8) |
| [[LS 180 (line)]] | wt | 127 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.458× (z -13.3) |
| [[NCI-H23 (line)]] | alt | 176 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.285× (z -22.8) |
| [[RKO (line)]] | wt | 225 | 1 | 3 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 1.86× (z +8.7) | [[Selinexor (drug)]] 5 µM 0.395× (z -18.6) |
| [[SNU-1 (line)]] | wt | 76.4 | 2 (1 ⚠) | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.22× (z +9.8) | [[Dinaciclib (drug)]] 0.05 µM 0.127× (z -15.9) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.409× (z -10.5) |
| [[SW1417 (line)]] | alt | 105 | 3 | 1 | [[Panobinostat (drug)]] 5 µM 2.27× (z +11.0) | [[Homoharringtonine (drug)]] 5 µM 0.475× (z -13.8) |
| [[SW48 (line)]] | wt | 170 | 1 | 3 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.28× (z +9.0) | [[Homoharringtonine (drug)]] 5 µM 0.411× (z -13.6) |
| [[AN3 CA (line)]] | alt | 167 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.224× (z -12.7) |
| [[NCI-H1573 (line)]] | alt | 135 | 1 | 2 | [[Vinblastine (sulfate) (drug)]] 5 µM 2.02× (z +9.3) | [[Homoharringtonine (drug)]] 5 µM 0.259× (z -18.1) |
| [[NCI-H2347 (line)]] | alt | 116 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.550× (z -9.9) |
| [[SW 1271 (line)]] | alt | 306 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.194× (z -13.9) |
| [[A498 (line)]] | wt | 181 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.439× (z -11.1) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.606× (z -9.5) |
| [[C-33 A (line)]] | alt | 114 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.24× (z +8.6) | [[Dinaciclib (drug)]] 0.05 µM 0.350× (z -10.4) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 110 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.38× (z +8.6) | [[Dinaciclib (drug)]] 0.5 µM 0.324× (z -11.1) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 143 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.472× (z -13.1) |
| [[BT-474 (line)]] | alt | 274 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.449× (z -10.0) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 113 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.417× (z -8.9) ⚠ toxic; cell-cycle shift, explains ~8% of this change |
| [[HT-29 (line)]] | alt | 114 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.443× (z -15.5) |
| [[SHP-77 (line)]] | alt | 136 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.202× (z -19.0) ⚠ toxic; transcription drop |
| [[SW 1088 (line)]] | alt | 287 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.186× (z -13.1) |
| [[NCI-H2122 (line)]] | alt | 167 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 180 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 103 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1795), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*71 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARID3B]] | +0.75 | +0.79 / +0.56 | both halves | 1e-05 |  |
| [[MAP2K1]] | +0.75 | +0.74 / +0.68 | both halves | 7e-06 |  |
| [[TMEM184B]] | +0.74 | +0.72 / +0.61 | both halves | 7e-06 |  |
| [[TPST2]] | +0.73 | +0.72 / +0.56 | both halves | 1e-05 |  |
| [[DNAJC5]] | +0.72 | +0.70 / +0.64 | both halves | 7e-06 |  |
| [[RABGEF1]] | +0.71 | +0.71 / +0.81 | both halves | 7e-06 |  |
| [[CSNK1E]] | +0.70 | +0.72 / +0.65 | both halves | 7e-06 |  |
| [[SH3GL1]] | +0.69 | +0.72 / +0.55 | both halves | 1e-05 |  |
| [[PBX4]] | +0.69 | +0.72 / +0.43 | both halves | 3e-05 |  |
| [[GIPR]] | +0.68 | +0.67 / +0.54 | both halves | 1e-05 |  |
| [[PLA2G15]] | +0.68 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[MPG]] | +0.68 | +0.65 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*29 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FUBP1]] | -0.74 | -0.53 / -0.62 | both halves | 1e-05 |  |
| [[ZNF280D]] | -0.71 | -0.67 / -0.61 | both halves | 7e-06 |  |
| [[DIS3L]] | -0.69 | -0.76 / -0.49 | both halves | 1e-05 |  |
| [[BCLAF1]] | -0.69 | -0.54 / -0.56 | both halves | 1e-05 |  |
| [[ZNF608]] | -0.68 | -0.71 / -0.66 | both halves | 7e-06 |  |
| [[CC2D2A]] | -0.66 | -0.64 / -0.55 | both halves | 1e-05 |  |
| [[HNRNPH3]] | -0.66 | -0.62 / -0.43 | both halves | 3e-05 |  |
| [[MTPAP]] | -0.65 | -0.61 / -0.64 | both halves | 7e-06 |  |
| [[EWSR1]] | -0.65 | -0.49 / -0.57 | both halves | 1e-05 |  |
| [[NFIB]] | -0.65 | -0.63 / -0.54 | both halves | 1e-05 |  |
| [[MED12]] | -0.65 | -0.54 / -0.46 | both halves | 3e-05 |  |
| [[TIA1]] | -0.64 | -0.67 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[F11R]] | B | F11R activity lowers MYO9B's level | lines that do not express F11R (10) vs lines expressing it (40) | 1.21× higher at baseline in the lines without F11R | 0.009 | ⚠ within organs, on part of the lines; also absent: ENSG00000287306, LONRF3, TUBA4A |
| [[GFPT2]] | B | GFPT2 activity raises MYO9B's level | lines that do not express GFPT2 (23) vs lines expressing it (27) | 1.52× lower at baseline in the lines without GFPT2 | 0.038 | ⚠ within organs, on part of the lines; also absent: PDCD1LG2, MIR100HG, AK5 |
| [[BICDL1]] | B | BICDL1 activity lowers MYO9B's level | lines that do not express BICDL1 (12) vs lines expressing it (38) | 1.48× higher at baseline in the lines without BICDL1 | 0.040 | ⚠ within organs, on part of the lines; also absent: ABLIM2, KRT18, LINC00857 |
| [[DNAH5]] | B | DNAH5 activity lowers MYO9B's level | lines that do not express DNAH5 (10) vs lines expressing it (40) | 1.06× higher at baseline in the lines without DNAH5 | 0.070 | ⚠ within organs, on part of the lines; also absent: LINC02966; maybe low, not absent |
| [[GPR157]] | C | GPR157's natural level weakens MYO9B's drug response | GPR157's natural level across 49 lines (lineage-adjusted; a glimpse) | r -0.61, reverse +0.01; direction not clear | 0.092 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 136]] — heme metabolism; 35 genes; every member is in the + arm (projection on the module's main direction 0.835). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.32; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (4.4, 1.7); signed map (-24.3, 20.7). **Vector** length 163, 60.1% of its response variance represented; |z| ≥ 3 in 1,784 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM |  | +13.3 | +10.9 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +13.2 | +10.3 |
|  | [[Belinostat (drug)]] 5 µM |  | +12.0 | +9.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +8.0 | +5.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +5.4 | +3.6 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +5.0 | +4.0 |
|  | [[Peretinoin (drug)]] 5 µM |  | +4.9 | +3.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +4.8 | +2.5 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -10.4 | -17.3 |
|  | [[Selinexor (drug)]] 5 µM |  | -9.5 | -10.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | -8.7 | -20.7 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -8.1 | -11.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -8.0 | -31.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | -7.6 | -6.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -6.4 | -4.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -6.0 | -4.8 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | -5.6 | -4.5 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -5.5 | -4.2 |

## What is on record

|  |  |
|---|---|
| Name | myosin IXB |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.11 — chr19:17,075,777-17,214,537 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously CELIAC4 |
| Gene groups (HGNC) | Myosin heavy chains, class IX |
| Hallmark sets | MITOTIC_SPINDLE |
| Reactome | 21 pathways, smallest: SLIT2:ROBO1 increases RHOA activity; RHOF GTPase cycle; FCGR3A-mediated phagocytosis |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13459](https://www.uniprot.org/uniprotkb/Q13459) (Unconventional myosin-IXb):

> Myosins are actin-based motor molecules with ATPase activity. Unconventional myosins serve in intracellular movements. Binds actin with high affinity both in the absence and presence of ATP and its mechanochemical activity is inhibited by calcium ions. Also acts as a GTPase activator for RHOA. Plays a role in the regulation of cell migration via its role as RHOA GTPase activator. This is regulated by its interaction with the SLIT2 receptor ROBO1; interaction with ROBO1 impairs interaction with …

**Summary**, from NCBI Gene [4650](https://www.ncbi.nlm.nih.gov/gene/4650):

> This gene encodes a member of the myosin family of actin-based molecular motor heavy chain proteins. The protein represents an unconventional myosin; it should not be confused with the conventional non-muscle myosin-9 (MYH9). The protein has four IQ motifs located in the neck domain that bind calmodulin, which serves as a light chain. The protein complex has a single-headed structure and exhibits processive movement on actin filaments toward the minus-end. The protein also has rho-GTPase …

**Accessions** — [HGNC:7609](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7609) · Entrez [4650](https://www.ncbi.nlm.nih.gov/gene/4650) · UniProt [Q13459](https://www.uniprot.org/uniprotkb/Q13459) · Ensembl [ENSG00000099331](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000099331)

## Data

Gene col 1795: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1795); `tables/drug_effects.parquet` (52 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1795, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1795]; `tensor/DDL_lfc|DDL_z.npy` [1795]; `embed/gene_vectors.npy` [1795]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1795 or target_col == 1795). Every well: [[MYO9B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MYO9B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
