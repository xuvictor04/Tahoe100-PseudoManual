---
symbol: "TSNARE1"
type: "gene"
col: 10043
ensembl_id: "ENSG00000171045"
name: "t-SNARE domain containing 1"
location: "8q24.3"
module: 33
arm: "+"
pooled_cpm: 40.09
n_lines_expressing: 50
n_dd_up: 0
n_dd_down: 39
n_dd_up_clean: 0
n_dd_down_clean: 21
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/033"]
generated_by: "tahoemap"
---

# TSNARE1

*t-SNARE domain containing 1* — 8q24.3

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (NCI-H1792 3.75×, HS-578T 2.41×; ⚠ cell-cycle shift, explains ~98% of this change).
> Pooled over the cell lines (median), lowered significantly by 39 drug-doses (18 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.426× (z -21.6, q 0e+00, down in 46 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DCAF4]] (+0.68, fdr 1e-05), [[CARMIL2]] (+0.61, fdr 2e-05), [[TFAP4]] (+0.61, fdr 7e-06); moves opposite to [[FKBP3]] (-0.58, fdr 4e-05), [[SNHG31]] (-0.50, fdr 1e-04), [[RO60]] (-0.50, fdr 4e-05).
> It sits in the **+** arm of [[Module 033]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 2 with an alert ⚠. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10043.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (NCI-H1792 3.75×, HS-578T 2.41×; ⚠ cell-cycle shift, explains ~98% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Hydroxyfasudil (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.21× | +3.5 | 0.22 | 12/48 (NCI-H1573, NCI-H23, …) | inconsistent across doses |  |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~62% of this change | 1.22× | +3.4 | 0.22 | 13/48 (NCI-H460, NCI-H1573, …) | inconsistent across doses |  |
| [[Rifaximin (drug)]] 5 µM |  | 1.20× | +3.2 | 0.26 | 11/47 (AsPC-1, SW480, …) | rises with dose | position effect removed |
| [[ULK-101 (drug)]] 0.05 µM |  | 1.20× | +3.1 | 0.29 | 13/48 (Hs 766T, NCI-H1573, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | 1.18× | +3.0 | 0.29 | 9/48 (NCI-H2347, LS 180, …) | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 49 in all, 22 with an alert ⚠; shown: the 15 strongest and the 11 next strongest without an alert. 39 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 18 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10043.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.426×** | -21.6 | 0e+00 | 46/48 (Hs 766T, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **0.410×** | -15.9 | 0e+00 | 41/46 (RKO, A-427, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **0.441×** | -14.6 | 0e+00 | 44/46 (PANC-1, SW480, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.453×** | -13.6 | 4e-40 | 36/48 (A498, SW480, …) | rises with dose | composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.479×** | -13.2 | 2e-37 | 44/48 (PANC-1, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | **0.501×** | -11.9 | 1e-30 | 29/40 (MIA PaCa-2, SHP-77, …) | all doses, stronger at high dose | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.528×** | -11.0 | 5e-26 | 34/46 (RPMI-7951, NCI-H23, …) | top dose only | cell-cycle shift (explains ~21% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.565×** | -9.8 | 7e-21 | 38/48 (C-33 A, A-172, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **0.557×** | -9.7 | 2e-20 | 35/45 (MIA PaCa-2, HEC-1-A, …) | all doses, stronger at high dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~33% of this change | **0.570×** | -9.7 | 3e-20 | 36/47 (C32, PANC-1, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.612×** | -8.8 | 1e-16 | 35/48 (C32, A498, …) | rises with dose | cell-cycle shift (explains ~19% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.649×** | -7.7 | 5e-13 | 35/48 (PANC-1, NCI-H23, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.649×** | -7.7 | 5e-13 | 34/48 (A-427, A498, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.651×** | -7.7 | 8e-13 | 33/47 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.742×** | -7.5 | 2e-12 | 30/48 (HEC-1-A, SW1417, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **0.690×** | -6.6 | 1e-09 | 28/48 (C32, LoVo, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.694×** | -6.5 | 2e-09 | 23/47 (MIA PaCa-2, C32, …) | rises with dose | cell-cycle shift (explains ~19% here); position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **0.782×** | -6.2 | 2e-08 | 23/48 (RKO, HEC-1-A, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.579×** | -5.1 | 9e-06 | 27/48 (A498, HS-578T, …) | rises with dose | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.621×** | -4.5 | 2e-04 | 24/46 (PANC-1, A498, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.635×** | -4.2 | 5e-04 | 24/47 (A498, Panc 03.27, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.726×** | -4.1 | 1e-03 | 18/48 (A498, LoVo, …) | rises with dose | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.807×** | -3.8 | 0.003 | 23/48 (A498, NCI-H1573, …) | rises with dose |  |
| [[venetoclax (drug)]] 5 µM |  | **0.669×** | -3.8 | 0.003 | 18/46 (A498, A549, …) | top dose only | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.823×** | -3.5 | 0.010 | 20/47 (NCI-H1573, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[EX229 (drug)]] 0.5 µM |  | **0.762×** | -3.5 | 0.010 | 16/48 (PANC-1, A498, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.35 per unit of S-phase module lfc, -0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10043. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 33.8 | 0 | 13 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.342× (z -16.2) ⚠ cell-cycle shift, explains ~98% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.431× (z -12.7) |
| [[MIA PaCa-2 (line)]] | alt | 48.0 | 0 | 11 (7 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0526× (z -24.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0729× (z -22.3) |
| [[SW480 (line)]] | alt | 53.1 | 0 | 11 (8 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.240× (z -15.5) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.419× (z -14.0) |
| [[C32 (line)]] | wt | 50.7 | 0 | 10 (6 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.136× (z -16.4) |
| [[HEC-1-A (line)]] | alt | 59.3 | 0 | 10 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.157× (z -15.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.361× (z -13.3) |
| [[HS-578T (line)]] | alt | 35.5 | 1 (1 ⚠) | 7 (6 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.41× (z +10.4) ⚠ cell-cycle shift, explains ~98% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.213× (z -18.2) |
| [[A549 (line)]] | wt | 46.4 | 0 | 7 (5 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.219× (z -13.4) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.325× (z -10.3) |
| [[LOX-IMVI (line)]] | wt | 44.7 | 0 | 7 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.220× (z -13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.300× (z -10.1) |
| [[HOP62 (line)]] | alt | 44.5 | 0 | 6 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.363× (z -12.7) |
| [[NCI-H23 (line)]] | alt | 50.3 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.154× (z -17.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.287× (z -11.0) |
| [[NCI-H460 (line)]] | wt | 23.8 | 0 | 6 (4 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.299× (z -11.3) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.330× (z -10.7) |
| [[RKO (line)]] | wt | 119 | 0 | 6 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0838× (z -24.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change · without an alert: [[Selinexor (drug)]] 5 µM 0.422× (z -12.1) |
| [[SNU-423 (line)]] | alt | 35.6 | 0 | 6 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.315× (z -13.5) |
| [[A-427 (line)]] | wt | 43.4 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.115× (z -19.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.351× (z -9.2) |
| [[A498 (line)]] | wt | 36.7 | 0 | 5 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.196× (z -15.8) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.254× (z -13.8) |
| [[SW48 (line)]] | wt | 62.7 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.103× (z -14.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.244× (z -9.6) |
| [[NCI-H1573 (line)]] | alt | 22.9 | 0 | 4 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.166× (z -12.6) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.347× (z -10.5) |
| [[NCI-H2030 (line)]] | alt | 39.9 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.277× (z -15.9) |
| [[Panc 03.27 (line)]] | alt | 42.3 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.284× (z -15.3) |
| [[SW1417 (line)]] | alt | 67.8 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.334× (z -16.6) |
| [[A-172 (line)]] | wt | 27.6 | 0 | 3 (2 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.172× (z -12.9) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.364× (z -10.9) |
| [[C-33 A (line)]] | alt | 39.6 | 0 | 3 (2 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.110× (z -13.4) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.284× (z -11.2) |
| [[LoVo (line)]] | wt | 31.8 | 0 | 3 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.296× (z -12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[RPMI-7951 (line)]] | alt | 34.9 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.178× (z -15.4) |
| [[Hs 766T (line)]] | wt | 36.4 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.108× (z -23.3) |
| [[hTERT-HPNE (line)]] | wt | 19.9 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.142× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[LS 180 (line)]] | wt | 44.1 | 0 | 2 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.268× (z -10.5) ⚠ cell-cycle shift, explains ~35% of this change |
| [[SHP-77 (line)]] | alt | 59.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.144× (z -16.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change |
| [[SK-MEL-2 (line)]] | alt | 55.6 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.389× (z -11.3) |
| [[AN3 CA (line)]] | alt | 46.4 | 0 | 1 (1 ⚠) | — | [[Pimozide (drug)]] 0.5 µM 0.153× (z -8.6) ⚠ transcription drop |
| [[AsPC-1 (line)]] | alt | 27.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.435× (z -9.0) |
| [[CHP-212 (line)]] | wt | 41.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.102× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change |
| [[COLO 205 (line)]] | alt | 39.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.197× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change |
| [[H4 (line)]] | wt | 22.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.268× (z -9.2) |
| [[HCT15 (line)]] | alt | 38.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.365× (z -9.5) |
| [[J82 (line)]] | alt | 28.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.235× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change |
| [[KATO III (line)]] | alt | 35.4 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.327× (z -8.6) ⚠ toxic |
| [[NCI-H1792 (line)]] | alt | 25.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.75× (z +14.1) ⚠ cell-cycle shift, explains ~98% of this change | — |
| [[NCI-H2347 (line)]] | alt | 27.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.416× (z -10.4) |
| [[SNU-1 (line)]] | wt | 42.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.204× (z -14.5) |
| [[SW 900 (line)]] | alt | 24.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.332× (z -11.2) |
| [[BT-474 (line)]] | alt | 63.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 40.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 33.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 35.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 40.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 24.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10043), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DCAF4]] | +0.68 | +0.57 / +0.60 | both halves | 1e-05 |  |
| [[CARMIL2]] | +0.61 | +0.48 / +0.52 | both halves | 2e-05 |  |
| [[TFAP4]] | +0.61 | +0.60 / +0.69 | both halves | 7e-06 |  |
| [[GRAMD4]] | +0.60 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[EXOSC5]] | +0.58 | +0.42 / +0.55 | both halves | 4e-05 |  |
| [[BRF1]] | +0.57 | +0.40 / +0.54 | both halves | 5e-05 |  |
| [[COQ8A]] | +0.56 | +0.46 / +0.55 | both halves | 3e-05 |  |
| [[NLE1]] | +0.55 | +0.45 / +0.44 | both halves | 3e-05 |  |
| [[ST6GALNAC6]] | +0.54 | +0.52 / +0.42 | both halves | 4e-05 |  |
| [[PKN1]] | +0.54 | +0.52 / +0.38 | both halves | 7e-05 |  |
| [[CAMKK1]] | +0.54 | +0.48 / +0.41 | both halves | 4e-05 |  |
| [[SNHG17]] | +0.53 | +0.49 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FKBP3]] | -0.58 | -0.50 / -0.42 | both halves | 4e-05 |  |
| [[SNHG31]] | -0.50 | -0.41 / -0.34 | both halves | 1e-04 |  |
| [[RO60]] | -0.50 | -0.42 / -0.47 | both halves | 4e-05 |  |
| [[DECR1]] | -0.49 | -0.42 / -0.23 | both halves | 5e-04 |  |
| [[RAB27A]] | -0.48 | -0.26 / -0.44 | both halves | 4e-04 |  |
| [[NXT2]] | -0.46 | -0.39 / -0.29 | both halves | 3e-04 |  |
| [[SCYL3]] | -0.46 | -0.40 / -0.21 | both halves | 6e-04 |  |
| [[PNISR-AS1]] | -0.45 | -0.24 / -0.25 | both halves | 5e-04 |  |
| [[EFCAB5]] | -0.45 | -0.29 / -0.18 | ⚠ not reproduced | 9e-04 |  |
| [[MEIS2]] | -0.45 | -0.33 / -0.37 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises TSNARE1's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 8.1% of all compounds | 0.075 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 033]] — MYC targets v2; 139 genes; this gene is in the **+** arm (projection on the module's main direction 0.523). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-12.1, -44.6); signed map (-40.2, -5.1). **Vector** length 86.0, 21.4% of its response variance represented; |z| ≥ 3 in 1,242 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +3.5 | -1.3 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | +3.0 | -2.7 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~98% of this change | +2.9 | -6.6 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +2.6 | +1.5 |
|  | [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~62% of this change | +2.4 | +3.4 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.3 | -0.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.2 | +1.3 |
|  | [[ULK-101 (drug)]] 0.05 µM |  | +1.9 | +3.1 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | +1.8 | +1.0 |
| fall | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -7.0 | -11.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | -6.1 | -9.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -5.4 | -7.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -4.0 | -21.6 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | -3.7 | -7.7 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.7 | -4.5 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -2.7 | -4.1 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.3 | -5.1 |
|  | [[Berbamine (drug)]] 0.05 µM |  | -2.2 | -3.4 |

## What is on record

|  |  |
|---|---|
| Name | t-SNARE domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q24.3 — chr8:142,212,080-142,403,182 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ31164 |
| Matched by | ensembl_id |

UniProt [Q96NA8](https://www.uniprot.org/uniprotkb/Q96NA8) carries no function annotation.

**Summary**, from NCBI Gene [203062](https://www.ncbi.nlm.nih.gov/gene/203062):

> Predicted to enable SNAP receptor activity and SNARE binding activity. Predicted to be involved in intracellular protein transport; vesicle docking; and vesicle fusion. Predicted to be located in membrane. Predicted to be part of SNARE complex. Predicted to be active in synaptic vesicle. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:26437](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26437) · Entrez [203062](https://www.ncbi.nlm.nih.gov/gene/203062) · UniProt [Q96NA8](https://www.uniprot.org/uniprotkb/Q96NA8) · Ensembl [ENSG00000171045](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000171045)

## Data

Gene col 10043: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10043); `tables/drug_effects.parquet` (54 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10043, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10043]; `tensor/DDL_lfc|DDL_z.npy` [10043]; `embed/gene_vectors.npy` [10043]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10043 or target_col == 10043). Every well: [[TSNARE1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TSNARE1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
