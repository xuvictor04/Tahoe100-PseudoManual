---
symbol: "TRAM2"
type: "gene"
col: 779
ensembl_id: "ENSG00000065308"
name: "translocation associated membrane protein 2"
location: "6p12.2"
module: 104
arm: "+"
pooled_cpm: 68.46
n_lines_expressing: 49
n_dd_up: 6
n_dd_down: 20
n_dd_up_clean: 6
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 10
direction_downstream: 0
tags: ["gene", "module/104"]
generated_by: "tahoemap"
---

# TRAM2

*translocation associated membrane protein 2* — 6p12.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (none with an alert); the strongest is [[Belinostat (drug)]] 5 µM: 1.61× (z +6.4, q 7e-08, up in 28 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (8 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.539× (z -11.4, q 1e-27, down in 35 of 47 measured lines).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EHD2]] (+0.62, fdr 2e-05), [[IMPDH1]] (+0.62, fdr 3e-05), [[SKIC3]] (+0.61, fdr 2e-05); moves opposite to [[MED13]] (-0.59, fdr 5e-05), [[TTC6]] (-0.58, fdr 9e-05), [[DENND5B-AS1]] (-0.56, fdr 2e-04).
> It is in [[Module 104]], a single-armed module (Molecules associated with elastic fibres).
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[SRPX]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, none with an alert. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 779.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **1.61×** | +6.4 | 7e-08 | 28/47 (PANC-1, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.40×** | +4.6 | 0.002 | 24/47 (KATO III, COLO 205, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.38×** | +4.3 | 0.003 | 23/47 (KATO III, COLO 205, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.37×** | +4.2 | 0.004 | 25/47 (PANC-1, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.74×** | +3.9 | 0.012 | 22/48 (PANC-1, HEC-1-A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Folic acid (drug)]] 5 µM |  | 1.20× | +3.4 | 0.067 | 14/47 (A498, KATO III, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **1.28×** | +3.3 | 0.067 | 21/47 (SW 900, hTERT-HPNE, …) | rises with dose |  |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | 1.26× | +3.1 | 0.15 | 14/47 (HT-29, A-172, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.18× | +3.0 | 0.17 | 19/47 (KATO III, NCI-H2347, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 8 with an alert ⚠. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 779.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.539×** | -11.4 | 1e-27 | 35/47 (SNU-423, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.572×** | -10.4 | 1e-22 | 33/47 (SNU-423, HS-578T, …) | rises with dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.556×** | -7.6 | 6e-12 | 33/47 (HOP62, SNU-423, …) | rises with dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.588×** | -6.8 | 1e-09 | 32/46 (HOP62, HS-578T, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.618×** | -6.5 | 1e-08 | 27/47 (HOP62, SW48, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.610×** | -6.4 | 2e-08 | 29/47 (HOP62, SNU-423, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.627×** | -6.3 | 3e-08 | 30/47 (RPMI-7951, A-172, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.652×** | -5.5 | 2e-06 | 29/48 (NCI-H23, HOP62, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **0.686×** | -4.9 | 7e-05 | 22/37 (SW 900, H4, …) | all doses, flat | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.687×** | -4.9 | 7e-05 | 27/46 (C-33 A, A549, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.679×** | -4.8 | 7e-05 | 25/40 (HOP62, HS-578T, …) | all doses, flat | cell-cycle shift (explains ~20% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.699×** | -4.8 | 7e-05 | 27/47 (HOP62, A-172, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **0.714×** | -4.5 | 3e-04 | 26/47 (SK-MEL-2, HOP62, …) | all doses, flat | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.726×** | -4.3 | 6e-04 | 25/47 (HOP62, NCI-H460, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.725×** | -4.3 | 6e-04 | 26/47 (HOP62, NCI-H460, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.729×** | -4.2 | 8e-04 | 24/47 (NCI-H460, HS-578T, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.728×** | -4.0 | 0.002 | 25/47 (J82, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.744×** | -4.0 | 0.002 | 23/47 (HOP62, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **0.763×** | -3.4 | 0.024 | 22/46 (CHP-212, RKO, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.843× | -3.1 | 0.058 | 24/47 (HOP62, A-172, …) | top dose only |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.795×** | -3.1 | 0.058 | 18/47 (J82, RPMI-7951, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, -0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 779. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 186 | 1 (1 ⚠) | 18 (8 ⚠) | [[Adagrasib (drug)]] 0.05 µM 1.53× (z +11.5) ⚠ position not correctable | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.205× (z -16.8) |
| [[HS-578T (line)]] | alt | 274 | 0 | 11 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.169× (z -19.9) |
| [[RPMI-7951 (line)]] | alt | 207 | 0 | 11 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.210× (z -16.5) |
| [[SNU-423 (line)]] | alt | 270 | 0 | 10 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.123× (z -23.9) |
| [[NCI-H460 (line)]] | wt | 31.8 | 0 | 8 (4 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.274× (z -11.9) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.286× (z -11.5) |
| [[A549 (line)]] | wt | 75.8 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.312× (z -12.3) |
| [[CFPAC-1 (line)]] | alt | 65.6 | 0 | 6 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.214× (z -15.6) |
| [[J82 (line)]] | alt | 209 | 0 | 6 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.302× (z -15.9) |
| [[A-172 (line)]] | wt | 236 | 0 | 5 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.188× (z -14.4) |
| [[KATO III (line)]] | alt | 26.4 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.37× (z +12.9) | — |
| [[SW 900 (line)]] | alt | 52.8 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0676× (z -17.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.230× (z -9.3) |
| [[hTERT-HPNE (line)]] | wt | 172 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.315× (z -12.0) |
| [[Panc 03.27 (line)]] | alt | 122 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.390× (z -12.8) |
| [[A498 (line)]] | wt | 52.0 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.481× (z -10.0) |
| [[C32 (line)]] | wt | 96.3 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.343× (z -12.2) |
| [[NCI-H23 (line)]] | alt | 30.9 | 0 | 3 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0533× (z -21.9) |
| [[PANC-1 (line)]] | alt | 46.2 | 2 | 1 | [[Belinostat (drug)]] 5 µM 2.36× (z +9.6) | [[Homoharringtonine (drug)]] 5 µM 0.519× (z -10.1) |
| [[SK-MEL-2 (line)]] | alt | 48.1 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.110× (z -15.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.333× (z -11.0) |
| [[H4 (line)]] | wt | 84.8 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.164× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.365× (z -8.5) |
| [[HEC-1-A (line)]] | alt | 36.1 | 0 | 2 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.131× (z -10.4) ⚠ toxic · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.403× (z -8.6) |
| [[NCI-H2347 (line)]] | alt | 22.2 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.181× (z -11.1) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.379× (z -9.1) |
| [[SW48 (line)]] | wt | 28.2 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.108× (z -11.4) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 30.4 | 0 | 2 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.361× (z -10.2) ⚠ cell-cycle shift, explains ~35% of this change |
| [[AsPC-1 (line)]] | alt | 22.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.270× (z -11.3) |
| [[BT-474 (line)]] | alt | 31.4 | 0 | 1 (1 ⚠) | — | [[LY-2584702 (tosylate salt) (drug)]] 5 µM 0.0728× (z -8.7) ⚠ toxic |
| [[C-33 A (line)]] | alt | 27.4 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.168× (z -9.6) ⚠ toxic |
| [[COLO 205 (line)]] | alt | 41.4 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 4.03× (z +9.4) | — |
| [[Hs 766T (line)]] | wt | 52.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.310× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change |
| [[LoVo (line)]] | wt | 20.0 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.73× (z +8.9) | — |
| [[NCI-H2030 (line)]] | alt | 37.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.391× (z -9.0) |
| [[SHP-77 (line)]] | alt | 19.2 | 0 | 1 | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.216× (z -8.6) |
| [[SW 1271 (line)]] | alt | 121 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0782× (z -9.6) ⚠ toxic |
| [[A-427 (line)]] | wt | 21.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 52.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 44.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 38.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 58.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 49.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 36.3 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 30.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 13.1 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 51.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 53.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 57.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 50.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 27.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 38.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 135 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 41.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 779), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*64 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EHD2]] | +0.62 | +0.59 / +0.48 | both halves | 2e-05 |  |
| [[IMPDH1]] | +0.62 | +0.63 / +0.45 | both halves | 3e-05 |  |
| [[SKIC3]] | +0.61 | +0.57 / +0.46 | both halves | 2e-05 |  |
| [[TANC2]] | +0.61 | +0.60 / +0.49 | both halves | 1e-05 |  |
| [[LOX]] | +0.61 | +0.61 / +0.62 | both halves | 7e-06 |  |
| [[HACE1]] | +0.60 | +0.59 / +0.43 | both halves | 4e-05 |  |
| [[SSBP2]] | +0.60 | +0.57 / +0.50 | both halves | 1e-05 |  |
| [[SFXN3]] | +0.60 | +0.58 / +0.41 | both halves | 4e-05 |  |
| [[POT1]] | +0.58 | +0.59 / +0.33 | both halves | 1e-04 |  |
| [[KATNAL1]] | +0.57 | +0.65 / +0.46 | both halves | 3e-05 |  |
| [[SRPX]] | +0.57 | +0.67 / +0.49 | both halves | 1e-05 |  |
| [[COPS8]] | +0.57 | +0.53 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*36 of its nearest partners move opposite, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MED13]] | -0.59 | -0.49 / -0.39 | both halves | 5e-05 |  |
| [[TTC6]] | -0.58 | -0.58 / -0.37 | both halves | 9e-05 |  |
| [[DENND5B-AS1]] | -0.56 | -0.49 / -0.31 | both halves | 2e-04 |  |
| [[LINC01004]] | -0.56 | -0.53 / -0.30 | both halves | 2e-04 |  |
| [[LINC00571]] | -0.55 | -0.53 / -0.26 | both halves | 4e-04 |  |
| [[CREM]] | -0.55 | -0.45 / -0.42 | both halves | 4e-05 |  |
| [[DLGAP1-AS2]] | -0.55 | -0.45 / -0.40 | both halves | 5e-05 |  |
| [[PPP1R12A-AS2]] | -0.54 | -0.54 / -0.27 | both halves | 3e-04 |  |
| [[LINC01829]] | -0.54 | -0.51 / -0.33 | both halves | 1e-04 |  |
| [[ANKHD1-EIF4EBP3]] | -0.54 | -0.58 / -0.30 | both halves | 2e-04 |  |
| [[GCNT4]] | -0.54 | -0.45 / -0.32 | both halves | 2e-04 |  |
| [[NLGN3]] | -0.53 | -0.51 / -0.31 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 10, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SRPX]] | B | SRPX activity raises TRAM2's level | lines that do not express SRPX (22) vs lines expressing it (28) | 2.05× lower at baseline in the lines without SRPX | 0.039 | ⚠ within organs, on part of the lines; also absent: COL15A1, ARHGEF6, ENSG00000230647 |
| [[GNB4]] | B | GNB4 activity raises TRAM2's level | lines that do not express GNB4 (18) vs lines expressing it (32) | 2.11× lower at baseline in the lines without GNB4 | 0.040 | ⚠ within organs, on part of the lines; also absent: MPDZ, BVES, BVES-AS1 |
| [[ADAMTS2]] | B | ADAMTS2 activity raises TRAM2's level | lines that do not express ADAMTS2 (29) vs lines expressing it (21) | 2.38× lower at baseline in the lines without ADAMTS2 | 0.040 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ZNF667, ZNF667-AS1, COL3A1 |
| [[CA12]] | B | CA12 activity raises TRAM2's level | lines that do not express CA12 (29) vs lines expressing it (21) | 1.87× lower at baseline in the lines without CA12 | 0.050 | ⚠ within organs, on part of the lines; also absent: NID2, IL33, IDO1 |
| [[HDAC6]] | B | HDAC6 activity lowers TRAM2's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[SLC37A1]] | B | SLC37A1 activity lowers TRAM2's level | lines that do not express SLC37A1 (9) vs lines expressing it (41) | 3.41× higher at baseline in the lines without SLC37A1 | 0.060 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: RSPH1, GRTP1, ABCA3; its own permutation p |
| [[IRAK3]] | B | IRAK3 activity raises TRAM2's level | lines that do not express IRAK3 (36) vs lines expressing it (14) | 1.43× lower at baseline in the lines without IRAK3 | 0.060 | ⚠ within organs, on part of the lines; also absent: IRAG2, TRBC2, CXCL5 |
| [[KATNAL1]] | B | KATNAL1 activity raises TRAM2's level | lines that do not express KATNAL1 (7) vs lines expressing it (43) | 2.49× lower at baseline in the lines without KATNAL1 | 0.064 | ⚠ within organs, on part of the lines; also absent: BOLA3-DT, STARD9, SPAG17 |
| [[SERPINE1]] | B | SERPINE1 activity raises TRAM2's level | lines that do not express SERPINE1 (27) vs lines expressing it (23) | 2.37× lower at baseline in the lines without SERPINE1 | 0.070 | ⚠ within organs, on part of the lines; also absent: FRMD4A, SIRLNT, ENSG00000230615 |
| [[MPP1]] | B | MPP1 activity raises TRAM2's level | lines that do not express MPP1 (7) vs lines expressing it (43) | 2.50× lower at baseline in the lines without MPP1 | 0.089 | ⚠ within organs, on part of the lines; also absent: ZNF566, ELOVL5, PALM2AKAP2 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 104]] — Molecules associated with elastic fibres; 44 genes; every member is in the + arm (projection on the module's main direction 0.481). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (30.3, 10.3); signed map (-29.2, 24.3). **Vector** length 112, 31.9% of its response variance represented; |z| ≥ 3 in 1,310 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM |  | +5.5 | +6.4 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +5.5 | +4.3 |
|  | [[Panobinostat (drug)]] 5 µM |  | +5.3 | +4.6 |
|  | [[Dexamethasone (drug)]] 5 µM |  | +4.1 | +1.7 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +4.1 | +2.4 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.8 | +0.9 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | +3.5 | +2.2 |
|  | [[Budesonide (drug)]] 5 µM |  | +3.3 | +1.7 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -8.8 | -11.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -6.7 | -6.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -6.1 | -10.4 |
|  | [[Harringtonine (drug)]] 5 µM |  | -5.9 | -7.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -5.7 | -5.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.6 | -3.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.5 | -3.1 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | -3.0 | -2.7 |
|  | [[Lactate (calcium) (drug)]] 0.5 µM |  | -2.4 | -1.4 |
|  | [[Cabozantinib (S-malate) (drug)]] 0.05 µM |  | -2.3 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | translocation associated membrane protein 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p12.2 — chr6:52,497,408-52,577,060 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0057 |
| Gene groups (HGNC) | TLC domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15035](https://www.uniprot.org/uniprotkb/Q15035) (Translocating chain-associated membrane protein 2):

> Necessary for collagen type I synthesis. May couple the activity of the ER Ca(2+) pump SERCA2B with the activity of the translocon. This coupling may increase the local Ca(2+) concentration at the site of collagen synthesis, and a high Ca(2+) concentration may be necessary for the function of molecular chaperones involved in collagen folding. Required for proper insertion of the first transmembrane helix N-terminus of TM4SF20 into the ER lumen, may act as a ceramide sensor for regulated …

**Summary**, from NCBI Gene [9697](https://www.ncbi.nlm.nih.gov/gene/9697):

> TRAM2 is a component of the translocon, a gated macromolecular channel that controls the posttranslational processing of nascent secretory and membrane proteins at the endoplasmic reticulum (ER) membrane.[supplied by OMIM, Jul 2004]

**Accessions** — [HGNC:16855](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16855) · Entrez [9697](https://www.ncbi.nlm.nih.gov/gene/9697) · UniProt [Q15035](https://www.uniprot.org/uniprotkb/Q15035) · Ensembl [ENSG00000065308](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000065308)

## Data

Gene col 779: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 779); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 779, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 779]; `tensor/DDL_lfc|DDL_z.npy` [779]; `embed/gene_vectors.npy` [779]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 779 or target_col == 779). Every well: [[TRAM2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TRAM2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
