---
symbol: "SMARCAL1"
type: "gene"
col: 6160
ensembl_id: "ENSG00000138375"
name: "SNF2 related chromatin remodeling annealing helicase 1"
location: "2q35"
module: 7
arm: "+"
pooled_cpm: 27.58
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 27
n_dd_up_clean: 4
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 3
direction_downstream: 1
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# SMARCAL1

*SNF2 related chromatin remodeling annealing helicase 1* — 2q35

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 1.23× (z +4.9, q 6e-04, up in 17 of 48 measured lines) ⚠ cell-cycle shift, would explain all of this change. The strongest without an alert is [[Ponatinib (drug)]] 0.5 µM: 1.26× (z +3.8, q 0.038, up in 15 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 27 drug-doses (15 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.250× (z -22.8, q 0e+00, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[C8orf33]] (+0.58, fdr 5e-05), [[FASTKD2]] (+0.56, fdr 2e-05), [[ZNF343]] (+0.56, fdr 1e-05); moves opposite to [[SLC35B2]] (-0.55, fdr 2e-04), [[CHKA]] (-0.55, fdr 2e-05), [[CADM4]] (-0.52, fdr 1e-04).
> It sits in the **+** arm of [[Module 007]] (Dengue Virus-Host Interactions).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[CAMK2N1]] → it (grade B ⚠); 1 goes from it, the strongest it → [[SMYD5]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6160.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.23×** | +4.9 | 6e-04 | 17/48 (KATO III, LS 180, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.26×** | +3.8 | 0.038 | 15/48 (HT-29, A-172, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.25×** | +3.6 | 0.054 | 15/47 (SW480, SK-MEL-2, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.24×** | +3.6 | 0.054 | 15/48 (SW48, RKO, …) | rises with dose |  |
| [[Bimiralisib (drug)]] 5 µM |  | **1.48×** | +3.4 | 0.076 | 5/47 (HEC-1-A, SW480, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | 1.22× | +3.2 | 0.14 | 11/47 (A498, NCI-H2030, …) | rises with dose |  |
| [[Demeclocycline (drug)]] 5 µM |  | 1.14× | +3.1 | 0.15 | 7/48 (RPMI-7951, NCI-H460, …) | top dose only |  |
| [[Tirabrutinib (drug)]] 0.5 µM |  | 1.20× | +3.0 | 0.18 | 6/48 (A549, HOP62, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 15 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 27 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6160.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.250×** | -22.8 | 0e+00 | 47/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.256×** | -22.4 | 0e+00 | 47/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.382×** | -22.3 | 0e+00 | 41/47 (PANC-1, NCI-H460, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.379×** | -15.9 | 0e+00 | 47/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.387×** | -15.0 | 0e+00 | 44/47 (PANC-1, NCI-H460, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.422×** | -14.1 | 2e-43 | 44/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.437×** | -13.0 | 5e-37 | 38/47 (PANC-1, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~25% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.466×** | -12.5 | 5e-34 | 42/48 (PANC-1, A-172, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.477×** | -12.1 | 5e-32 | 41/48 (PANC-1, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.502×** | -11.3 | 8e-28 | 37/48 (PANC-1, HEC-1-A, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.576×** | -9.0 | 8e-18 | 28/47 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.386×** | -8.2 | 1e-14 | 39/48 (H4, MIA PaCa-2, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~22% here); composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.622×** | -7.8 | 3e-13 | 33/48 (HS-578T, MIA PaCa-2, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.657×** | -6.9 | 2e-10 | 32/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | **0.642×** | -6.7 | 7e-10 | 23/40 (C32, SW1417, …) | inconsistent across doses | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.820×** | -4.6 | 1e-04 | 22/48 (NCI-H460, C32, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.648×** | -3.7 | 0.005 | 19/48 (HOP62, SK-MEL-2, …) | rises with dose | noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.663×** | -3.5 | 0.011 | 15/47 (PANC-1, H4, …) | top dose only | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.820×** | -3.2 | 0.026 | 16/48 (SW 1088, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Aprepitant (drug)]] 0.05 µM |  | **0.826×** | -3.1 | 0.039 | 12/48 (NCI-H661, HT-29, …) | inconsistent across doses |  |
| [[Budesonide (drug)]] 0.05 µM |  | 0.838× | -2.9 | 0.082 | 10/48 (SW 900, AsPC-1, …) | inconsistent across doses |  |
| [[Pasireotide (acetate) (drug)]] 5 µM |  | 0.882× | -2.9 | 0.082 | 5/48 (A-172, HOP62, …) | rises with dose |  |
| [[Piroxicam (drug)]] 0.05 µM |  | 0.840× | -2.8 | 0.088 | 4/48 (SW 900, Hs 766T, …) | inconsistent across doses |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | 0.841× | -2.8 | 0.088 | 12/48 (hTERT-HPNE, RPMI-7951, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.35 per unit of S-phase module lfc, -0.34 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6160. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 32.8 | 0 | 15 (11 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.193× (z -21.0) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.143× (z -17.6) |
| [[PANC-1 (line)]] | alt | 40.5 | 0 | 11 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.161× (z -29.2) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.170× (z -20.0) |
| [[A-172 (line)]] | wt | 54.4 | 0 | 8 (7 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.192× (z -14.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.517× (z -8.6) |
| [[HEC-1-A (line)]] | alt | 30.8 | 0 | 8 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.291× (z -16.3) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.373× (z -9.2) |
| [[RPMI-7951 (line)]] | alt | 40.7 | 0 | 7 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0723× (z -17.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.199× (z -11.0) |
| [[H4 (line)]] | wt | 37.0 | 0 | 6 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.105× (z -13.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.120× (z -12.6) |
| [[LOX-IMVI (line)]] | wt | 28.2 | 0 | 6 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.204× (z -11.9) |
| [[MIA PaCa-2 (line)]] | alt | 35.6 | 0 | 6 (4 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0483× (z -21.6) ⚠ toxic; cell-cycle shift, explains ~25% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.181× (z -12.7) |
| [[NCI-H1573 (line)]] | alt | 28.8 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.241× (z -16.7) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.225× (z -12.4) |
| [[SNU-1 (line)]] | wt | 28.8 | 0 | 6 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0584× (z -16.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0943× (z -13.6) |
| [[SW480 (line)]] | alt | 23.9 | 0 | 6 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.124× (z -20.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.153× (z -18.1) |
| [[LoVo (line)]] | wt | 20.0 | 0 | 5 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.142× (z -17.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.214× (z -13.4) |
| [[NCI-H1792 (line)]] | alt | 25.7 | 0 | 5 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.197× (z -11.1) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.232× (z -10.0) |
| [[HOP62 (line)]] | alt | 25.7 | 0 | 4 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.193× (z -12.5) |
| [[SW1417 (line)]] | alt | 24.7 | 0 | 4 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.161× (z -13.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.247× (z -10.6) |
| [[A549 (line)]] | wt | 31.5 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.204× (z -17.5) ⚠ cell-cycle shift, explains ~30% of this change |
| [[C32 (line)]] | wt | 27.8 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.124× (z -12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.273× (z -8.7) |
| [[CFPAC-1 (line)]] | alt | 25.4 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.230× (z -14.1) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.242× (z -9.6) |
| [[Hs 766T (line)]] | wt | 22.5 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.309× (z -10.0) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.230× (z -8.9) |
| [[HT-29 (line)]] | alt | 12.9 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.153× (z -10.8) |
| [[hTERT-HPNE (line)]] | wt | 24.5 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.275× (z -10.2) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.163× (z -10.2) |
| [[Panc 03.27 (line)]] | alt | 24.9 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.223× (z -10.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.251× (z -9.3) |
| [[SHP-77 (line)]] | alt | 21.8 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.124× (z -13.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.188× (z -10.7) |
| [[SNU-423 (line)]] | alt | 31.9 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.125× (z -19.7) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.109× (z -14.8) |
| [[SW 900 (line)]] | alt | 20.2 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.103× (z -13.4) |
| [[A498 (line)]] | wt | 29.1 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.300× (z -15.1) ⚠ cell-cycle shift, explains ~30% of this change |
| [[HepG2_C3A (line)]] | wt | 19.3 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.116× (z -10.7) ⚠ toxic |
| [[HS-578T (line)]] | alt | 25.6 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.241× (z -9.1) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 13.8 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0951× (z -14.1) |
| [[NCI-H2030 (line)]] | alt | 39.6 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.218× (z -11.9) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 21.3 | 0 | 2 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0864× (z -14.5) ⚠ cell-cycle shift, explains ~93% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.139× (z -12.2) |
| [[SK-MEL-2 (line)]] | alt | 33.2 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.218× (z -11.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.286× (z -9.5) |
| [[SW48 (line)]] | wt | 18.4 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0555× (z -12.8) |
| [[A-427 (line)]] | wt | 43.7 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.129× (z -17.5) ⚠ cell-cycle shift, explains ~95% of this change |
| [[AN3 CA (line)]] | alt | 22.6 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0489× (z -10.1) |
| [[AsPC-1 (line)]] | alt | 14.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.313× (z -8.7) ⚠ cell-cycle shift, explains ~30% of this change |
| [[BT-474 (line)]] | alt | 16.1 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.145× (z -10.0) |
| [[COLO 205 (line)]] | alt | 13.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.109× (z -9.6) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 29.4 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.113× (z -12.6) |
| [[J82 (line)]] | alt | 18.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.375× (z -9.2) ⚠ cell-cycle shift, explains ~30% of this change |
| [[LS 180 (line)]] | wt | 16.9 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.224× (z -9.1) |
| [[NCI-H23 (line)]] | alt | 46.7 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.374× (z -8.9) ⚠ toxic |
| [[NCI-H2347 (line)]] | alt | 11.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.366× (z -9.1) ⚠ cell-cycle shift, explains ~30% of this change |
| [[C-33 A (line)]] | alt | 29.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 25.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 51.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 31.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6160), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C8orf33]] | +0.58 | +0.45 / +0.40 | both halves | 5e-05 |  |
| [[FASTKD2]] | +0.56 | +0.53 / +0.46 | both halves | 2e-05 |  |
| [[ZNF343]] | +0.56 | +0.52 / +0.49 | both halves | 1e-05 |  |
| [[ANGEL2]] | +0.55 | +0.46 / +0.36 | both halves | 1e-04 |  |
| [[ZFR]] | +0.54 | +0.52 / +0.39 | both halves | 5e-05 |  |
| [[MRPL45]] | +0.54 | +0.48 / +0.43 | both halves | 3e-05 |  |
| [[BLTP3B]] | +0.54 | +0.49 / +0.43 | both halves | 3e-05 |  |
| [[PARG]] | +0.53 | +0.43 / +0.45 | both halves | 3e-05 |  |
| [[YARS2]] | +0.53 | +0.43 / +0.43 | both halves | 3e-05 |  |
| [[PSMC2]] | +0.53 | +0.50 / +0.32 | both halves | 2e-04 |  |
| [[WAPL]] | +0.52 | +0.52 / +0.44 | both halves | 3e-05 |  |
| [[FARS2]] | +0.52 | +0.51 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC35B2]] | -0.55 | -0.50 / -0.31 | both halves | 2e-04 |  |
| [[CHKA]] | -0.55 | -0.49 / -0.46 | both halves | 2e-05 |  |
| [[CADM4]] | -0.52 | -0.33 / -0.49 | both halves | 1e-04 |  |
| [[PPP1R13B]] | -0.51 | -0.47 / -0.46 | both halves | 3e-05 |  |
| [[SLC25A25]] | -0.50 | -0.43 / -0.50 | both halves | 4e-05 |  |
| [[EML4]] | -0.50 | -0.42 / -0.45 | both halves | 4e-05 |  |
| [[LIFR]] | -0.49 | -0.39 / -0.34 | both halves | 1e-04 |  |
| [[CNN2]] | -0.48 | -0.32 / -0.45 | both halves | 2e-04 |  |
| [[GMDS]] | -0.48 | -0.40 / -0.41 | both halves | 4e-05 |  |
| [[GDF11]] | -0.47 | -0.39 / -0.37 | both halves | 9e-05 |  |
| [[SPTSSA]] | -0.47 | -0.47 / -0.33 | both halves | 1e-04 |  |
| [[IGFBP2]] | -0.47 | -0.45 / -0.29 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CAMK2N1]] | B | CAMK2N1 activity lowers SMARCAL1's level | lines that do not express CAMK2N1 (8) vs lines expressing it (42) | 1.31× higher at baseline in the lines without CAMK2N1 | 0.074 | ⚠ within organs, on part of the lines; also absent: RPLP0P2; maybe low, not absent |
| [[EPDR1]] | B | EPDR1 activity raises SMARCAL1's level | lines that do not express EPDR1 (14) vs lines expressing it (36) | 1.29× lower at baseline in the lines without EPDR1 | 0.088 | ⚠ within organs, on part of the lines; also absent: RBM24, BEX2, GATA3 |
| [[SEMA3F]] | B | SEMA3F activity raises SMARCAL1's level | lines that do not express SEMA3F (6) vs lines expressing it (44) | 1.12× lower at baseline in the lines without SEMA3F | 0.094 | ⚠ within organs, on part of the lines; also absent: MCM2, PIMREG, GKAP1 |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SMYD5]] | C | SMARCAL1's natural level strengthens SMYD5's drug response | SMARCAL1's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.63, reverse +0.17; direction not clear | 0.076 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **+** arm (projection on the module's main direction 0.449). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-17.9, 18.1); signed map (10.4, -31.5). **Vector** length 64.7, 13.7% of its response variance represented; |z| ≥ 3 in 1,213 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.6 | -2.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +4.4 | -3.2 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +4.3 | +0.2 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.8 | -1.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.4 | +1.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.6 | -2.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.1 | +1.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.8 | +2.0 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -4.4 | -4.6 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.4 | -22.4 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | -3.3 | -11.3 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~27% of this change | -3.3 | -6.3 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | -3.2 | -12.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.4 | -7.8 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.8 | -2.2 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.7 | -3.5 |
|  | [[Cepharanthine (drug)]] 5 µM |  | -1.3 | -0.3 |

## What is on record

|  |  |
|---|---|
| Name | SNF2 related chromatin remodeling annealing helicase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q35 — chr2:216,412,383-216,483,053 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HHARP, HARP |
| Gene groups (HGNC) | SNF2 related family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NZC9](https://www.uniprot.org/uniprotkb/Q9NZC9) (SNF2 related chromatin remodeling annealing helicase 1):

> ATP-dependent annealing helicase that binds selectively to fork DNA relative to ssDNA or dsDNA and catalyzes the rewinding of the stably unwound DNA. Rewinds single-stranded DNA bubbles that are stably bound by replication protein A (RPA). Acts throughout the genome to reanneal stably unwound DNA, performing the opposite reaction of many enzymes, such as helicases and polymerases, that unwind DNA. May play an important role in DNA damage response by acting at stalled replication forks.

**Summary**, from NCBI Gene [50485](https://www.ncbi.nlm.nih.gov/gene/50485):

> The protein encoded by this gene is a member of the SWI/SNF family of proteins. Members of this family have helicase and ATPase activities and are thought to regulate transcription of certain genes by altering the chromatin structure around those genes. The encoded protein shows sequence similarity to the E. coli RNA polymerase-binding protein HepA. Mutations in this gene are a cause of Schimke immunoosseous dysplasia (SIOD), an autosomal recessive disorder with the diagnostic features of …

**Accessions** — [HGNC:11102](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11102) · Entrez [50485](https://www.ncbi.nlm.nih.gov/gene/50485) · UniProt [Q9NZC9](https://www.uniprot.org/uniprotkb/Q9NZC9) · Ensembl [ENSG00000138375](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000138375)

## Data

Gene col 6160: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6160); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6160, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6160]; `tensor/DDL_lfc|DDL_z.npy` [6160]; `embed/gene_vectors.npy` [6160]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6160 or target_col == 6160). Every well: [[SMARCAL1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SMARCAL1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
