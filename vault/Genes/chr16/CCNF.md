---
symbol: "CCNF"
type: "gene"
col: 8473
ensembl_id: "ENSG00000162063"
name: "cyclin F"
location: "16p13.3"
module: 22
arm: "+"
pooled_cpm: 21.0
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 45
n_dd_up_clean: 7
n_dd_down_clean: 25
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/022"]
generated_by: "tahoemap"
---

# CCNF

*cyclin F* — 16p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (7 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 2.08× (z +12.1, q 9e-31, up in 37 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 45 drug-doses (20 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.508× (z -15.7, q 0e+00, down in 40 of 48 measured lines) ⚠ cell-cycle shift, explains ~63% of this change. The strongest without an alert is [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM: 0.599× (z -11.9, q 3e-30, down in 36 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KIF18B]] (+0.90, fdr 7e-06), [[PSRC1]] (+0.89, fdr 7e-06), [[CDCA8]] (+0.88, fdr 7e-06).
> It is in [[Module 022]], a single-armed module (G2/M checkpoint).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 7 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8473.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **2.08×** | +12.1 | 9e-31 | 37/48 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **2.02×** | +11.6 | 9e-29 | 38/48 (SW480, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **1.98×** | +11.3 | 3e-27 | 39/47 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.59×** | +7.6 | 4e-12 | 26/46 (SW1417, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~97% of this change | **1.57×** | +7.4 | 1e-11 | 27/45 (PANC-1, NCI-H460, …) | all doses, flat | low cells (technical?) |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~88% of this change | **2.09×** | +6.3 | 2e-08 | 23/45 (NCI-H23, PANC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.41×** | +5.7 | 9e-07 | 19/48 (A498, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); position effect removed |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~91% of this change | **1.27×** | +5.7 | 9e-07 | 25/48 (NCI-H1573, C32, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~92% of this change | **1.34×** | +4.9 | 7e-05 | 18/47 (NCI-H23, PANC-1, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~94% of this change | **1.33×** | +4.7 | 1e-04 | 16/48 (NCI-H23, PANC-1, …) | all doses, flat |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~98% of this change | **1.29×** | +4.2 | 0.002 | 16/46 (PANC-1, A549, …) | all doses, flat | position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **1.59×** | +4.0 | 0.003 | 7/48 (AsPC-1, KATO III, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~98% of this change | **1.25×** | +3.7 | 0.009 | 12/48 (HT-29, CFPAC-1, …) | all doses, flat |  |
| [[Mebendazole (drug)]] 0.5 µM |  | **1.24×** | +3.6 | 0.011 | 6/47 (HepG2/C3A, HT-29, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 5 µM |  | 1.16× | +3.5 | 0.018 | 7/48 (HT-29, HEC-1-A, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 52 in all, 23 with an alert ⚠; shown: the 15 strongest and the 10 next strongest without an alert. 45 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 20 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8473.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **0.508×** | -15.7 | 0e+00 | 40/48 (A-427, LOX-IMVI, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.448×** | -13.2 | 5e-37 | 37/47 (PANC-1, HEC-1-A, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **0.450×** | -13.1 | 7e-37 | 36/48 (SNU-1, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.599×** | -11.9 | 3e-30 | 36/48 (A-172, HOP62, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.504×** | -11.2 | 4e-27 | 32/47 (NCI-H23, C32, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.510×** | -11.0 | 2e-26 | 31/43 (J82, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~56% of this change | **0.521×** | -10.1 | 5e-22 | 30/48 (HEC-1-A, SK-MEL-2, …) | all doses, flat |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.542×** | -9.6 | 4e-20 | 36/46 (HEC-1-A, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Cytarabine (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.565×** | -9.3 | 6e-19 | 36/47 (SNU-1, A549, …) | all doses, flat |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.555×** | -9.3 | 1e-18 | 24/35 (NCI-H2347, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.670×** | -9.2 | 1e-18 | 33/47 (HEC-1-A, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.564×** | -9.0 | 9e-18 | 34/48 (SK-MEL-2, A-427, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **0.585×** | -8.4 | 2e-15 | 30/47 (AsPC-1, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~54% of this change | **0.620×** | -7.8 | 2e-13 | 31/48 (Hs 766T, A-427, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.619×** | -7.3 | 2e-11 | 24/40 (A-427, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Amsacrine (drug)]] 5 µM |  | **0.738×** | -7.0 | 8e-11 | 26/48 (A549, A-172, …) | rises with dose |  |
| [[Cytarabine (drug)]] 0.05 µM |  | **0.634×** | -6.9 | 2e-10 | 25/47 (A549, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.666×** | -6.6 | 8e-10 | 26/47 (HS-578T, NCI-H1573, …) | rises with dose |  |
| [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | **0.650×** | -6.5 | 2e-09 | 28/47 (PANC-1, NCI-H460, …) | all doses, flat |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.681×** | -6.3 | 8e-09 | 21/48 (AN3 CA, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | **0.695×** | -5.7 | 3e-07 | 22/47 (NCI-H1573, HepG2/C3A, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.717×** | -5.4 | 1e-06 | 22/48 (C32, A-172, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.754×** | -4.6 | 9e-05 | 18/47 (SNU-1, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.770×** | -4.3 | 4e-04 | 18/47 (C32, NCI-H460, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.787×** | -3.9 | 0.002 | 15/48 (A-427, MIA PaCa-2, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.20 per unit of S-phase module lfc, +0.99 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8473. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 24.4 | 0 | 7 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.187× (z -12.4) ⚠ toxic; transcription drop · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.198× (z -11.6) |
| [[A-427 (line)]] | wt | 48.4 | 0 | 6 (5 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.165× (z -18.7) ⚠ cell-cycle shift, explains ~63% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.201× (z -11.3) |
| [[A-172 (line)]] | wt | 27.9 | 0 | 4 (3 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.313× (z -10.8) |
| [[C32 (line)]] | wt | 16.6 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0965× (z -12.1) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.155× (z -9.6) |
| [[NCI-H1573 (line)]] | alt | 14.6 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.120× (z -11.1) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 29.6 | 0 | 3 (2 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM 0.0682× (z -11.3) ⚠ cell-cycle shift, explains ~60% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.107× (z -9.4) |
| [[SW480 (line)]] | alt | 26.4 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.80× (z +9.1) | [[Dinaciclib (drug)]] 5 µM 0.272× (z -11.2) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 22.6 | 0 | 2 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.278× (z -11.6) ⚠ cell-cycle shift, explains ~63% of this change |
| [[H4 (line)]] | wt | 27.6 | 0 | 2 (2 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM 0.105× (z -8.7) ⚠ cell-cycle shift, explains ~60% of this change |
| [[HOP62 (line)]] | alt | 23.2 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.245× (z -9.1) ⚠ toxic; transcription drop · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.397× (z -8.7) |
| [[LOX-IMVI (line)]] | wt | 20.3 | 0 | 2 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.182× (z -13.2) ⚠ cell-cycle shift, explains ~63% of this change |
| [[LS 180 (line)]] | wt | 21.1 | 0 | 2 (1 ⚠) | — | [[Belzutifan (drug)]] 5 µM 0.0397× (z -8.9) |
| [[NCI-H23 (line)]] | alt | 27.0 | 0 | 2 | — | [[Auranofin (drug)]] 5 µM 0.120× (z -13.6) |
| [[NCI-H2347 (line)]] | alt | 11.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.139× (z -12.0) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 19.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.263× (z -10.9) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 19.7 | 0 | 2 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0985× (z -11.9) |
| [[AN3 CA (line)]] | alt | 38.6 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.102× (z -8.8) |
| [[C-33 A (line)]] | alt | 38.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.146× (z -11.0) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 11.7 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.208× (z -12.2) ⚠ cell-cycle shift, explains ~63% of this change |
| [[HCT15 (line)]] | alt | 37.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.122× (z -10.3) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 17.3 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.226× (z -10.2) ⚠ cell-cycle shift, explains ~63% of this change |
| [[HS-578T (line)]] | alt | 15.8 | 0 | 1 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.166× (z -8.9) ⚠ cell-cycle shift, explains ~37% of this change |
| [[J82 (line)]] | alt | 32.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.161× (z -14.8) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 24.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.184× (z -10.8) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 14.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.150× (z -11.0) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 21.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.106× (z -9.4) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 41.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.191× (z -9.9) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 15.7 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.267× (z -8.7) ⚠ cell-cycle shift, explains ~63% of this change |
| [[SW1417 (line)]] | alt | 23.5 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.405× (z -8.5) ⚠ cell-cycle shift, explains ~63% of this change |
| [[A498 (line)]] | wt | 17.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 18.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.19 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 12.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 15.2 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 9.30 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.46 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 27.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 21.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 23.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8473), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KIF18B]] | +0.90 | +0.90 / +0.91 | both halves | 7e-06 | same gene group; STRING 624 |
| [[PSRC1]] | +0.89 | +0.87 / +0.85 | both halves | 7e-06 | **novel candidate** |
| [[CDCA8]] | +0.88 | +0.89 / +0.92 | both halves | 7e-06 | STRING 733 |
| [[GPSM2]] | +0.87 | +0.85 / +0.82 | both halves | 7e-06 | **novel candidate** |
| [[DLGAP5]] | +0.87 | +0.89 / +0.85 | both halves | 7e-06 | STRING 606 |
| [[GTSE1]] | +0.87 | +0.87 / +0.90 | both halves | 7e-06 | STRING 555 |
| [[CKAP2]] | +0.85 | +0.83 / +0.86 | both halves | 7e-06 |  |
| [[KIF2C]] | +0.85 | +0.87 / +0.87 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 672 |
| [[CDCA3]] | +0.85 | +0.84 / +0.84 | both halves | 7e-06 | STRING 743 |
| [[CDKN3]] | +0.85 | +0.78 / +0.84 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT |
| [[HJURP]] | +0.85 | +0.85 / +0.83 | both halves | 7e-06 | STRING 698 |
| [[PTTG1]] | +0.84 | +0.84 / +0.81 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 515 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 2, C 4.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises CCNF's level | compounds that target TOP2A: 5 of 5 lower it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 7.3% of all compounds | 0.010 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[NEURL1B]] | B | NEURL1B activity raises CCNF's level | lines that do not express NEURL1B (7) vs lines expressing it (43) | 1.68× lower at baseline in the lines without NEURL1B | 0.080 | ⚠ within organs, on part of the lines; also absent: PIMREG, WNT9A, ENSG00000267131 |
| [[NDC80]] | C | NDC80 activity raises CCNF's level | lines that do not express NDC80 (3) vs lines expressing it (47) | 1.99× lower at baseline in the lines without NDC80 | 0.049 | ⚠ few lines (3 vs 47); across organs; also absent: SH3BP5, DSCC1, KLF9; maybe low, not absent |
| [[FAM72D]] | C | FAM72D activity raises CCNF's level | lines that do not express FAM72D (3) vs lines expressing it (47) | 1.77× lower at baseline in the lines without FAM72D | 0.062 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: ATP6V1E2, ASAP3, ENSG00000267131; maybe low, not absent; its own permutation p |
| [[CDCA3]] | C | CDCA3 activity raises CCNF's level | lines that do not express CDCA3 (3) vs lines expressing it (47) | 2.08× lower at baseline in the lines without CDCA3 | 0.085 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: TBC1D19, PBK, SNPH; maybe low, not absent |
| [[CDC20]] | C | CDC20 activity raises CCNF's level | lines that do not express CDC20 (3) vs lines expressing it (47) | 2.19× lower at baseline in the lines without CDC20 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: SPDL1, ARHGAP10, CDC45; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 022]] — G2/M checkpoint; 185 genes; every member is in the + arm (projection on the module's main direction 0.843). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-35.7, -57.1); signed map (-50.1, -40.8). **Vector** length 148, 47.3% of its response variance represented; |z| ≥ 3 in 1,359 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *DREAM G2/M down* (control, mean cos +0.77 to 28); *Mitotic Prometaphase* (reactome, mean cos +0.64 to 48); *E2F targets* (hallmark, mean cos +0.62 to 46).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM |  | +7.2 | +11.3 |
|  | [[Panobinostat (drug)]] 5 µM |  | +6.5 | +11.6 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +6.5 | +12.1 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~97% of this change | +5.6 | +7.4 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +4.8 | +5.7 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +3.1 | +2.3 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.0 | +4.0 |
|  | [[Mebendazole (drug)]] 0.5 µM |  | +2.9 | +3.6 |
|  | [[Docetaxel (drug)]] 5 µM |  | +2.9 | +3.5 |
|  | [[Vinblastine (sulfate) (drug)]] 0.05 µM |  | +2.4 | +2.7 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | -9.5 | -15.7 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~59% of this change | -8.8 | -13.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -7.4 | -11.9 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~56% of this change | -7.0 | -10.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | -6.8 | -13.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -6.4 | -11.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -5.2 | -6.6 |
|  | [[Amsacrine (drug)]] 5 µM |  | -4.6 | -7.0 |
|  | [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | -3.5 | -6.5 |

## What is on record

|  |  |
|---|---|
| Name | cyclin F |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p13.3 — chr16:2,429,394-2,458,854 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FBX1, FBXO1 |
| Gene groups (HGNC) | Cyclins; F-boxes other; MicroRNA protein coding host genes |
| Hallmark sets | MTORC1_SIGNALING, G2M_CHECKPOINT |
| Reactome | 4 pathways, smallest: Neddylation; Antigen processing: Ubiquitination & Proteasome degradation; Class I MHC mediated antigen processing & presentation |
| Matched by | ensembl_id |

**Function**, from UniProt [P41002](https://www.uniprot.org/uniprotkb/P41002) (Cyclin-F):

> Substrate recognition component of a SCF (SKP1-CUL1-F-box protein) E3 ubiquitin-protein ligase complex which mediates the ubiquitination and subsequent proteasomal degradation of target proteins. The SCF(CCNF) E3 ubiquitin-protein ligase complex is an integral component of the ubiquitin proteasome system (UPS) and links proteasome degradation to the cell cycle. Mediates the substrate recognition and the proteasomal degradation of various target proteins involved in the regulation of cell cycle …

**Summary**, from NCBI Gene [899](https://www.ncbi.nlm.nih.gov/gene/899):

> This gene encodes a member of the cyclin family. Cyclins are important regulators of cell cycle transitions through their ability to bind and activate cyclin-dependent protein kinases. This member also belongs to the F-box protein family which is characterized by an approximately 40 amino acid motif, the F-box. The F-box proteins constitute one of the four subunits of the ubiquitin protein ligase complex called SCFs (SKP1-cullin-F-box), which function in phosphorylation-dependent …

**Accessions** — [HGNC:1591](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1591) · Entrez [899](https://www.ncbi.nlm.nih.gov/gene/899) · UniProt [P41002](https://www.uniprot.org/uniprotkb/P41002) · Ensembl [ENSG00000162063](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000162063)

## Data

Gene col 8473: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8473); `tables/drug_effects.parquet` (67 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8473, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8473]; `tensor/DDL_lfc|DDL_z.npy` [8473]; `embed/gene_vectors.npy` [8473]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8473 or target_col == 8473). Every well: [[CCNF — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CCNF.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
