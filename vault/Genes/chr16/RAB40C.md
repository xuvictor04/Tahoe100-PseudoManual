---
symbol: "RAB40C"
type: "gene"
col: 12417
ensembl_id: "ENSG00000197562"
name: "RAB40C, member RAS oncogene family"
location: "16p13.3"
module: 3
arm: "+"
pooled_cpm: 55.72
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 25
n_dd_up_clean: 2
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# RAB40C

*RAB40C, member RAS oncogene family* — 16p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 1.44× (z +4.9, q 6e-04, up in 25 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ipatasertib (drug)]] 0.5 µM: 1.57× (z +4.3, q 0.005, up in 29 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[Digitoxin (drug)]] 5 µM in 2 lines (LS 180 3.01×, PANC-1 3.04×; ⚠ toxic; transcription drop); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (LS 180 2.97×); [[Homoharringtonine (drug)]] 5 µM in 1 line (KATO III 2.41×); [[Panobinostat (drug)]] 5 µM in 1 line (SW480 2.48×).
> Pooled over the cell lines (median), lowered significantly by 25 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.323× (z -15.0, q 0e+00, down in 40 of 47 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Harringtonine (drug)]] 5 µM: 0.422× (z -11.0, q 7e-26, down in 40 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CBFA2T2]] (+0.76, fdr 7e-06), [[FAM193B]] (+0.74, fdr 7e-06), [[SDHAP2]] (+0.73, fdr 7e-06); moves opposite to [[ZNF655]] (-0.70, fdr 7e-06), [[KRT8P12]] (-0.70, fdr 7e-06), [[TRIM44]] (-0.69, fdr 7e-06).
> It sits in the **+** arm of [[Module 003]] (mRNA 3'-end processing).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[DEPP1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12417.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[Digitoxin (drug)]] 5 µM in 2 lines (LS 180 3.01×, PANC-1 3.04×; ⚠ toxic; transcription drop); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (LS 180 2.97×); [[Homoharringtonine (drug)]] 5 µM in 1 line (KATO III 2.41×); [[Panobinostat (drug)]] 5 µM in 1 line (SW480 2.48×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.44×** | +4.9 | 6e-04 | 25/48 (LS 180, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.57×** | +4.3 | 0.005 | 29/47 (A498, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM |  | **1.36×** | +4.1 | 0.007 | 28/48 (SW480, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | 1.28× | +3.3 | 0.13 | 19/48 (KATO III, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Radotinib (drug)]] 5 µM |  | 1.18× | +3.2 | 0.16 | 17/48 (AsPC-1, PANC-1, …) | top dose only |  |
| [[Fumaric acid (drug)]] 5 µM |  | 1.26× | +3.0 | 0.22 | 17/49 (HT-29, SHP-77, …) | top dose only | plate-row cell shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 8 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 25 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12417.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.323×** | -15.0 | 0e+00 | 40/47 (A-172, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.325×** | -14.3 | 6e-44 | 34/39 (MIA PaCa-2, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.359×** | -12.5 | 9e-34 | 38/43 (HT-29, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.422×** | -11.0 | 7e-26 | 40/48 (A549, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **0.609×** | -9.2 | 3e-18 | 38/48 (NCI-H2347, HS-578T, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~2% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.557×** | -7.7 | 1e-12 | 36/48 (A549, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.656×** | -5.5 | 2e-06 | 30/47 (A-172, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.750×** | -5.3 | 7e-06 | 25/48 (A-172, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belumosudil (drug)]] 5 µM |  | **0.677×** | -4.9 | 5e-05 | 33/48 (A549, SHP-77, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.773×** | -4.8 | 1e-04 | 29/48 (RPMI-7951, A-172, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.708×** | -4.5 | 3e-04 | 31/48 (CFPAC-1, PANC-1, …) | two highest doses |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.710×** | -4.5 | 3e-04 | 28/49 (J82, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.711×** | -4.5 | 3e-04 | 31/48 (NCI-H1792, PANC-1, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.721×** | -4.3 | 7e-04 | 25/48 (A-172, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~29% of this change | **0.729×** | -4.0 | 0.002 | 24/45 (CFPAC-1, NCI-H2347, …) | two highest doses |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.742×** | -3.9 | 0.003 | 30/48 (A498, SW 900, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.811×** | -3.9 | 0.004 | 27/48 (A-172, HS-578T, …) | top dose only |  |
| [[Megestrol (drug)]] 0.05 µM |  | **0.746×** | -3.8 | 0.004 | 28/48 (A498, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~5% here) |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | **0.748×** | -3.8 | 0.004 | 24/49 (Hs 766T, A498, …) | inconsistent across doses |  |
| [[Busulfan (drug)]] 0.05 µM |  | **0.775×** | -3.3 | 0.022 | 22/49 (A498, HS-578T, …) | inconsistent across doses |  |
| [[Berbamine (drug)]] 0.05 µM |  | **0.788×** | -3.1 | 0.044 | 21/48 (A498, SW 1271, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.24 per unit of S-phase module lfc, +0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12417. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 91.9 | 0 | 9 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.161× (z -23.6) |
| [[HS-578T (line)]] | alt | 80.6 | 0 | 8 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.115× (z -14.4) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.119× (z -14.2) |
| [[PANC-1 (line)]] | alt | 86.6 | 1 (1 ⚠) | 7 (3 ⚠) | [[Digitoxin (drug)]] 5 µM 3.04× (z +9.1) ⚠ toxic; transcription drop | [[Harringtonine (drug)]] 5 µM 0.189× (z -13.0) |
| [[A498 (line)]] | wt | 73.2 | 0 | 7 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0947× (z -18.8) |
| [[A549 (line)]] | wt | 64.0 | 0 | 7 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0923× (z -20.6) |
| [[CFPAC-1 (line)]] | alt | 67.4 | 0 | 7 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.109× (z -16.8) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.235× (z -11.4) |
| [[SW 900 (line)]] | alt | 97.2 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0989× (z -15.5) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.226× (z -9.9) |
| [[C32 (line)]] | wt | 47.4 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.115× (z -16.7) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.211× (z -11.5) |
| [[Hs 766T (line)]] | wt | 73.6 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.120× (z -15.4) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.261× (z -9.8) |
| [[HT-29 (line)]] | alt | 89.9 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.137× (z -15.3) ⚠ toxic; transcription drop · without an alert: [[Selinexor (drug)]] 5 µM 0.426× (z -10.0) |
| [[hTERT-HPNE (line)]] | wt | 57.5 | 0 | 5 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.123× (z -13.5) |
| [[NCI-H1792 (line)]] | alt | 77.7 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0833× (z -19.4) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.200× (z -12.5) |
| [[NCI-H2347 (line)]] | alt | 50.4 | 0 | 5 (3 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.310× (z -13.3) |
| [[AsPC-1 (line)]] | alt | 74.7 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.264× (z -9.9) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.274× (z -9.6) |
| [[HCT15 (line)]] | alt | 104 | 0 | 4 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.231× (z -11.4) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.449× (z -8.8) |
| [[HEC-1-A (line)]] | alt | 43.8 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.196× (z -13.9) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 83.8 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.170× (z -10.7) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.215× (z -9.3) |
| [[KATO III (line)]] | alt | 44.8 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.41× (z +9.2) | [[Dinaciclib (drug)]] 5 µM 0.0775× (z -18.1) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 54.2 | 2 (1 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 3.01× (z +9.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.97× (z +9.6) | [[Dinaciclib (drug)]] 5 µM 0.320× (z -9.4) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 47.3 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.154× (z -14.8) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.158× (z -14.6) |
| [[SK-MEL-2 (line)]] | alt | 49.1 | 1 (1 ⚠) | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.08× (z +8.5) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 5 µM 0.253× (z -10.7) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 115 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0807× (z -12.6) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 29.2 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.128× (z -11.3) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.187× (z -8.9) |
| [[MIA PaCa-2 (line)]] | alt | 35.1 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0755× (z -19.7) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.253× (z -10.5) |
| [[NCI-H23 (line)]] | alt | 30.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.193× (z -11.3) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 36.0 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.205× (z -11.0) |
| [[SNU-1 (line)]] | wt | 34.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.109× (z -12.1) |
| [[SNU-423 (line)]] | alt | 45.6 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.165× (z -12.4) |
| [[A-427 (line)]] | wt | 33.3 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.286× (z -9.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[C-33 A (line)]] | alt | 44.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.112× (z -15.6) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 45.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.327× (z -9.2) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 41.1 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.223× (z -11.2) |
| [[NCI-H2030 (line)]] | alt | 35.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.239× (z -11.1) ⚠ toxic; transcription drop |
| [[NCI-H596 (line)]] | alt | 69.8 | 0 | 1 | — | [[Methylthiouracil (drug)]] 0.05 µM 0.133× (z -23.5) |
| [[RPMI-7951 (line)]] | alt | 41.1 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.266× (z -8.7) |
| [[SHP-77 (line)]] | alt | 86.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.291× (z -8.6) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 50.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.279× (z -10.7) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 31.3 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.48× (z +8.7) | — |
| [[AN3 CA (line)]] | alt | 45.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 47.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 30.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 32.7 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 42.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 96.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 40.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 26.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 62.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 30.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 64.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12417), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CBFA2T2]] | +0.76 | +0.77 / +0.68 | both halves | 7e-06 |  |
| [[FAM193B]] | +0.74 | +0.79 / +0.68 | both halves | 7e-06 |  |
| [[SDHAP2]] | +0.73 | +0.74 / +0.67 | both halves | 7e-06 |  |
| [[ANG]] | +0.73 | +0.71 / +0.71 | both halves | 7e-06 |  |
| [[STK32C]] | +0.73 | +0.62 / +0.67 | both halves | 7e-06 |  |
| [[ULK1]] | +0.72 | +0.67 / +0.69 | both halves | 7e-06 |  |
| [[ALKBH7]] | +0.72 | +0.66 / +0.70 | both halves | 7e-06 |  |
| [[LIN7B]] | +0.72 | +0.56 / +0.67 | both halves | 1e-05 |  |
| [[MPND]] | +0.72 | +0.59 / +0.67 | both halves | 7e-06 |  |
| [[MALSU1]] | +0.72 | +0.67 / +0.60 | both halves | 7e-06 |  |
| [[PLEKHH3]] | +0.72 | +0.70 / +0.63 | both halves | 7e-06 |  |
| [[TRIM62]] | +0.71 | +0.57 / +0.69 | both halves | 1e-05 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF655]] | -0.70 | -0.59 / -0.65 | both halves | 7e-06 |  |
| [[KRT8P12]] | -0.70 | -0.68 / -0.61 | both halves | 7e-06 |  |
| [[TRIM44]] | -0.69 | -0.63 / -0.65 | both halves | 7e-06 |  |
| [[ZNF300]] | -0.68 | -0.45 / -0.69 | both halves | 3e-05 |  |
| [[GMFB]] | -0.68 | -0.48 / -0.78 | both halves | 2e-05 |  |
| [[DARS2]] | -0.67 | -0.62 / -0.58 | both halves | 7e-06 |  |
| [[PTPN11]] | -0.66 | -0.66 / -0.67 | both halves | 7e-06 |  |
| [[NCR3LG1]] | -0.66 | -0.59 / -0.57 | both halves | 9e-06 |  |
| [[ZNF121]] | -0.66 | -0.59 / -0.66 | both halves | 7e-06 |  |
| [[TASOR]] | -0.66 | -0.66 / -0.54 | both halves | 1e-05 |  |
| [[UTP20]] | -0.65 | -0.63 / -0.60 | both halves | 7e-06 |  |
| [[RBM12]] | -0.65 | -0.56 / -0.66 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DEPP1]] | B | DEPP1 activity raises RAB40C's level | lines that do not express DEPP1 (21) vs lines expressing it (29) | 1.42× lower at baseline in the lines without DEPP1 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with SMARCA4; also absent: LOX, TNFAIP2, BST2 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **+** arm (projection on the module's main direction 0.815). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (0.9, -14.0); signed map (-29.0, 12.0). **Vector** length 144, 46.7% of its response variance represented; |z| ≥ 3 in 1,119 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM |  | +6.7 | +4.1 |
|  | [[Belinostat (drug)]] 5 µM |  | +6.3 | +3.3 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +6.2 | +3.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +5.7 | +4.3 |
|  | [[Radotinib (drug)]] 5 µM |  | +4.4 | +3.2 |
|  | [[Binimetinib (drug)]] 5 µM |  | +3.2 | +1.5 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +3.0 | +2.6 |
|  | [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | +3.0 | +2.1 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -9.6 | -11.0 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -9.0 | -7.7 |
|  | [[Selinexor (drug)]] 5 µM |  | -8.7 | -9.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -6.9 | -12.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -6.8 | -5.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -4.1 | -2.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.1 | -4.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.0 | -4.8 |
|  | [[Busulfan (drug)]] 0.05 µM |  | -3.8 | -3.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.8 | -4.9 |

## What is on record

|  |  |
|---|---|
| Name | RAB40C, member RAS oncogene family |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p13.3 — chr16:589,357-629,272 (+) |
| Ensembl biotype | protein_coding |
| Also known as | RARL; previously RASL8C |
| Gene groups (HGNC) | RAB, member RAS oncogene GTPases |
| Hallmark sets | P53_PATHWAY |
| Reactome | 1 pathways, smallest: RAB geranylgeranylation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96S21](https://www.uniprot.org/uniprotkb/Q96S21) (Ras-related protein Rab-40C):

> RAB40C small GTPase acts as substrate-recognition component of the ECS(RAB40C) E3 ubiquitin ligase complex which mediates the ubiquitination and subsequent proteasomal degradation of target proteins. The Rab40 subfamily belongs to the Rab family that are key regulators of intracellular membrane trafficking, from the formation of transport vesicles to their fusion with membranes. Rabs cycle between an inactive GDP-bound form and an active GTP-bound form that is able to recruit to membranes …

**Summary**, from NCBI Gene [57799](https://www.ncbi.nlm.nih.gov/gene/57799):

> Enables G protein activity and ubiquitin-like ligase-substrate adaptor activity. Involved in several processes, including lipid droplet formation; negative regulation of focal adhesion assembly; and proteasome-mediated ubiquitin-dependent protein catabolic process. Located in Golgi membrane; cytosol; and lipid droplet. Part of Cul5-RING ubiquitin ligase complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:18285](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18285) · Entrez [57799](https://www.ncbi.nlm.nih.gov/gene/57799) · UniProt [Q96S21](https://www.uniprot.org/uniprotkb/Q96S21) · Ensembl [ENSG00000197562](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000197562)

## Data

Gene col 12417: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12417); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12417, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12417]; `tensor/DDL_lfc|DDL_z.npy` [12417]; `embed/gene_vectors.npy` [12417]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12417 or target_col == 12417). Every well: [[RAB40C — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RAB40C.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
