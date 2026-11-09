---
symbol: "GPSM2"
type: "gene"
col: 4309
ensembl_id: "ENSG00000121957"
name: "G protein signaling modulator 2"
location: "1p13.3"
module: 22
arm: "+"
pooled_cpm: 70.85
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 33
n_dd_up_clean: 8
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 9
direction_downstream: 0
tags: ["gene", "module/022"]
generated_by: "tahoemap"
---

# GPSM2

*G protein signaling modulator 2* — 1p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (3 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 1.78× (z +12.1, q 7e-31, up in 40 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 33 drug-doses (16 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.510× (z -19.7, q 0e+00, down in 44 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CCNF]] (+0.87, fdr 7e-06), [[PSRC1]] (+0.84, fdr 7e-06), [[NEK2]] (+0.84, fdr 7e-06).
> It is in [[Module 022]], a single-armed module (G2/M checkpoint).
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 6 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4309.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **1.78×** | +12.1 | 7e-31 | 40/48 (NCI-H460, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.71×** | +11.2 | 2e-26 | 38/48 (NCI-H460, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.62×** | +10.0 | 2e-21 | 39/48 (A498, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.35×** | +8.9 | 1e-16 | 31/48 (HEC-1-A, RKO, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.49×** | +8.3 | 1e-14 | 34/48 (A498, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.89×** | +7.0 | 3e-10 | 36/48 (J82, RKO, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.37×** | +6.5 | 6e-09 | 29/48 (RKO, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~73% of this change | **1.78×** | +6.3 | 2e-08 | 28/47 (MIA PaCa-2, NCI-H23, …) | top dose only | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~64% of this change | **1.26×** | +4.8 | 9e-05 | 21/48 (NCI-H23, PANC-1, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.22×** | +4.3 | 0.001 | 20/48 (HepG2/C3A, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~67% of this change | **1.22×** | +4.2 | 0.001 | 20/47 (NCI-H23, PANC-1, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~80% of this change | 1.18× | +3.4 | 0.031 | 12/48 (HT-29, HEC-1-A, …) | inconsistent across doses |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | 1.17× | +3.3 | 0.045 | 8/48 (HOP62, H4, …) | rises with dose |  |
| [[Ixazomib (drug)]] 0.05 µM |  | 1.18× | +3.2 | 0.050 | 6/47 (NCI-H1792, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Tofacitinib (drug)]] 5 µM |  | 1.11× | +3.2 | 0.050 | 10/48 (MIA PaCa-2, SHP-77, …) | all doses, flat |  |
| [[Tofacitinib (drug)]] 0.05 µM |  | 1.16× | +3.2 | 0.053 | 3/48 (MIA PaCa-2, PANC-1, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 52 in all, 19 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 33 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4309.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.510×** | -19.7 | 0e+00 | 44/47 (SW480, LS 180, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.575×** | -16.2 | 0e+00 | 40/48 (A-172, HS-578T, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Auranofin (drug)]] 5 µM |  | **0.560×** | -12.0 | 5e-31 | 39/48 (C32, HEC-1-A, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.553×** | -11.8 | 5e-30 | 45/48 (SW480, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.672×** | -11.6 | 4e-29 | 38/48 (A-427, A498, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.592×** | -10.9 | 2e-25 | 37/48 (SNU-1, H4, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.609×** | -10.3 | 8e-23 | 39/48 (HEC-1-A, HOP62, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.617×** | -10.0 | 9e-22 | 41/48 (A498, LS 180, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.629×** | -9.6 | 5e-20 | 35/48 (SW480, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.643×** | -8.8 | 8e-17 | 39/48 (HEC-1-A, SNU-1, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.661×** | -8.6 | 5e-16 | 32/48 (NCI-H1792, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.656×** | -8.3 | 7e-15 | 32/48 (MIA PaCa-2, LS 180, …) | all doses, flat |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.694×** | -7.6 | 2e-12 | 31/47 (C32, SW1417, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.692×** | -7.3 | 9e-12 | 32/48 (HS-578T, NCI-H2030, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.708×** | -7.2 | 3e-11 | 31/48 (HEC-1-A, HOP62, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.746×** | -5.8 | 1e-07 | 27/48 (NCI-H460, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Amsacrine (drug)]] 5 µM |  | **0.832×** | -5.3 | 2e-06 | 26/48 (A498, HS-578T, …) | rises with dose |  |
| [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | **0.796×** | -4.4 | 3e-04 | 21/48 (HEC-1-A, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | 0.839× | -3.6 | 0.006 | 14/48 (RPMI-7951, HOP62, …) | all doses, flat |  |
| [[Temsirolimus (drug)]] 0.5 µM |  | 0.844× | -3.5 | 0.009 | 20/48 (Hs 766T, LOX-IMVI, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.28 per unit of S-phase module lfc, +0.64 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4309. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LS 180 (line)]] | wt | 139 | 0 | 7 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.237× (z -17.0) |
| [[HEC-1-A (line)]] | alt | 97.2 | 0 | 6 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.378× (z -16.6) |
| [[HOP62 (line)]] | alt | 51.3 | 0 | 6 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.397× (z -13.4) ⚠ cell-cycle shift, explains ~44% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.353× (z -10.2) |
| [[A498 (line)]] | wt | 50.0 | 1 | 4 (2 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.43× (z +8.5) | [[Selinexor (drug)]] 5 µM 0.384× (z -13.0) ⚠ cell-cycle shift, explains ~44% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.327× (z -10.7) |
| [[C32 (line)]] | wt | 63.9 | 0 | 5 (2 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.204× (z -12.5) |
| [[SW480 (line)]] | alt | 104 | 0 | 5 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.345× (z -17.2) |
| [[LoVo (line)]] | wt | 77.2 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.415× (z -14.3) |
| [[NCI-H460 (line)]] | wt | 57.4 | 2 | 2 (1 ⚠) | [[Belinostat (drug)]] 5 µM 2.07× (z +8.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.467× (z -12.8) |
| [[SK-MEL-2 (line)]] | alt | 111 | 0 | 4 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.370× (z -12.0) ⚠ cell-cycle shift, explains ~44% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.334× (z -9.3) |
| [[SNU-1 (line)]] | wt | 80.2 | 0 | 4 (3 ⚠) | — | [[Selinexor (drug)]] 0.5 µM 0.176× (z -10.3) ⚠ cell-cycle shift, explains ~50% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.214× (z -8.8) |
| [[H4 (line)]] | wt | 66.9 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.250× (z -12.3) |
| [[HS-578T (line)]] | alt | 87.3 | 0 | 3 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.344× (z -13.4) ⚠ cell-cycle shift, explains ~44% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.415× (z -11.0) |
| [[A-427 (line)]] | wt | 48.6 | 0 | 2 (1 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.391× (z -11.8) |
| [[HCT15 (line)]] | alt | 151 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.365× (z -12.5) |
| [[hTERT-HPNE (line)]] | wt | 58.6 | 0 | 2 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.388× (z -9.1) ⚠ cell-cycle shift, explains ~44% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.254× (z -8.9) |
| [[KATO III (line)]] | alt | 67.2 | 2 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.09× (z +11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 82.4 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.330× (z -13.4) |
| [[NCI-H2030 (line)]] | alt | 49.2 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.478× (z -9.5) |
| [[NCI-H2347 (line)]] | alt | 73.9 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.496× (z -10.8) |
| [[RPMI-7951 (line)]] | alt | 124 | 0 | 2 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.252× (z -11.0) |
| [[SHP-77 (line)]] | alt | 96.2 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.217× (z -12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.389× (z -11.2) |
| [[A-172 (line)]] | wt | 46.1 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.300× (z -13.7) ⚠ cell-cycle shift, explains ~44% of this change |
| [[A549 (line)]] | wt | 48.9 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.398× (z -10.8) ⚠ cell-cycle shift, explains ~44% of this change |
| [[AN3 CA (line)]] | alt | 110 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.257× (z -11.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[CFPAC-1 (line)]] | alt | 56.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.438× (z -10.8) |
| [[Hs 766T (line)]] | wt | 80.6 | 0 | 1 | — | [[Futibatinib (drug)]] 5 µM 0.0565× (z -12.4) |
| [[HT-29 (line)]] | alt | 61.9 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.465× (z -8.6) ⚠ cell-cycle shift, explains ~44% of this change |
| [[J82 (line)]] | alt | 66.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.488× (z -10.7) |
| [[NCI-H1792 (line)]] | alt | 49.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.148× (z -15.3) |
| [[NCI-H23 (line)]] | alt | 106 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.497× (z -8.8) ⚠ cell-cycle shift, explains ~44% of this change |
| [[Panc 03.27 (line)]] | alt | 52.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +10.4) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[PANC-1 (line)]] | alt | 62.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.524× (z -10.7) |
| [[RKO (line)]] | wt | 35.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.07× (z +10.7) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[SW 900 (line)]] | alt | 85.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.339× (z -11.9) |
| [[SW1417 (line)]] | alt | 156 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.291× (z -15.4) |
| [[SW48 (line)]] | wt | 70.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.390× (z -8.7) |
| [[AsPC-1 (line)]] | alt | 49.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 38.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 79.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 21.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 24.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 54.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 34.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 42.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 50.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 75.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 52.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 82.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 59.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4309), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCNF]] | +0.87 | +0.85 / +0.82 | both halves | 7e-06 | **novel candidate** |
| [[PSRC1]] | +0.84 | +0.84 / +0.75 | both halves | 7e-06 | **novel candidate** |
| [[NEK2]] | +0.84 | +0.79 / +0.85 | both halves | 7e-06 |  |
| [[DLGAP5]] | +0.83 | +0.81 / +0.86 | both halves | 7e-06 |  |
| [[NEURL1B]] | +0.83 | +0.80 / +0.77 | both halves | 7e-06 |  |
| [[NUF2]] | +0.82 | +0.78 / +0.83 | both halves | 7e-06 |  |
| [[TOP2A]] | +0.82 | +0.78 / +0.83 | both halves | 7e-06 |  |
| [[CIT]] | +0.82 | +0.79 / +0.79 | both halves | 7e-06 |  |
| [[CDKN3]] | +0.81 | +0.64 / +0.85 | both halves | 7e-06 |  |
| [[PRR11]] | +0.81 | +0.80 / +0.80 | both halves | 7e-06 |  |
| [[PTTG1]] | +0.80 | +0.78 / +0.78 | both halves | 7e-06 |  |
| [[DEPDC1B]] | +0.80 | +0.77 / +0.85 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 6, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises GPSM2's level | compounds that target TOP2A: 5 of 5 lower it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 5.0% of all compounds | 0.005 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[PIMREG]] | B | PIMREG activity raises GPSM2's level | lines that do not express PIMREG (6) vs lines expressing it (44) | 1.81× lower at baseline in the lines without PIMREG | 0.020 | ⚠ within organs, on part of the lines; also absent: PBK, AURKB, ENSG00000197332; maybe low, not absent |
| [[NEURL1B]] | B | NEURL1B activity raises GPSM2's level | lines that do not express NEURL1B (7) vs lines expressing it (43) | 1.70× lower at baseline in the lines without NEURL1B | 0.038 | ⚠ within organs, on part of the lines; also absent: PIMREG, WNT9A, ENSG00000267131 |
| [[NEURL1B]] | B | NEURL1B activity strengthens GPSM2's drug response | lines that do not express NEURL1B (7) vs lines expressing it (41) | the lines without NEURL1B respond 0.72× as strongly (z diff +1.36); strongest at Idarubicin (hydrochloride) 5 µM: 0.79x vs 0.45x (z diff +5.6) | 0.045 | ⚠ within organs, on part of the lines; also absent: PIMREG, WNT9A, ENSG00000267131; target measured in part of the lines; artifact flags |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers GPSM2's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity lowers GPSM2's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[PBK]] | C | PBK activity raises GPSM2's level | lines that do not express PBK (4) vs lines expressing it (46) | 2.08× lower at baseline in the lines without PBK | 0.030 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SPDL1, SMARCD3, NCS1; maybe low, not absent |
| [[ACBD7]] | C | ACBD7 activity raises GPSM2's level | lines that do not express ACBD7 (4) vs lines expressing it (46) | 1.32× lower at baseline in the lines without ACBD7 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ENSG00000197332, LRP3, PHGDH; maybe low, not absent; its own permutation p |
| [[CDCA3]] | C | CDCA3 activity raises GPSM2's level | lines that do not express CDCA3 (3) vs lines expressing it (47) | 2.09× lower at baseline in the lines without CDCA3 | 0.097 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: TBC1D19, PBK, SNPH; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 022]] — G2/M checkpoint; 185 genes; every member is in the + arm (projection on the module's main direction 0.773). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-35.4, -58.0); signed map (-50.5, -39.9). **Vector** length 159, 54.6% of its response variance represented; |z| ≥ 3 in 1,543 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *G2/M checkpoint* (hallmark, mean cos +0.62 to 60); *DREAM G2/M down* (control, mean cos +0.71 to 28); *Mitotic Prometaphase* (reactome, mean cos +0.58 to 48).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM |  | +8.9 | +12.1 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +8.5 | +8.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +7.8 | +8.9 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +7.5 | +10.0 |
|  | [[Panobinostat (drug)]] 5 µM |  | +7.4 | +11.2 |
|  | [[Brivudine (drug)]] 5 µM |  | +6.6 | +7.0 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +3.7 | +2.4 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | +2.8 | +2.8 |
|  | [[Mebendazole (drug)]] 5 µM |  | +2.6 | +2.4 |
| fall | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -10.2 | -11.6 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | -10.0 | -16.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -9.2 | -19.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -7.9 | -11.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -7.8 | -12.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -6.5 | -10.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -5.5 | -7.2 |
|  | [[Amsacrine (drug)]] 5 µM |  | -5.2 | -5.3 |

## What is on record

|  |  |
|---|---|
| Name | G protein signaling modulator 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p13.3 — chr1:108,875,350-108,934,545 (+) |
| Ensembl biotype | protein_coding |
| Also known as | LGN, Pins; previously DFNB82 |
| Gene groups (HGNC) | Tetratricopeptide repeat domain containing |
| Reactome | 3 pathways, smallest: G alpha (i) signalling events; GPCR downstream signalling; Signaling by GPCR |
| Matched by | ensembl_id |

**Function**, from UniProt [P81274](https://www.uniprot.org/uniprotkb/P81274) (G protein-signaling modulator 2):

> Plays an important role in mitotic spindle pole organization via its interaction with NUMA1. Required for cortical dynein-dynactin complex recruitment during metaphase. Plays a role in metaphase spindle orientation. Also plays an important role in asymmetric cell divisions. Has guanine nucleotide dissociation inhibitor (GDI) activity towards G(i) alpha proteins, such as GNAI1 and GNAI3, and thereby regulates their activity (By similarity).

**Summary**, from NCBI Gene [29899](https://www.ncbi.nlm.nih.gov/gene/29899):

> The protein encoded by this gene belongs to a family of proteins that modulate activation of G proteins, which transduce extracellular signals received by cell surface receptors into integrated cellular responses. The N-terminal half of this protein contains 10 copies of leu-gly-asn (LGN) repeat, and the C-terminal half contains 4 GoLoco motifs, which are involved in guanine nucleotide exchange. This protein may play a role in neuroblast division and in the development of normal hearing. …

**Accessions** — [HGNC:29501](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29501) · Entrez [29899](https://www.ncbi.nlm.nih.gov/gene/29899) · UniProt [P81274](https://www.uniprot.org/uniprotkb/P81274) · Ensembl [ENSG00000121957](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000121957)

## Data

Gene col 4309: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4309); `tables/drug_effects.parquet` (69 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4309, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4309]; `tensor/DDL_lfc|DDL_z.npy` [4309]; `embed/gene_vectors.npy` [4309]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4309 or target_col == 4309). Every well: [[GPSM2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GPSM2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
