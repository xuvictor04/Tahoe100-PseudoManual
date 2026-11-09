---
symbol: "CMIP"
type: "gene"
col: 7740
ensembl_id: "ENSG00000153815"
name: "c-Maf inducing protein"
location: "16q23.2-q23.3"
module: 154
arm: "+"
pooled_cpm: 345.97
n_lines_expressing: 49
n_dd_up: 3
n_dd_down: 16
n_dd_up_clean: 3
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/154"]
generated_by: "tahoemap"
---

# CMIP

*c-Maf inducing protein* — 16q23.2-q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.27× (z +7.5, q 3e-11, up in 32 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (9 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.541× (z -19.6, q 0e+00, down in 42 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SMS]] (+0.64, fdr 1e-05), [[EXT1]] (+0.63, fdr 1e-05), [[EHD4]] (+0.63, fdr 2e-05); moves opposite to [[DDX59]] (-0.61, fdr 3e-05), [[DNAJC27]] (-0.61, fdr 1e-05), [[ANGEL2]] (-0.61, fdr 3e-05).
> It is in [[Module 154]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 5 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7740.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.27×** | +7.5 | 3e-11 | 32/47 (A-172, SW480, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.25×** | +5.0 | 1e-04 | 26/47 (hTERT-HPNE, RPMI-7951, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.24×** | +4.9 | 2e-04 | 25/47 (Hs 766T, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | 1.18× | +3.8 | 0.024 | 19/46 (NCI-H1573, HT-29, …) | rises with dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | 1.18× | +3.7 | 0.024 | 21/47 (NCI-H1573, HT-29, …) | rises with dose |  |
| [[Sivelestat (sodium tetrahydrate) (drug)]] 5 µM |  | 1.19× | +3.7 | 0.024 | 19/48 (RKO, HEC-1-A, …) | top dose only | plate-row cell shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +3.6 | 0.031 | 21/47 (hTERT-HPNE, SW480, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.15× | +3.2 | 0.092 | 16/47 (AsPC-1, HT-29, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~11% of this change | 1.15× | +3.2 | 0.092 | 19/48 (HOP62, A498, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 11 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7740.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.541×** | -19.6 | 0e+00 | 42/48 (PANC-1, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.586×** | -11.6 | 2e-28 | 33/43 (SW480, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.603×** | -11.0 | 9e-26 | 39/46 (HepG2/C3A, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.633×** | -10.3 | 1e-22 | 32/48 (COLO 205, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.692×** | -8.0 | 1e-13 | 34/46 (PANC-1, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.693×** | -8.0 | 2e-13 | 34/47 (NCI-H2030, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.708×** | -7.5 | 6e-12 | 31/47 (HOP62, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.743×** | -6.7 | 1e-09 | 30/47 (PANC-1, A549, …) | two highest doses | cell-cycle shift (explains ~10% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.750×** | -6.2 | 3e-08 | 34/49 (HOP62, HS-578T, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.728×** | -6.1 | 6e-08 | 29/44 (SW480, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~12% of this change | **0.789×** | -5.3 | 5e-06 | 30/47 (A549, PANC-1, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **0.795×** | -5.2 | 1e-05 | 24/47 (HepG2/C3A, PANC-1, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.854× | -5.0 | 2e-05 | 20/47 (HOP62, A-172, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | 0.855× | -5.0 | 2e-05 | 19/47 (CFPAC-1, PANC-1, …) | two highest doses | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~27% of this change | **0.801×** | -5.0 | 2e-05 | 27/47 (PANC-1, KATO III, …) | inconsistent across doses | low cells (technical?) |
| [[Ponatinib (drug)]] 5 µM |  | **0.819×** | -4.5 | 2e-04 | 26/47 (HepG2/C3A, PANC-1, …) | inconsistent across doses |  |
| [[Budesonide (drug)]] 0.05 µM |  | **0.829×** | -4.2 | 7e-04 | 23/47 (NCI-H460, HOP62, …) | inconsistent across doses |  |
| [[Dexamethasone (drug)]] 5 µM |  | 0.845× | -3.8 | 0.004 | 19/47 (NCI-H460, HOP62, …) | rises with dose |  |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | 0.865× | -3.3 | 0.030 | 17/47 (NCI-H460, A549, …) | rises with dose |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | 0.872× | -3.1 | 0.052 | 17/47 (A549, NCI-H1792, …) | rises with dose |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | 0.867× | -3.1 | 0.052 | 21/48 (HOP62, NCI-H460, …) | rises with dose |  |
| [[Sulfatinib (drug)]] 5 µM |  | 0.868× | -3.1 | 0.052 | 15/48 (J82, NCI-H1792, …) | top dose only |  |
| [[Amsacrine (drug)]] 5 µM |  | 0.909× | -3.1 | 0.056 | 6/47 (NCI-H2030, PANC-1, …) | top dose only |  |
| [[Radotinib (drug)]] 5 µM |  | 0.915× | -2.9 | 0.095 | 7/47 (LoVo, NCI-H2347, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7740. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 382 | 0 | 15 (10 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.337× (z -24.3) |
| [[MIA PaCa-2 (line)]] | alt | 559 | 0 | 12 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.245× (z -23.5) |
| [[HOP62 (line)]] | alt | 350 | 0 | 8 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.402× (z -19.0) |
| [[KATO III (line)]] | alt | 525 | 2 (1 ⚠) | 6 (4 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.04× (z +9.6) ⚠ unreliable plate only · without an alert: [[Auranofin (drug)]] 5 µM 1.91× (z +8.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.452× (z -15.2) |
| [[NCI-H2030 (line)]] | alt | 1,107 | 0 | 8 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.268× (z -20.2) |
| [[A-172 (line)]] | wt | 297 | 1 | 6 (3 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.51× (z +8.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.496× (z -14.9) |
| [[A549 (line)]] | wt | 763 | 0 | 7 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.317× (z -20.9) |
| [[CFPAC-1 (line)]] | alt | 443 | 0 | 7 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.350× (z -19.9) |
| [[HS-578T (line)]] | alt | 439 | 1 | 6 (3 ⚠) | [[PH-797804 (drug)]] 5 µM 3.71× (z +10.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.391× (z -20.2) |
| [[HepG2_C3A (line)]] | wt | 502 | 0 | 6 (5 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.211× (z -21.7) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.355× (z -21.3) |
| [[LOX-IMVI (line)]] | wt | 213 | 0 | 6 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.545× (z -11.8) |
| [[NCI-H1573 (line)]] | alt | 332 | 3 (2 ⚠) | 3 (3 ⚠) | [[Daptomycin (drug)]] 5 µM 2.60× (z +11.3) ⚠ unreliable plate only · without an alert: [[Peretinoin (drug)]] 5 µM 2.67× (z +11.2) | [[Homoharringtonine (drug)]] 5 µM 0.492× (z -11.9) ⚠ cell-cycle shift, explains ~52% of this change |
| [[NCI-H23 (line)]] | alt | 321 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.253× (z -16.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.475× (z -13.0) |
| [[NCI-H460 (line)]] | wt | 184 | 1 (1 ⚠) | 4 (2 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 1.93× (z +10.1) ⚠ unreliable plate only | [[Harringtonine (drug)]] 5 µM 0.433× (z -12.4) |
| [[COLO 205 (line)]] | alt | 508 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.276× (z -18.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.458× (z -15.5) |
| [[HCT15 (line)]] | alt | 299 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.490× (z -13.0) |
| [[Hs 766T (line)]] | wt | 473 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.476× (z -14.5) |
| [[HT-29 (line)]] | alt | 320 | 1 (1 ⚠) | 3 (2 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.05× (z +10.7) ⚠ unreliable plate only | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.456× (z -11.3) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.654× (z -9.0) |
| [[J82 (line)]] | alt | 236 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.565× (z -11.1) |
| [[RKO (line)]] | wt | 237 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.478× (z -14.0) ⚠ cell-cycle shift, explains ~52% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.428× (z -10.9) |
| [[SW480 (line)]] | alt | 462 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.272× (z -19.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.509× (z -14.9) |
| [[SW1417 (line)]] | alt | 270 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.527× (z -13.4) |
| [[A498 (line)]] | wt | 564 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.458× (z -16.1) |
| [[AsPC-1 (line)]] | alt | 232 | 1 (1 ⚠) | 1 | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.86× (z +12.5) ⚠ unreliable plate only | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.515× (z -11.2) |
| [[BT-474 (line)]] | alt | 158 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.472× (z -12.0) ⚠ cell-cycle shift, explains ~52% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.551× (z -9.5) |
| [[Panc 03.27 (line)]] | alt | 279 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.584× (z -10.3) |
| [[RPMI-7951 (line)]] | alt | 133 | 1 | 1 | [[Panobinostat (drug)]] 5 µM 2.29× (z +8.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.559× (z -8.7) |
| [[SNU-1 (line)]] | wt | 135 | 1 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.35× (z +9.3) ⚠ cell-cycle shift, would explain all of this change | [[Dinaciclib (drug)]] 5 µM 0.423× (z -9.0) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 231 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.507× (z -13.3) |
| [[SW48 (line)]] | wt | 330 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.405× (z -12.0) |
| [[A-427 (line)]] | wt | 559 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.428× (z -10.7) |
| [[C32 (line)]] | wt | 96.5 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.439× (z -8.5) ⚠ cell-cycle shift, explains ~12% of this change |
| [[H4 (line)]] | wt | 192 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.355× (z -10.5) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 229 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.621× (z -11.4) |
| [[hTERT-HPNE (line)]] | wt | 113 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.81× (z +10.4) | — |
| [[LoVo (line)]] | wt | 201 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.555× (z -11.6) |
| [[LS 180 (line)]] | wt | 327 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.443× (z -11.9) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 253 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.468× (z -15.0) |
| [[SK-MEL-2 (line)]] | alt | 154 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.378× (z -11.8) |
| [[SW 900 (line)]] | alt | 197 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.632× (z -8.8) |
| [[AN3 CA (line)]] | alt | 190 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 184 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 98.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 427 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 128 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 274 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 85.2 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 164 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 276 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 225 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7740), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*51 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMS]] | +0.64 | +0.57 / +0.62 | both halves | 1e-05 |  |
| [[EXT1]] | +0.63 | +0.61 / +0.53 | both halves | 1e-05 |  |
| [[EHD4]] | +0.63 | +0.60 / +0.48 | both halves | 2e-05 |  |
| [[CDCP1]] | +0.61 | +0.62 / +0.54 | both halves | 1e-05 |  |
| [[PFKFB3]] | +0.59 | +0.56 / +0.53 | both halves | 1e-05 | same gene group |
| [[EDA]] | +0.59 | +0.44 / +0.46 | both halves | 3e-05 | same gene group |
| [[ZFYVE28]] | +0.58 | +0.53 / +0.43 | both halves | 3e-05 |  |
| [[ADAMTS16]] | +0.58 | +0.51 / +0.50 | both halves | 1e-05 |  |
| [[SHB]] | +0.57 | +0.60 / +0.45 | both halves | 3e-05 |  |
| [[TM4SF1]] | +0.57 | +0.55 / +0.51 | both halves | 1e-05 |  |
| [[PTPRF]] | +0.57 | +0.47 / +0.43 | both halves | 3e-05 |  |
| [[SLC35F3]] | +0.57 | +0.51 / +0.59 | both halves | 1e-05 | same gene group |

## Genes that move opposite

*49 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DDX59]] | -0.61 | -0.47 / -0.46 | both halves | 3e-05 |  |
| [[DNAJC27]] | -0.61 | -0.54 / -0.53 | both halves | 1e-05 |  |
| [[ANGEL2]] | -0.61 | -0.46 / -0.51 | both halves | 3e-05 |  |
| [[WDFY3]] | -0.59 | -0.45 / -0.41 | both halves | 4e-05 |  |
| [[RNF146]] | -0.59 | -0.51 / -0.44 | both halves | 3e-05 |  |
| [[RAB21]] | -0.59 | -0.50 / -0.42 | both halves | 4e-05 |  |
| [[NCOA2]] | -0.58 | -0.47 / -0.46 | both halves | 3e-05 | STRING 441 |
| [[DECR1]] | -0.58 | -0.47 / -0.43 | both halves | 3e-05 |  |
| [[FAM76B]] | -0.57 | -0.46 / -0.59 | both halves | 2e-05 |  |
| [[TP53]] | -0.57 | -0.48 / -0.47 | both halves | 2e-05 |  |
| [[TAPT1]] | -0.57 | -0.53 / -0.48 | both halves | 2e-05 |  |
| [[RAF1]] | -0.57 | -0.41 / -0.45 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers CMIP's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HOXB7]] | B | HOXB7 activity lowers CMIP's level | lines that do not express HOXB7 (7) vs lines expressing it (43) | 1.33× higher at baseline in the lines without HOXB7 | 0.050 | ⚠ within organs, on part of the lines |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 154]]; 29 genes; every member is in the + arm (projection on the module's main direction 0.587). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-1.1, 15.1); signed map (3.1, 45.7). **Vector** length 127, 41.5% of its response variance represented; |z| ≥ 3 in 1,544 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +7.7 | +2.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +7.6 | +7.5 |
|  | [[Panobinostat (drug)]] 5 µM |  | +6.5 | +5.0 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +6.4 | +3.6 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +6.4 | +4.9 |
|  | [[Peretinoin (drug)]] 5 µM |  | +5.5 | +2.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +4.8 | +1.5 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +4.3 | +1.0 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -7.7 | -19.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -6.2 | -11.0 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.7 | -2.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | -5.7 | -4.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -5.5 | -7.5 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -4.0 | -2.7 |
|  | [[Budesonide (drug)]] 0.05 µM |  | -3.7 | -4.2 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -3.7 | -1.6 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -3.5 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | c-Maf inducing protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q23.2-q23.3 — chr16:81,444,808-81,711,762 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | MicroRNA protein coding host genes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IY22](https://www.uniprot.org/uniprotkb/Q8IY22) (C-Maf-inducing protein):

> Plays a role in T-cell signaling pathway. Isoform 2 may play a role in T-helper 2 (Th2) signaling pathway and seems to represent the first proximal signaling protein that links T-cell receptor-mediated signal to the activation of c-Maf Th2 specific factor.

**Summary**, from NCBI Gene [80790](https://www.ncbi.nlm.nih.gov/gene/80790):

> This gene encodes a c-Maf inducing protein that plays a role in T-cell signaling pathway. Alternatively spliced transcript variants encoding different isoforms have been described for this gene. [provided by RefSeq, Aug 2011]

**Accessions** — [HGNC:24319](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24319) · Entrez [80790](https://www.ncbi.nlm.nih.gov/gene/80790) · UniProt [Q8IY22](https://www.uniprot.org/uniprotkb/Q8IY22) · Ensembl [ENSG00000153815](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000153815)

## Data

Gene col 7740: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7740); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7740, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7740]; `tensor/DDL_lfc|DDL_z.npy` [7740]; `embed/gene_vectors.npy` [7740]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7740 or target_col == 7740). Every well: [[CMIP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CMIP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
