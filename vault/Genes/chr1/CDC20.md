---
symbol: "CDC20"
type: "gene"
col: 3902
ensembl_id: "ENSG00000117399"
name: "cell division cycle 20"
location: "1p34.2"
module: 22
arm: "+"
pooled_cpm: 24.31
n_lines_expressing: 47
n_dd_up: 25
n_dd_down: 20
n_dd_up_clean: 12
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 5
direction_downstream: 60
tags: ["gene", "module/022"]
generated_by: "tahoemap"
---

# CDC20

*cell division cycle 20* — 1p34.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (13 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 2.72× (z +9.1, q 5e-17, up in 38 of 45 measured lines) ⚠ cell-cycle shift, explains ~81% of this change. The strongest without an alert is [[Belinostat (drug)]] 5 µM: 1.88× (z +6.0, q 3e-07, up in 29 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (12 with an alert ⚠); the strongest is [[Bortezomib (drug)]] 0.05 µM: 0.448× (z -7.2, q 4e-10, down in 33 of 44 measured lines) ⚠ cell-cycle shift, explains ~67% of this change. The strongest without an alert is [[Amsacrine (drug)]] 5 µM: 0.694× (z -4.9, q 1e-04, down in 29 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PLK1]] (+0.90, fdr 7e-06), [[CCNB1]] (+0.87, fdr 7e-06), [[CDKN3]] (+0.87, fdr 7e-06).
> It is in [[Module 022]], a single-armed module (G2/M checkpoint).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 60 go from it, the strongest it → [[NEURL1B]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 13 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3902.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~81% of this change | **2.72×** | +9.1 | 5e-17 | 38/45 (PANC-1, SW1417, …) | rises with dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~73% of this change | **2.37×** | +8.2 | 6e-14 | 38/42 (HOP62, PANC-1, …) | all doses, flat | low cells (technical?); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.84×** | +8.2 | 6e-14 | 31/44 (SW1417, RKO, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **2.06×** | +6.8 | 1e-09 | 37/44 (RKO, SW1417, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | **1.88×** | +6.0 | 3e-07 | 29/44 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~89% of this change | **1.80×** | +5.6 | 2e-06 | 28/40 (PANC-1, A549, …) | rises with dose | composition shift; position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.77×** | +5.4 | 5e-06 | 30/45 (KATO III, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~72% of this change | **1.77×** | +5.2 | 2e-05 | 21/36 (MIA PaCa-2, A-172, …) | rises with dose | composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~94% of this change | **1.70×** | +5.0 | 4e-05 | 25/44 (RKO, SW1417, …) | all doses, stronger at high dose |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~90% of this change | **1.44×** | +4.9 | 5e-05 | 33/45 (HOP62, MIA PaCa-2, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.64×** | +4.7 | 2e-04 | 25/45 (LoVo, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~71% of this change | **1.64×** | +4.5 | 3e-04 | 27/43 (A-172, Hs 766T, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 0.05 µM |  | **1.55×** | +4.2 | 0.001 | 21/45 (HOP62, HT-29, …) | all doses, flat |  |
| [[Mebendazole (drug)]] 5 µM |  | **1.57×** | +4.1 | 0.002 | 27/45 (SW480, LoVo, …) | rises with dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.53×** | +4.0 | 0.002 | 23/44 (HOP62, NCI-H460, …) | two highest doses |  |
| [[Docetaxel (drug)]] 5 µM |  | **1.30×** | +3.5 | 0.012 | 19/45 (HT-29, HEC-1-A, …) | all doses, flat | position effect removed |
| [[Peretinoin (drug)]] 5 µM |  | **1.44×** | +3.3 | 0.024 | 21/44 (HOP62, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.42×** | +3.3 | 0.024 | 16/44 (HOP62, H4, …) | all doses, stronger at high dose |  |
| [[HI-TOPK-032 (drug)]] 0.5 µM |  | **1.62×** | +3.3 | 0.027 | 20/45 (HOP62, CFPAC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.41×** | +3.3 | 0.027 | 18/43 (HOP62, NCI-H2030, …) | all doses, flat |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.37×** | +3.0 | 0.065 | 14/43 (SW480, SW48, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.25×** | +3.0 | 0.070 | 19/45 (HOP62, RKO, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 12 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3902.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~67% of this change | **0.448×** | -7.2 | 4e-10 | 33/44 (NCI-H2030, LOX-IMVI, …) | all doses, flat | position effect removed |
| [[Cytarabine (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **0.507×** | -6.4 | 3e-08 | 38/44 (NCI-H1573, A-172, …) | all doses, flat |  |
| [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **0.497×** | -6.4 | 4e-08 | 38/44 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **0.555×** | -5.6 | 4e-06 | 26/43 (SW48, LOX-IMVI, …) | inconsistent across doses |  |
| [[Amsacrine (drug)]] 5 µM |  | **0.694×** | -4.9 | 1e-04 | 29/45 (LS 180, LOX-IMVI, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **0.610×** | -4.7 | 3e-04 | 24/44 (LS 180, A498, …) | inconsistent across doses |  |
| [[Cytarabine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~68% of this change | **0.634×** | -4.3 | 0.001 | 25/45 (BT-474, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~99% of this change | **0.651×** | -4.1 | 0.003 | 22/44 (SNU-1, C32, …) | top dose only | position effect removed |
| [[Cytarabine (drug)]] 0.05 µM |  | **0.636×** | -4.0 | 0.005 | 21/44 (NCI-H1573, HOP62, …) | all doses, stronger at high dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.457×** | -3.9 | 0.006 | 23/42 (SHP-77, J82, …) | top dose only | noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.666×** | -3.8 | 0.006 | 24/44 (HCT15, SNU-1, …) | two highest doses |  |
| [[Gemcitabine (drug)]] 0.5 µM |  | **0.688×** | -3.6 | 0.016 | 23/45 (A498, SW48, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Cytarabine (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~68% of this change | **0.677×** | -3.5 | 0.017 | 24/44 (A-427, LS 180, …) | all doses, flat |  |
| [[Gemcitabine (drug)]] 0.05 µM |  | **0.758×** | -3.5 | 0.018 | 23/45 (SHP-77, A-427, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~87% of this change | **0.501×** | -3.4 | 0.024 | 18/40 (A-172, A-427, …) | all doses, flat | noisy plate (z scaled); position effect removed |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | **0.711×** | -3.2 | 0.039 | 14/44 (CHP-212, HS-578T, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.712×** | -3.2 | 0.039 | 17/44 (A-427, C32, …) | inconsistent across doses | position effect removed |
| [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | **0.703×** | -3.1 | 0.058 | 17/44 (A-427, HOP62, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.21 per unit of S-phase module lfc, +1.42 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3902. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LS 180 (line)]] | wt | 22.5 | 0 | 3 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.0961× (z -15.3) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.162× (z -11.9) |
| [[PANC-1 (line)]] | alt | 24.7 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.55× (z +9.2) ⚠ cell-cycle shift, would explain all of this change | — |
| [[SW1417 (line)]] | alt | 32.2 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.60× (z +12.8) ⚠ cell-cycle shift, would explain all of this change | — |
| [[A498 (line)]] | wt | 27.5 | 0 | 2 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.273× (z -12.8) ⚠ cell-cycle shift, would explain all of this change |
| [[H4 (line)]] | wt | 28.2 | 0 | 2 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.154× (z -9.7) ⚠ cell-cycle shift, would explain all of this change |
| [[HOP62 (line)]] | alt | 25.3 | 2 (2 ⚠) | 0 | [[Docetaxel (drug)]] 0.05 µM 7.03× (z +12.6) ⚠ transcription drop; cell-cycle shift, explains ~73% of this change | — |
| [[LOX-IMVI (line)]] | wt | 22.3 | 0 | 2 (2 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM 0.147× (z -9.7) ⚠ cell-cycle shift, explains ~60% of this change |
| [[RKO (line)]] | wt | 23.4 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.49× (z +12.7) ⚠ cell-cycle shift, would explain all of this change | — |
| [[SNU-1 (line)]] | wt | 66.5 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0516× (z -15.8) ⚠ cell-cycle shift, explains ~94% of this change |
| [[SW48 (line)]] | wt | 35.3 | 0 | 2 (1 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM 0.0662× (z -12.7) ⚠ cell-cycle shift, explains ~60% of this change · without an alert: [[Amsacrine (drug)]] 0.5 µM 0.139× (z -9.2) |
| [[A-172 (line)]] | wt | 17.1 | 0 | 1 (1 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM 0.184× (z -8.5) ⚠ cell-cycle shift, explains ~60% of this change |
| [[A549 (line)]] | wt | 20.5 | 0 | 1 (1 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM 0.163× (z -9.2) ⚠ cell-cycle shift, explains ~60% of this change |
| [[AsPC-1 (line)]] | alt | 18.1 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.281× (z -8.8) ⚠ cell-cycle shift, would explain all of this change |
| [[HCT15 (line)]] | alt | 32.6 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 0.5 µM 0.103× (z -9.4) ⚠ cell-cycle shift, would explain all of this change |
| [[HEC-1-A (line)]] | alt | 32.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.65× (z +9.5) ⚠ cell-cycle shift, would explain all of this change | — |
| [[KATO III (line)]] | alt | 16.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.90× (z +10.8) ⚠ cell-cycle shift, would explain all of this change | — |
| [[LoVo (line)]] | wt | 14.8 | 0 | 1 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.220× (z -11.6) |
| [[MIA PaCa-2 (line)]] | alt | 27.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.231× (z -9.0) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H2030 (line)]] | alt | 44.2 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.235× (z -8.9) ⚠ cell-cycle shift, explains ~67% of this change |
| [[Panc 03.27 (line)]] | alt | 33.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.48× (z +10.6) ⚠ cell-cycle shift, would explain all of this change | — |
| [[SHP-77 (line)]] | alt | 33.7 | 0 | 1 | — | [[Bosentan (hydrate) (drug)]] 5 µM 0.213× (z -8.7) |
| [[A-427 (line)]] | wt | 40.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 42.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 29.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.83 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.80 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 4.70 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 37.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 34.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 9.28 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.95 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 8.74 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 27.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 30.0 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 71.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 29.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3902), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PLK1]] | +0.90 | +0.90 / +0.90 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 999 |
| [[CCNB1]] | +0.87 | +0.87 / +0.89 | both halves | 7e-06 | pathway: APC/C-mediated degradation of cell cycle proteins; STRING 999 |
| [[CDKN3]] | +0.87 | +0.84 / +0.86 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 885 |
| [[CCNB2]] | +0.87 | +0.86 / +0.88 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 999 |
| [[NEK2]] | +0.87 | +0.85 / +0.86 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 999 |
| [[KIF20A]] | +0.86 | +0.83 / +0.87 | both halves | 7e-06 | pathway: HALLMARK_ESTROGEN_RESPONSE_LATE; STRING 981 |
| [[DLGAP5]] | +0.86 | +0.81 / +0.87 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 981 |
| [[CCNA2]] | +0.85 | +0.83 / +0.84 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 999 |
| [[CKAP2]] | +0.85 | +0.83 / +0.84 | both halves | 7e-06 | STRING 579 |
| [[BUB1]] | +0.84 | +0.82 / +0.83 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 999 |
| [[KNSTRN]] | +0.84 | +0.86 / +0.85 | both halves | 7e-06 | STRING 562 |
| [[TROAP]] | +0.84 | +0.79 / +0.84 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 827 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 3, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises CDC20's level | compounds that target TOP2A: 4 of 5 lower it (Amsacrine, Doxorubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.4% of all compounds | 0.015 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[NEURL1B]] | B | NEURL1B activity raises CDC20's level | lines that do not express NEURL1B (7) vs lines expressing it (43) | 1.97× lower at baseline in the lines without NEURL1B | 0.077 | ⚠ within organs, on part of the lines; also absent: PIMREG, WNT9A, ENSG00000267131 |
| [[HYLS1]] | B | HYLS1 activity raises CDC20's level | lines that do not express HYLS1 (5) vs lines expressing it (45) | 2.12× lower at baseline in the lines without HYLS1 | 0.084 | ⚠ within organs, on part of the lines; also absent: DNAJB5, PPP2R3A, CEP170; maybe low, not absent |
| [[PIMREG]] | C | PIMREG activity raises CDC20's level | lines that do not express PIMREG (6) vs lines expressing it (44) | 2.45× lower at baseline in the lines without PIMREG | 0.032 | ⚠ within organs, on part of the lines; also absent: PBK, AURKB, ENSG00000197332; maybe low, not absent; co-absent with the target |
| [[AURKB]] | C | AURKB activity raises CDC20's level | lines that do not express AURKB (4) vs lines expressing it (46) | 2.54× lower at baseline in the lines without AURKB | 0.090 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TCF19, SMARCD3, CDC45; maybe low, not absent |

### Downstream of this gene

*60 arrows, 60 of them with an alert ⚠; grade A 0, B 0, C 60. Shown: the 12 strongest; 48 more arrows (48 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NEURL1B]] | C | CDC20 activity raises NEURL1B's level | lines that do not express CDC20 (3) vs lines expressing it (47) | 3.80× lower at baseline in the lines without CDC20 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: SPDL1, ARHGAP10, CDC45; maybe low, not absent; its own permutation p |
| [[AURKB]] | C | CDC20 activity raises AURKB's level | lines that do not express CDC20 (3) vs lines expressing it (47) | 3.40× lower at baseline in the lines without CDC20 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: SPDL1, ARHGAP10, CDC45; maybe low, not absent; its own permutation p |
| [[CENPF]] | C | CDC20 activity raises CENPF's level | lines that do not express CDC20 (3) vs lines expressing it (47) | 3.21× lower at baseline in the lines without CDC20 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: SPDL1, ARHGAP10, CDC45; maybe low, not absent; its own permutation p |
| [[CEP55]] | C | CDC20 activity raises CEP55's level | lines that do not express CDC20 (3) vs lines expressing it (47) | 3.21× lower at baseline in the lines without CDC20 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: SPDL1, ARHGAP10, CDC45; maybe low, not absent; co-absent with the target; its own permutation p |
| [[ANLN]] | C | CDC20 activity raises ANLN's level | lines that do not express CDC20 (3) vs lines expressing it (47) | 3.18× lower at baseline in the lines without CDC20 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: SPDL1, ARHGAP10, CDC45; maybe low, not absent; its own permutation p |
| [[SHCBP1]] | C | CDC20 activity raises SHCBP1's level | lines that do not express CDC20 (3) vs lines expressing it (47) | 3.15× lower at baseline in the lines without CDC20 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: SPDL1, ARHGAP10, CDC45; maybe low, not absent; its own permutation p |
| [[KIF20A]] | C | CDC20 activity raises KIF20A's level | lines that do not express CDC20 (3) vs lines expressing it (47) | 3.06× lower at baseline in the lines without CDC20 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: SPDL1, ARHGAP10, CDC45; maybe low, not absent; its own permutation p |
| [[NDC80]] | C | CDC20 activity raises NDC80's level | lines that do not express CDC20 (3) vs lines expressing it (47) | 3.04× lower at baseline in the lines without CDC20 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: SPDL1, ARHGAP10, CDC45; maybe low, not absent; its own permutation p |
| [[SPDL1]] | C | CDC20 activity raises SPDL1's level | lines that do not express CDC20 (3) vs lines expressing it (47) | 3.01× lower at baseline in the lines without CDC20 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: SPDL1, ARHGAP10, CDC45; maybe low, not absent; co-absent with the target; its own permutation p |
| [[KIF18B]] | C | CDC20 activity raises KIF18B's level | lines that do not express CDC20 (3) vs lines expressing it (47) | 2.98× lower at baseline in the lines without CDC20 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: SPDL1, ARHGAP10, CDC45; maybe low, not absent; its own permutation p |
| [[CCNB1]] | C | CDC20 activity raises CCNB1's level | lines that do not express CDC20 (3) vs lines expressing it (47) | 2.76× lower at baseline in the lines without CDC20 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: SPDL1, ARHGAP10, CDC45; maybe low, not absent; its own permutation p |
| [[UBE2S]] | C | CDC20 activity raises UBE2S's level | lines that do not express CDC20 (3) vs lines expressing it (47) | 2.72× lower at baseline in the lines without CDC20 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: SPDL1, ARHGAP10, CDC45; maybe low, not absent; its own permutation p |

## Where it sits

- **Module**: [[Module 022]] — G2/M checkpoint; 185 genes; every member is in the + arm (projection on the module's main direction 0.826). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-37.5, -57.5); signed map (-51.3, -42.9). **Vector** length 130, 43.5% of its response variance represented; |z| ≥ 3 in 1,287 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *mitotic spindle* (hallmark, mean cos +0.66 to 38); *G2/M Transition* (reactome, mean cos +0.64 to 28); *Mitotic G2-G2/M phases* (reactome, mean cos +0.64 to 28).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~81% of this change | +7.5 | +9.1 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~73% of this change | +6.6 | +8.2 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +5.8 | +8.2 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | +5.0 | +6.8 |
|  | [[Belinostat (drug)]] 5 µM |  | +3.7 | +6.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.2 | +3.0 |
|  | [[Docetaxel (drug)]] 5 µM |  | +3.2 | +3.5 |
|  | [[Vinblastine (sulfate) (drug)]] 0.05 µM |  | +3.2 | +4.2 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +2.8 | +3.3 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.8 | +3.3 |
| fall | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~99% of this change | -6.9 | -4.1 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~67% of this change | -6.3 | -7.2 |
|  | [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | -6.0 | -6.4 |
|  | [[Cytarabine (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~55% of this change | -5.6 | -6.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~57% of this change | -5.0 | -4.7 |
|  | [[Amsacrine (drug)]] 5 µM |  | -4.4 | -4.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.3 | -1.1 |
|  | [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | -3.9 | -3.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.6 | -1.3 |
|  | [[Gemcitabine (drug)]] 0.05 µM |  | -3.3 | -3.5 |

## What is on record

|  |  |
|---|---|
| Name | cell division cycle 20 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p34.2 — chr1:43,358,981-43,363,203 (+) |
| Ensembl biotype | protein_coding |
| Also known as | p55CDC, CDC20A |
| Gene groups (HGNC) | WD repeat domain containing |
| Hallmark sets | ESTROGEN_RESPONSE_LATE, G2M_CHECKPOINT, E2F_TARGETS, MYC_TARGETS_V1 |
| Reactome | 38 pathways, smallest: Phosphorylation of Emi1; Conversion from APC/C:Cdc20 to APC/C:Cdh1 in late anaphase; Inactivation of APC/C via direct inhibition of the APC/C complex |
| Matched by | ensembl_id |

**Function**, from UniProt [Q12834](https://www.uniprot.org/uniprotkb/Q12834) (Cell division cycle protein 20 homolog):

> Substrate-specific adapter and activator of the anaphase promoting complex/cyclosome (APC/C) that confers substrate specificity by binding to substrates and targeting them to the APC/C for ubiquitination and degradation. Essential for activating APC/C in the metaphase/anaphase transition of the cell cycle, targeting the degradation of cyclin B and securin. Recognizes and binds the destruction box (D box), KEB box and ABBA motifs on protein substrates. The CDC20-APC/C complex positively …

**Summary**, from NCBI Gene [991](https://www.ncbi.nlm.nih.gov/gene/991):

> CDC20 appears to act as a regulatory protein interacting with several other proteins at multiple points in the cell cycle. It is required for two microtubule-dependent processes, nuclear movement prior to anaphase and chromosome separation. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:1723](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1723) · Entrez [991](https://www.ncbi.nlm.nih.gov/gene/991) · UniProt [Q12834](https://www.uniprot.org/uniprotkb/Q12834) · Ensembl [ENSG00000117399](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000117399)

## Data

Gene col 3902: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3902); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3902, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3902]; `tensor/DDL_lfc|DDL_z.npy` [3902]; `embed/gene_vectors.npy` [3902]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3902 or target_col == 3902). Every well: [[CDC20 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CDC20.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
