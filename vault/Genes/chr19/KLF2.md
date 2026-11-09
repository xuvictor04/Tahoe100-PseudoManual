---
symbol: "KLF2"
type: "gene"
col: 4819
ensembl_id: "ENSG00000127528"
name: "KLF transcription factor 2"
location: "19p13.11"
module: 123
arm: "+"
pooled_cpm: 9.67
n_lines_expressing: 47
n_dd_up: 19
n_dd_down: 23
n_dd_up_clean: 16
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/123"]
generated_by: "tahoemap"
---

# KLF2

*KLF transcription factor 2* — 19p13.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (3 with an alert ⚠); the strongest is [[Pitavastatin (Calcium) (drug)]] 5 µM: 5.19× (z +10.9, q 9e-25, up in 40 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.289× (z -12.0, q 1e-30, down in 34 of 42 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RHOB]] (+0.77, fdr 7e-06), [[EZR]] (+0.73, fdr 7e-06), [[JUND]] (+0.73, fdr 7e-06); moves opposite to [[ZCCHC4]] (-0.68, fdr 3e-05), [[NAXD]] (-0.62, fdr 2e-05), [[METTL3]] (-0.61, fdr 1e-05).
> It is in [[Module 123]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); 1 goes from it, the strongest it → [[AFDN]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 3 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4819.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **5.19×** | +10.9 | 9e-25 | 40/40 (HS-578T, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **4.17×** | +9.2 | 1e-17 | 38/43 (LS 180, SW480, …) | all doses, stronger at high dose | low cells (technical?); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **2.26×** | +7.9 | 5e-13 | 33/42 (Panc 03.27, NCI-H2347, …) | rises with dose | composition shift |
| [[Neratinib (drug)]] 5 µM |  | **3.11×** | +7.8 | 1e-12 | 37/44 (SHP-77, HOP62, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **2.43×** | +5.9 | 5e-07 | 23/43 (SNU-1, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~25% here); composition shift |
| [[Neratinib (maleate) (drug)]] 0.5 µM |  | **2.30×** | +5.7 | 1e-06 | 30/41 (HCT15, SHP-77, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **1.79×** | +5.6 | 1e-06 | 29/45 (HCT15, LOX-IMVI, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **2.15×** | +5.3 | 1e-05 | 28/44 (NCI-H460, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Pitavastatin (Calcium) (drug)]] 0.05 µM |  | **2.18×** | +4.9 | 5e-05 | 28/41 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose | position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **1.86×** | +4.3 | 0.001 | 21/44 (C-33 A, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Neratinib (drug)]] 0.5 µM |  | **1.72×** | +3.7 | 0.009 | 20/44 (NCI-H2347, CFPAC-1, …) | rises with dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.65×** | +3.6 | 0.015 | 21/45 (HS-578T, HOP62, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.58×** | +3.5 | 0.018 | 22/44 (HS-578T, LOX-IMVI, …) | two highest doses | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.44×** | +3.5 | 0.018 | 19/45 (MIA PaCa-2, SW480, …) | top dose only |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.66×** | +3.5 | 0.019 | 20/44 (Panc 03.27, SW480, …) | inconsistent across doses | position effect removed |
| [[Rapamycin (drug)]] 5 µM |  | **1.41×** | +3.3 | 0.030 | 14/45 (SW480, SHP-77, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4819.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.289×** | -12.0 | 1e-30 | 34/42 (AsPC-1, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.290×** | -8.5 | 6e-15 | 38/44 (MIA PaCa-2, SK-MEL-2, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.328×** | -7.4 | 4e-11 | 29/38 (NCI-H2347, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.337×** | -7.2 | 1e-10 | 30/39 (NCI-H460, SNU-1, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.428×** | -5.8 | 6e-07 | 26/42 (SNU-1, NCI-H460, …) | top dose only |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **0.429×** | -5.8 | 6e-07 | 33/44 (LS 180, LoVo, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.586×** | -5.2 | 2e-05 | 30/45 (SNU-1, NCI-H2347, …) | top dose only | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~39% of this change | **0.469×** | -5.0 | 4e-05 | 25/34 (SNU-1, LS 180, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.625×** | -4.6 | 3e-04 | 23/44 (NCI-H2030, AsPC-1, …) | rises with dose | low cells (technical?) |
| [[NG25 (drug)]] 5 µM |  | **0.293×** | -4.4 | 6e-04 | 23/36 (MIA PaCa-2, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.540×** | -4.2 | 0.001 | 22/44 (H4, LS 180, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.552×** | -4.1 | 0.002 | 22/43 (SW480, A-427, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.559×** | -3.8 | 0.007 | 18/40 (LoVo, RKO, …) | inconsistent across doses | cell-cycle shift (explains ~22% here) |
| [[Ponatinib (drug)]] 5 µM |  | **0.581×** | -3.7 | 0.008 | 18/43 (SNU-1, HT-29, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.582×** | -3.7 | 0.008 | 20/44 (BT-474, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.377×** | -3.5 | 0.016 | 13/41 (MIA PaCa-2, SW1417, …) | rises with dose | noisy plate (z scaled); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.612×** | -3.4 | 0.023 | 21/43 (LoVo, A549, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.613×** | -3.4 | 0.023 | 13/44 (NCI-H460, MIA PaCa-2, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.397×** | -3.3 | 0.026 | 17/38 (SW 900, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.67 per unit of S-phase module lfc, +0.61 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4819. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SNU-1 (line)]] | wt | 80.3 | 3 (2 ⚠) | 6 (2 ⚠) | [[Harringtonine (drug)]] 5 µM 7.57× (z +12.2) | [[Auranofin (drug)]] 5 µM 0.0977× (z -14.5) |
| [[LoVo (line)]] | wt | 19.8 | 0 | 7 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0704× (z -13.2) |
| [[MIA PaCa-2 (line)]] | alt | 23.6 | 0 | 6 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.128× (z -15.3) |
| [[NCI-H460 (line)]] | wt | 19.0 | 0 | 6 (2 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.0710× (z -13.9) |
| [[BT-474 (line)]] | alt | 10.0 | 0 | 3 | — | [[Digitoxin (drug)]] 0.5 µM 0.0312× (z -12.5) |
| [[LS 180 (line)]] | wt | 13.1 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.142× (z -11.5) |
| [[NCI-H2347 (line)]] | alt | 7.80 | 1 (1 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 5.33× (z +9.9) ⚠ cell-cycle shift, explains ~39% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.160× (z -10.9) |
| [[AsPC-1 (line)]] | alt | 16.6 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0615× (z -17.5) |
| [[Panc 03.27 (line)]] | alt | 13.4 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 6.46× (z +11.0) ⚠ cell-cycle shift, explains ~39% of this change | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0891× (z -9.6) |
| [[SK-MEL-2 (line)]] | alt | 15.3 | 0 | 2 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0756× (z -10.5) ⚠ unreliable plate only · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.204× (z -9.1) |
| [[A549 (line)]] | wt | 7.63 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0809× (z -8.8) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 17.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0978× (z -12.0) |
| [[HS-578T (line)]] | alt | 6.90 | 1 | 0 | [[Pitavastatin (Calcium) (drug)]] 5 µM 14.1× (z +8.5) | — |
| [[hTERT-HPNE (line)]] | wt | 10.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.87× (z +8.5) ⚠ cell-cycle shift, explains ~39% of this change | — |
| [[NCI-H2030 (line)]] | alt | 19.1 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.262× (z -8.8) ⚠ cell-cycle shift, explains ~32% of this change |
| [[SW 900 (line)]] | alt | 8.34 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.123× (z -9.8) |
| [[SW480 (line)]] | alt | 6.92 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.229× (z -8.7) |
| [[A-172 (line)]] | wt | 12.6 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 8.27 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.83 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.95 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 9.70 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.54 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.30 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.01 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.44 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.13 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.74 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.10 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.97 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.14 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.48 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.90 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.58 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 6.66 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.79 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.17 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.66 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.03 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.93 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.97 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4819), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*45 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RHOB]] | +0.77 | +0.75 / +0.77 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB; STRING 401 |
| [[EZR]] | +0.73 | +0.67 / +0.68 | both halves | 7e-06 |  |
| [[JUND]] | +0.73 | +0.64 / +0.75 | both halves | 7e-06 | STRING 482 |
| [[LMNA]] | +0.67 | +0.63 / +0.68 | both halves | 7e-06 |  |
| [[TUBB2B]] | +0.63 | +0.52 / +0.53 | both halves | 1e-05 |  |
| [[TUBB2A]] | +0.61 | +0.54 / +0.66 | both halves | 1e-05 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[DLGAP4]] | +0.60 | +0.38 / +0.59 | both halves | 6e-05 |  |
| [[CRIP2]] | +0.57 | +0.41 / +0.54 | both halves | 4e-05 |  |
| [[SPAG9]] | +0.57 | +0.35 / +0.46 | both halves | 1e-04 |  |
| [[TUFT1]] | +0.57 | +0.53 / +0.44 | both halves | 3e-05 |  |
| [[JUN]] | +0.57 | +0.59 / +0.57 | both halves | 9e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB; STRING 720 |
| [[DHRS2]] | +0.57 | +0.43 / +0.39 | both halves | 5e-05 |  |

## Genes that move opposite

*55 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZCCHC4]] | -0.68 | -0.46 / -0.71 | both halves | 3e-05 |  |
| [[NAXD]] | -0.62 | -0.50 / -0.48 | both halves | 2e-05 |  |
| [[METTL3]] | -0.61 | -0.49 / -0.57 | both halves | 1e-05 |  |
| [[FBXO22]] | -0.58 | -0.40 / -0.48 | both halves | 4e-05 |  |
| [[TMEM68]] | -0.58 | -0.38 / -0.51 | both halves | 6e-05 |  |
| [[NAF1]] | -0.58 | -0.49 / -0.41 | both halves | 4e-05 |  |
| [[CIAO2A]] | -0.57 | -0.50 / -0.41 | both halves | 4e-05 |  |
| [[NIPBL-DT]] | -0.57 | -0.47 / -0.29 | both halves | 3e-04 |  |
| [[HSPA14]] | -0.56 | -0.44 / -0.45 | both halves | 3e-05 |  |
| [[LY6G5B]] | -0.56 | -0.45 / -0.48 | both halves | 3e-05 |  |
| [[UQCC1]] | -0.56 | -0.29 / -0.57 | both halves | 3e-04 |  |
| [[METTL4]] | -0.56 | -0.41 / -0.38 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises KLF2's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.8% of all compounds | 0.028 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[AFDN]] | C | KLF2 activity lowers AFDN's level | lines that do not express KLF2 (3) vs lines expressing it (47) | 2.46× higher at baseline in the lines without KLF2 | 0.070 | ⚠ few lines (3 vs 47); across organs; also absent: LEKR1, CBR3, DPP7; maybe low, not absent |

## Where it sits

- **Module**: [[Module 123]] — TNF-alpha signaling via NF-kB; 40 genes; every member is in the + arm (projection on the module's main direction 0.704). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (22.3, -0.1); signed map (-0.2, 22.8). **Vector** length 112, 27.5% of its response variance represented; |z| ≥ 3 in 1,189 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | +8.0 | +7.9 |
|  | [[Harringtonine (drug)]] 5 µM |  | +5.8 | +5.9 |
|  | [[Panobinostat (drug)]] 5 µM |  | +5.1 | +5.3 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +5.0 | +3.3 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM |  | +4.7 | +10.9 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +4.1 | +9.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.8 | +3.5 |
|  | [[Binimetinib (drug)]] 5 µM |  | +2.8 | +3.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.5 | +3.5 |
|  | [[Entrectinib (drug)]] 5 µM |  | +2.2 | +1.6 |
| fall | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -7.3 | -7.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -6.0 | -12.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -5.9 | -7.2 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | -5.0 | -4.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.8 | -8.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.7 | -5.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.5 | -5.8 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -2.7 | -3.3 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -2.7 | -2.9 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.6 | -3.5 |

## What is on record

|  |  |
|---|---|
| Name | KLF transcription factor 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.11 — chr19:16,324,826-16,328,685 (+) |
| Ensembl biotype | protein_coding |
| Also known as | LKLF |
| Gene groups (HGNC) | Zinc fingers C2H2-type; KLF transcription factors |
| Hallmark sets | TNFA_SIGNALING_VIA_NFKB |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y5W3](https://www.uniprot.org/uniprotkb/Q9Y5W3) (Krueppel-like factor 2):

> Transcription factor that binds to the CACCC box in the promoter of target genes such as HBB/beta globin or NOV and activates their transcription. Might be involved in transcriptional regulation by modulating the binding of the RARA nuclear receptor to RARE DNA elements.

**Summary**, from NCBI Gene [10365](https://www.ncbi.nlm.nih.gov/gene/10365):

> This gene encodes a protein that belongs to the Kruppel family of transcription factors. The encoded zinc finger protein is expressed early in mammalian development and is found in many different cell types. The protein acts to bind the CACCC box found in the promoter of target genes to activate their transcription. It plays a role in many processes during development and disease including adipogenesis, embryonic erythropoiesis, epithelial integrity, inflammation and t-cell viability. [provided …

**Accessions** — [HGNC:6347](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6347) · Entrez [10365](https://www.ncbi.nlm.nih.gov/gene/10365) · UniProt [Q9Y5W3](https://www.uniprot.org/uniprotkb/Q9Y5W3) · Ensembl [ENSG00000127528](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000127528)

## Data

Gene col 4819: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4819); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4819, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4819]; `tensor/DDL_lfc|DDL_z.npy` [4819]; `embed/gene_vectors.npy` [4819]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4819 or target_col == 4819). Every well: [[KLF2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KLF2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
