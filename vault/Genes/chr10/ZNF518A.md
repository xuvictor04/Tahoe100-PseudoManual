---
symbol: "ZNF518A"
type: "gene"
col: 10869
ensembl_id: "ENSG00000177853"
name: "zinc finger protein 518A"
location: "10q24.1"
module: 11
arm: "+"
pooled_cpm: 90.46
n_lines_expressing: 48
n_dd_up: 5
n_dd_down: 28
n_dd_up_clean: 5
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/011"]
generated_by: "tahoemap"
---

# ZNF518A

*zinc finger protein 518A* — 10q24.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.37× (z +8.2, q 1e-13, up in 33 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 28 drug-doses (12 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.440× (z -15.1, q 0e+00, down in 45 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[METTL18]] (+0.75, fdr 7e-06), [[LARP7]] (+0.75, fdr 1e-05), [[FAM200A]] (+0.74, fdr 7e-06); moves opposite to [[ST6GALNAC6]] (-0.71, fdr 7e-06), [[TPST2]] (-0.69, fdr 1e-05), [[GRB2]] (-0.66, fdr 3e-05).
> It sits in the **+** arm of [[Module 011]] (Mitochondrial translation elongation).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[ANKRD18A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 1 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10869.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.37×** | +8.2 | 1e-13 | 33/46 (RKO, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.43×** | +6.6 | 1e-08 | 32/46 (RKO, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.32×** | +5.0 | 1e-04 | 23/46 (RKO, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.27×** | +4.5 | 1e-03 | 22/46 (A-427, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | 1.14× | +3.4 | 0.063 | 16/46 (LoVo, AsPC-1, …) | rises with dose | low cells (technical?) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 1.20× | +3.3 | 0.063 | 17/46 (A-172, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | 1.19× | +3.3 | 0.063 | 16/46 (SW48, AsPC-1, …) | inconsistent across doses |  |
| [[Bestatin (hydrochloride) (drug)]] 0.5 µM |  | 1.19× | +3.3 | 0.063 | 14/46 (PANC-1, NCI-H1573, …) | inconsistent across doses |  |
| [[NG25 (drug)]] 5 µM |  | **1.40×** | +3.3 | 0.063 | 21/45 (AsPC-1, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Meloxicam (drug)]] 0.5 µM |  | 1.19× | +3.1 | 0.093 | 12/46 (PANC-1, CFPAC-1, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 16 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 28 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10869.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.440×** | -15.1 | 0e+00 | 45/46 (SW480, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.457×** | -14.4 | 7e-45 | 44/46 (HepG2/C3A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.484×** | -13.3 | 3e-38 | 41/46 (HepG2/C3A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.565×** | -10.5 | 9e-24 | 42/46 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **0.568×** | -10.0 | 1e-21 | 29/42 (NCI-H23, HCT15, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **0.595×** | -9.5 | 1e-19 | 41/46 (NCI-H661, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **0.564×** | -9.5 | 2e-19 | 32/46 (SW480, HCT15, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.597×** | -8.8 | 1e-16 | 32/43 (RKO, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.631×** | -8.2 | 2e-14 | 34/45 (PANC-1, SNU-423, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.653×** | -7.8 | 3e-13 | 36/46 (SW480, PANC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.661×** | -7.6 | 1e-12 | 34/46 (HepG2/C3A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.461×** | -7.5 | 4e-12 | 37/43 (C-33 A, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.651×** | -7.5 | 4e-12 | 40/46 (PANC-1, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.500×** | -6.7 | 1e-09 | 37/47 (SK-MEL-2, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **0.711×** | -6.3 | 1e-08 | 30/46 (PANC-1, KATO III, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.754×** | -5.2 | 6e-06 | 24/46 (SK-MEL-2, NCI-H23, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.624×** | -4.5 | 2e-04 | 23/46 (LOX-IMVI, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.856× | -4.0 | 0.001 | 15/47 (CFPAC-1, PANC-1, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.756×** | -3.7 | 0.005 | 24/47 (MIA PaCa-2, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.827×** | -3.5 | 0.011 | 19/46 (CFPAC-1, hTERT-HPNE, …) | rises with dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.718×** | -3.2 | 0.029 | 15/46 (Hs 766T, SHP-77, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.23 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10869. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 123 | 0 | 17 (12 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.270× (z -18.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.381× (z -13.5) |
| [[SW480 (line)]] | alt | 156 | 1 | 12 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.68× (z +11.6) | [[Belinostat (drug)]] 5 µM 0.313× (z -18.4) |
| [[RKO (line)]] | wt | 110 | 4 (1 ⚠) | 7 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.18× (z +23.6) | [[Dinaciclib (drug)]] 0.05 µM 0.114× (z -23.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.374× (z -11.5) |
| [[SK-MEL-2 (line)]] | alt | 115 | 0 | 10 (6 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.300× (z -14.4) ⚠ cell-cycle shift, explains ~56% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.418× (z -10.9) |
| [[NCI-H23 (line)]] | alt | 141 | 0 | 9 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.118× (z -26.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.381× (z -12.6) |
| [[C-33 A (line)]] | alt | 180 | 1 | 7 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.81× (z +10.1) | [[Panobinostat (drug)]] 5 µM 0.367× (z -12.1) |
| [[CFPAC-1 (line)]] | alt | 180 | 0 | 8 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.334× (z -12.7) |
| [[HepG2_C3A (line)]] | wt | 187 | 1 | 6 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.95× (z +11.9) | [[Panobinostat (drug)]] 5 µM 0.224× (z -18.8) |
| [[RPMI-7951 (line)]] | alt | 141 | 0 | 7 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.213× (z -15.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.322× (z -11.7) |
| [[HCT15 (line)]] | alt | 241 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.101× (z -25.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.290× (z -14.5) |
| [[LS 180 (line)]] | wt | 183 | 1 | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.79× (z +11.1) | [[Panobinostat (drug)]] 5 µM 0.341× (z -14.5) |
| [[NCI-H1792 (line)]] | alt | 134 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.217× (z -15.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.322× (z -12.5) |
| [[SHP-77 (line)]] | alt | 151 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.174× (z -23.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.309× (z -16.2) |
| [[A-427 (line)]] | wt | 90.6 | 2 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.20× (z +18.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.374× (z -11.3) ⚠ cell-cycle shift, explains ~66% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.464× (z -8.8) |
| [[HT-29 (line)]] | alt | 103 | 2 (1 ⚠) | 3 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.28× (z +9.4) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 1.76× (z +9.1) | [[Panobinostat (drug)]] 5 µM 0.370× (z -11.2) |
| [[NCI-H460 (line)]] | wt | 56.2 | 0 | 5 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.344× (z -13.7) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.388× (z -12.1) |
| [[SW 900 (line)]] | alt | 128 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.280× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.423× (z -8.7) |
| [[BT-474 (line)]] | alt | 74.9 | 3 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.12× (z +10.8) | [[Belinostat (drug)]] 0.5 µM 0.436× (z -8.5) |
| [[AsPC-1 (line)]] | alt | 71.1 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.299× (z -11.5) |
| [[COLO 205 (line)]] | alt | 143 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.234× (z -14.6) |
| [[HEC-1-A (line)]] | alt | 70.0 | 0 | 3 | — | [[Ixazomib citrate (drug)]] 5 µM 0.428× (z -10.0) |
| [[J82 (line)]] | alt | 44.8 | 0 | 3 (1 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.237× (z -13.9) |
| [[NCI-H596 (line)]] | alt | 93.8 | 1 (1 ⚠) | 2 | [[Pentoxifylline (drug)]] 0.05 µM 3.25× (z +10.3) ⚠ transcription drop | [[L-Eflornithine (monohydrochloride) (drug)]] 0.05 µM 0.386× (z -8.8) |
| [[SNU-423 (line)]] | alt | 76.6 | 0 | 3 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.367× (z -10.0) |
| [[CHP-212 (line)]] | wt | 56.6 | 0 | 2 | — | [[Radotinib (drug)]] 0.5 µM 0.125× (z -10.5) |
| [[H4 (line)]] | wt | 94.1 | 0 | 2 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.255× (z -10.8) |
| [[LOX-IMVI (line)]] | wt | 70.8 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 1.93× (z +8.9) | [[Belinostat (drug)]] 5 µM 0.383× (z -9.3) |
| [[NCI-H661 (line)]] | alt | 107 | 0 | 2 | — | [[Belinostat (drug)]] 0.5 µM 0.0374× (z -16.8) |
| [[A-172 (line)]] | wt | 63.3 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.438× (z -8.7) |
| [[A549 (line)]] | wt | 112 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.301× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[C32 (line)]] | wt | 61.7 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0923× (z -10.2) ⚠ toxic |
| [[KATO III (line)]] | alt | 28.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.188× (z -13.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[LoVo (line)]] | wt | 69.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.395× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[MIA PaCa-2 (line)]] | alt | 64.6 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.315× (z -9.2) ⚠ toxic; cell-cycle shift, explains ~28% of this change |
| [[NCI-H2030 (line)]] | alt | 68.8 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.198× (z -14.0) ⚠ toxic; cell-cycle shift, explains ~28% of this change |
| [[NCI-H2347 (line)]] | alt | 26.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.83× (z +11.7) | — |
| [[Panc 03.27 (line)]] | alt | 69.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.287× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[SW 1271 (line)]] | alt | 44.3 | 0 | 1 | — | [[Pimitespib (drug)]] 0.05 µM 0.0648× (z -8.7) |
| [[SW1417 (line)]] | alt | 75.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.14× (z +11.9) | — |
| [[A498 (line)]] | wt | 61.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 14.1 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 30.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 61.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 34.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 48.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 63.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 109 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.64 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 67.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 90.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10869), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[METTL18]] | +0.75 | +0.72 / +0.69 | both halves | 7e-06 |  |
| [[LARP7]] | +0.75 | +0.81 / +0.57 | both halves | 1e-05 |  |
| [[FAM200A]] | +0.74 | +0.76 / +0.61 | both halves | 7e-06 |  |
| [[ZNF764]] | +0.74 | +0.73 / +0.54 | both halves | 1e-05 | same gene group |
| [[EPC1]] | +0.74 | +0.67 / +0.66 | both halves | 7e-06 |  |
| [[NAIF1]] | +0.73 | +0.74 / +0.60 | both halves | 7e-06 |  |
| [[HHLA3]] | +0.73 | +0.75 / +0.43 | both halves | 3e-05 |  |
| [[SDSL]] | +0.72 | +0.72 / +0.55 | both halves | 1e-05 |  |
| [[MAPK1IP1L]] | +0.71 | +0.68 / +0.55 | both halves | 1e-05 |  |
| [[CMTR2]] | +0.71 | +0.74 / +0.63 | both halves | 7e-06 |  |
| [[ERCC6L2]] | +0.70 | +0.69 / +0.48 | both halves | 2e-05 |  |
| [[ZNF620]] | +0.70 | +0.70 / +0.57 | both halves | 1e-05 | same gene group |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ST6GALNAC6]] | -0.71 | -0.67 / -0.58 | both halves | 7e-06 |  |
| [[TPST2]] | -0.69 | -0.67 / -0.54 | both halves | 1e-05 |  |
| [[GRB2]] | -0.66 | -0.72 / -0.43 | both halves | 3e-05 |  |
| [[GSDMB]] | -0.66 | -0.55 / -0.59 | both halves | 1e-05 |  |
| [[SDHAP1]] | -0.66 | -0.66 / -0.48 | both halves | 2e-05 |  |
| [[LPCAT1]] | -0.66 | -0.69 / -0.43 | both halves | 3e-05 |  |
| [[SDHAP4]] | -0.65 | -0.66 / -0.49 | both halves | 1e-05 |  |
| [[IER3IP1]] | -0.65 | -0.67 / -0.48 | both halves | 2e-05 |  |
| [[LIMK1]] | -0.64 | -0.58 / -0.53 | both halves | 1e-05 |  |
| [[WASF3]] | -0.64 | -0.58 / -0.47 | both halves | 2e-05 |  |
| [[TBC1D24]] | -0.64 | -0.55 / -0.47 | both halves | 2e-05 |  |
| [[GET1]] | -0.64 | -0.58 / -0.50 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ANKRD18A]] | B | ANKRD18A activity raises ZNF518A's level | lines that do not express ANKRD18A (11) vs lines expressing it (39) | 1.49× lower at baseline in the lines without ANKRD18A | 0.037 | ⚠ within organs, on part of the lines; also absent: LRRC61, SLC27A2, CHMP4C |
| [[PPP1R1C]] | B | PPP1R1C activity raises ZNF518A's level | lines that do not express PPP1R1C (13) vs lines expressing it (37) | 1.89× lower at baseline in the lines without PPP1R1C | 0.045 | ⚠ within organs, on part of the lines; also absent: ENSG00000261227, LINC01239, ADGRL4; maybe low, not absent |
| [[ZC3H12B]] | B | ZC3H12B activity raises ZNF518A's level | lines that do not express ZC3H12B (21) vs lines expressing it (29) | 1.72× lower at baseline in the lines without ZC3H12B | 0.088 | ⚠ within organs, on part of the lines; also absent: RUNX3, TMEM132D, LINC01876 |
| [[TRIP6]] | B | TRIP6 activity lowers ZNF518A's level | lines that do not express TRIP6 (12) vs lines expressing it (38) | 1.68× higher at baseline in the lines without TRIP6 | 0.091 | ⚠ within organs, on part of the lines; also absent: EFNB2, PLAC4 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 011]] — Mitochondrial translation elongation; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.710). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-26.4, 10.1); signed map (7.4, -19.6). **Vector** length 115, 36.4% of its response variance represented; |z| ≥ 3 in 1,214 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +11.9 | +6.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +11.8 | +8.2 |
|  | [[Harringtonine (drug)]] 5 µM |  | +11.3 | +5.0 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +8.7 | +2.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +7.1 | +4.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.6 | +2.3 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +4.3 | +3.0 |
|  | [[Berbamine (drug)]] 0.05 µM |  | +2.5 | +1.7 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +2.5 | +2.4 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -6.5 | -9.5 |
|  | [[Belinostat (drug)]] 5 µM |  | -5.9 | -15.1 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -4.8 | -7.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -4.7 | -10.5 |
|  | [[Panobinostat (drug)]] 5 µM |  | -4.6 | -14.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.8 | -4.0 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -3.3 | -3.5 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.0 | -3.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.0 | -7.8 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -2.6 | -3.7 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger protein 518A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q24.1 — chr10:96,129,715-96,205,288 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0335; previously ZNF518 |
| Gene groups (HGNC) | Zinc fingers C2H2-type |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6AHZ1](https://www.uniprot.org/uniprotkb/Q6AHZ1) (Zinc finger protein 518A):

> Through its association with the EHMT1-EHMT2/G9A and PRC2/EED-EZH2 histone methyltransferase complexes may function in gene silencing, regulating repressive post-translational methylation of histone tails at promoters of target genes.

**Summary**, from NCBI Gene [9849](https://www.ncbi.nlm.nih.gov/gene/9849):

> The protein encoded by this gene is a member of the krueppel C2H2-type zinc finger protein family. The encoded protein contains five zinc fingers and is likely a nuclear transcriptional regulator. Numerous transcript variants encoding two different isoforms have been found for this gene. [provided by RefSeq, Aug 2016]

**Accessions** — [HGNC:29009](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29009) · Entrez [9849](https://www.ncbi.nlm.nih.gov/gene/9849) · UniProt [Q6AHZ1](https://www.uniprot.org/uniprotkb/Q6AHZ1) · Ensembl [ENSG00000177853](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000177853)

## Data

Gene col 10869: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10869); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10869, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10869]; `tensor/DDL_lfc|DDL_z.npy` [10869]; `embed/gene_vectors.npy` [10869]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10869 or target_col == 10869). Every well: [[ZNF518A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZNF518A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
