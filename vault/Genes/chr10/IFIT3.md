---
symbol: "IFIT3"
type: "gene"
col: 4135
ensembl_id: "ENSG00000119917"
name: "interferon induced protein with tetratricopeptide repeats 3"
location: "10q23.31"
module: 32
arm: "+"
pooled_cpm: 122.63
n_lines_expressing: 42
n_dd_up: 29
n_dd_down: 52
n_dd_up_clean: 29
n_dd_down_clean: 44
in_vector_space: true
direction_upstream: 55
direction_downstream: 55
tags: ["gene", "module/032"]
generated_by: "tahoemap"
---

# IFIT3

*interferon induced protein with tetratricopeptide repeats 3* — 10q23.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 29 drug-doses (none with an alert); the strongest is [[Harringtonine (drug)]] 0.5 µM: 3.77× (z +10.3, q 3e-22, up in 36 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 52 drug-doses (8 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.116× (z -16.7, q 0e+00, down in 40 of 40 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[IFIT1]] (+0.96, fdr 7e-06, ⚠ same locus), [[IFIT2]] (+0.96, fdr 7e-06, ⚠ same locus), [[RSAD2]] (+0.95, fdr 7e-06), [[IFIH1]] (+0.94, fdr 7e-06), [[XAF1]] (+0.93, fdr 7e-06).
> It is in [[Module 032]], a single-armed module (interferon alpha response).
> Probable direction (from the cell lines, not proof of direct regulation): 55 arrows point to it, the strongest [[PLAAT4]] → it (grade B ⚠); 55 go from it, the strongest it → [[IFI44]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, none with an alert; shown: the 15 strongest. 29 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4135.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **3.77×** | +10.3 | 3e-22 | 36/40 (NCI-H460, NCI-H2347, …) | two highest doses | cell-cycle shift (explains ~3% here) |
| [[TAK-901 (drug)]] 5 µM |  | **4.27×** | +5.9 | 1e-06 | 29/41 (RPMI-7951, NCI-H460, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **2.16×** | +5.8 | 2e-06 | 29/39 (AsPC-1, CFPAC-1, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **2.02×** | +5.2 | 2e-05 | 22/40 (NCI-H460, LS 180, …) | two highest doses | cell-cycle shift (explains ~14% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.88×** | +4.9 | 1e-04 | 24/39 (NCI-H2030, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~15% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.80×** | +4.4 | 8e-04 | 25/40 (AsPC-1, CFPAC-1, …) | rises with dose | position effect removed |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.76×** | +4.4 | 8e-04 | 24/39 (AsPC-1, CFPAC-1, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.62×** | +4.4 | 8e-04 | 23/40 (CFPAC-1, LoVo, …) | all doses, flat | noisy plate (z scaled) |
| [[venetoclax (drug)]] 0.05 µM |  | **1.86×** | +4.2 | 0.002 | 30/41 (HOP62, LoVo, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.70×** | +4.2 | 0.002 | 22/41 (CFPAC-1, SW1417, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.47×** | +4.0 | 0.004 | 21/41 (CFPAC-1, LoVo, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.56×** | +3.9 | 0.005 | 22/40 (AsPC-1, CFPAC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.63×** | +3.8 | 0.007 | 22/41 (CFPAC-1, AsPC-1, …) | rises with dose | position effect removed |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.60×** | +3.7 | 0.010 | 24/40 (A498, A-172, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.60×** | +3.7 | 0.010 | 23/40 (SNU-1, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 52 in all, 8 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 52 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4135.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.116×** | -16.7 | 0e+00 | 40/40 (SNU-423, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.146×** | -15.0 | 0e+00 | 39/40 (SNU-423, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.166×** | -13.9 | 7e-42 | 38/40 (RPMI-7951, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.347×** | -11.6 | 5e-29 | 34/40 (COLO 205, A549, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~7% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.266×** | -10.3 | 1e-22 | 35/40 (SNU-423, MIA PaCa-2, …) | rises with dose |  |
| [[Tofacitinib (drug)]] 5 µM |  | **0.442×** | -9.0 | 3e-17 | 29/41 (MIA PaCa-2, CFPAC-1, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.323×** | -8.8 | 1e-16 | 32/41 (MIA PaCa-2, A549, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.348×** | -8.2 | 2e-14 | 34/40 (BT-474, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.402×** | -7.1 | 1e-10 | 36/40 (CHP-212, SNU-423, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | **0.528×** | -7.0 | 2e-10 | 28/41 (MIA PaCa-2, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **0.421×** | -6.7 | 1e-09 | 27/40 (MIA PaCa-2, SNU-423, …) | all doses, stronger at high dose |  |
| [[Tofacitinib (drug)]] 0.5 µM |  | **0.435×** | -6.4 | 5e-09 | 24/41 (SNU-423, A549, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.457×** | -6.1 | 6e-08 | 27/40 (SNU-423, A549, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.468×** | -5.9 | 2e-07 | 25/40 (A549, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.456×** | -5.9 | 2e-07 | 27/39 (A-172, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.586×** | -5.9 | 2e-07 | 32/41 (CHP-212, CFPAC-1, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.25 per unit of S-phase module lfc, +0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4135. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SNU-423 (line)]] | alt | 459 | 0 | 26 (8 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0283× (z -21.0) |
| [[A549 (line)]] | wt | 145 | 0 | 20 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0777× (z -19.3) |
| [[MIA PaCa-2 (line)]] | alt | 245 | 1 | 15 (3 ⚠) | [[Harringtonine (drug)]] 0.5 µM 4.97× (z +8.7) | [[Tofacitinib (drug)]] 5 µM 0.0946× (z -18.0) |
| [[NCI-H2347 (line)]] | alt | 184 | 3 | 11 (1 ⚠) | [[Harringtonine (drug)]] 0.5 µM 10.2× (z +14.1) | [[Tofacitinib (drug)]] 5 µM 0.178× (z -14.8) |
| [[RPMI-7951 (line)]] | alt | 235 | 2 | 12 (3 ⚠) | [[Harringtonine (drug)]] 0.5 µM 5.45× (z +11.2) | [[Panobinostat (drug)]] 5 µM 0.0468× (z -20.2) |
| [[A-172 (line)]] | wt | 506 | 2 | 9 (6 ⚠) | [[Homoharringtonine (drug)]] 0.05 µM 4.97× (z +9.8) | [[Dinaciclib (drug)]] 5 µM 0.00742× (z -28.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.0440× (z -18.9) |
| [[CFPAC-1 (line)]] | alt | 277 | 2 | 9 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 7.24× (z +10.4) | [[Tofacitinib (drug)]] 5 µM 0.129× (z -15.7) |
| [[HS-578T (line)]] | alt | 128 | 2 | 9 (1 ⚠) | [[Harringtonine (drug)]] 0.5 µM 7.53× (z +10.6) | [[Panobinostat (drug)]] 5 µM 0.0478× (z -15.9) |
| [[A498 (line)]] | wt | 156 | 0 | 10 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0657× (z -16.1) |
| [[BT-474 (line)]] | alt | 84.9 | 0 | 10 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0524× (z -13.1) |
| [[LoVo (line)]] | wt | 92.1 | 0 | 10 | — | [[Belinostat (drug)]] 5 µM 0.0749× (z -13.7) |
| [[NCI-H1792 (line)]] | alt | 118 | 0 | 10 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.105× (z -15.9) |
| [[COLO 205 (line)]] | alt | 283 | 0 | 9 | — | [[Selinexor (drug)]] 5 µM 0.0919× (z -14.1) |
| [[NCI-H460 (line)]] | wt | 325 | 6 | 3 | [[Homoharringtonine (drug)]] 5 µM 5.53× (z +15.7) | [[Panobinostat (drug)]] 5 µM 0.100× (z -14.9) |
| [[HEC-1-A (line)]] | alt | 38.8 | 5 | 3 | [[Harringtonine (drug)]] 0.5 µM 8.20× (z +13.0) | [[Panobinostat (drug)]] 5 µM 0.170× (z -10.9) |
| [[RKO (line)]] | wt | 68.7 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.145× (z -11.9) |
| [[LS 180 (line)]] | wt | 73.7 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.84× (z +14.7) | — |
| [[CHP-212 (line)]] | wt | 105 | 0 | 5 | — | [[Belinostat (drug)]] 5 µM 0.0312× (z -13.4) |
| [[SK-MEL-2 (line)]] | alt | 129 | 1 | 4 | [[Harringtonine (drug)]] 0.5 µM 6.93× (z +9.5) | [[Panobinostat (drug)]] 5 µM 0.0945× (z -11.5) |
| [[KATO III (line)]] | alt | 66.1 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.0735× (z -11.9) |
| [[NCI-H2030 (line)]] | alt | 51.8 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.6× (z +17.2) | — |
| [[Panc 03.27 (line)]] | alt | 227 | 0 | 4 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0457× (z -9.6) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 5 µM 0.211× (z -9.2) |
| [[SW1417 (line)]] | alt | 66.3 | 0 | 4 | — | [[Selinexor (drug)]] 5 µM 0.258× (z -10.5) |
| [[AsPC-1 (line)]] | alt | 67.6 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.124× (z -9.7) |
| [[HOP62 (line)]] | alt | 36.8 | 3 | 0 | [[Harringtonine (drug)]] 5 µM 8.37× (z +9.9) | — |
| [[Hs 766T (line)]] | wt | 266 | 0 | 3 | — | [[Selinexor (drug)]] 5 µM 0.288× (z -10.5) |
| [[J82 (line)]] | alt | 62.6 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.54× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~18% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 5.15× (z +8.5) | — |
| [[C32 (line)]] | wt | 55.4 | 1 | 1 | [[Harringtonine (drug)]] 0.5 µM 12.2× (z +10.9) | [[Belinostat (drug)]] 5 µM 0.108× (z -9.5) |
| [[H4 (line)]] | wt | 135 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.109× (z -9.3) |
| [[hTERT-HPNE (line)]] | wt | 105 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.66× (z +10.2) | [[Panobinostat (drug)]] 5 µM 0.155× (z -10.4) |
| [[LOX-IMVI (line)]] | wt | 66.1 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.0654× (z -11.4) |
| [[SNU-1 (line)]] | wt | 49.7 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.102× (z -9.1) |
| [[SW 900 (line)]] | alt | 47.6 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.160× (z -8.7) |
| [[A-427 (line)]] | wt | 7.86 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 33.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 23.9 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 29.2 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 30.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 60.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 33.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 217 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 23.0 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 80.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 32.3 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 29.3 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 28.7 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 129 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 125 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 15.3 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 12.2 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4135), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IFIT1]] | +0.96 | +0.94 / +0.97 | both halves | 7e-06 | same gene group; pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 999; ⚠ same locus (15.1 kb, same strand: neighbours can correlate without regulation) |
| [[IFIT2]] | +0.96 | +0.96 / +0.95 | both halves | 7e-06 | same gene group; pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 999; ⚠ same locus (18.0 kb, same strand: neighbours can correlate without regulation) |
| [[RSAD2]] | +0.95 | +0.92 / +0.95 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 999 |
| [[IFIH1]] | +0.94 | +0.88 / +0.95 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 972 |
| [[XAF1]] | +0.93 | +0.87 / +0.94 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 938 |
| [[PARP14]] | +0.93 | +0.86 / +0.93 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 705 |
| [[OAS2]] | +0.93 | +0.88 / +0.94 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 947 |
| [[OASL]] | +0.92 | +0.90 / +0.93 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 964 |
| [[MX2]] | +0.92 | +0.86 / +0.93 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 888 |
| [[MX1]] | +0.92 | +0.90 / +0.92 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 972 |
| [[RIGI]] | +0.92 | +0.87 / +0.93 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 966 |
| [[PARP9]] | +0.92 | +0.85 / +0.92 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 925 |
| [[CMPK2]] | +0.92 | +0.87 / +0.92 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 904 |
| [[OAS1]] | +0.91 | +0.84 / +0.93 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 947 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*55 arrows, 55 of them with an alert ⚠; grade A 0, B 38, C 17. Shown: the 12 strongest; 43 more arrows (43 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLAAT4]] | B | PLAAT4 activity raises IFIT3's level | lines that do not express PLAAT4 (21) vs lines expressing it (29) | 3.18× lower at baseline in the lines without PLAAT4 | 8e-04 | ⚠ within organs, on part of the lines; also absent: PTPRB, TNFSF10, EPSTI1 |
| [[RSAD2]] | B | RSAD2 activity raises IFIT3's level | lines that do not express RSAD2 (14) vs lines expressing it (36) | 3.38× lower at baseline in the lines without RSAD2 | 0.001 | ⚠ within organs, on part of the lines; also absent: SH3TC1, IFI27, SRMS |
| [[OASL]] | B | OASL activity raises IFIT3's level | lines that do not express OASL (10) vs lines expressing it (40) | 3.49× lower at baseline in the lines without OASL | 0.001 | ⚠ within organs, on part of the lines; also absent: TMEM92-AS1, GBP2, TENT5A; maybe low, not absent |
| [[GBP4]] | B | GBP4 activity raises IFIT3's level | lines that do not express GBP4 (20) vs lines expressing it (30) | 3.54× lower at baseline in the lines without GBP4 | 0.002 | ⚠ within organs, on part of the lines; also absent: SAMD9L, CD5L, GBP1 |
| [[SAMD9L]] | B | SAMD9L activity raises IFIT3's level | lines that do not express SAMD9L (18) vs lines expressing it (32) | 3.38× lower at baseline in the lines without SAMD9L | 0.003 | ⚠ within organs, on part of the lines; also absent: GBP4, CD5L, TRIM22 |
| [[IFI16]] | B | IFI16 activity raises IFIT3's level | lines that do not express IFI16 (18) vs lines expressing it (32) | 3.28× lower at baseline in the lines without IFI16 | 0.004 | ⚠ within organs, on part of the lines; also absent: MMP14, IL1A, MAF |
| [[CASP10]] | B | CASP10 activity raises IFIT3's level | lines that do not express CASP10 (19) vs lines expressing it (31) | 2.50× lower at baseline in the lines without CASP10 | 0.005 | ⚠ within organs, on part of the lines; also absent: RARRES1, TRIM22, ACSL5 |
| [[IFI44]] | B | IFI44 activity raises IFIT3's level | lines that do not express IFI44 (12) vs lines expressing it (38) | 3.48× lower at baseline in the lines without IFI44 | 0.006 | ⚠ within organs, on part of the lines; also absent: SAMD9, GBP1, BMP2 |
| [[LMO2]] | B | LMO2 activity raises IFIT3's level | lines that do not express LMO2 (24) vs lines expressing it (26) | 2.64× lower at baseline in the lines without LMO2 | 0.007 | ⚠ within organs, on part of the lines; also absent: TNFSF10, SAA1, SAA4; maybe low, not absent |
| [[ABCA1]] | B | ABCA1 activity raises IFIT3's level | lines that do not express ABCA1 (20) vs lines expressing it (30) | 2.95× lower at baseline in the lines without ABCA1 | 0.007 | ⚠ within organs, on part of the lines; also absent: FN1, CDH2, IGFBP7 |
| [[SAMD9]] | B | SAMD9 activity raises IFIT3's level | lines that do not express SAMD9 (11) vs lines expressing it (39) | 3.87× lower at baseline in the lines without SAMD9 | 0.007 | ⚠ within organs, on part of the lines; also absent: IFI44, GBP1, TLR6 |
| [[OAS1]] | B | OAS1 activity raises IFIT3's level | lines that do not express OAS1 (13) vs lines expressing it (37) | 2.70× lower at baseline in the lines without OAS1 | 0.008 | ⚠ within organs, on part of the lines; also absent: OAS2, TRIM22, IFI27; maybe low, not absent |

### Downstream of this gene

*55 arrows, 55 of them with an alert ⚠; grade A 0, B 50, C 5. Shown: the 12 strongest; 43 more arrows (43 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IFI44]] | B | IFIT3 activity raises IFI44's level | lines that do not express IFIT3 (8) vs lines expressing it (42) | 5.39× lower at baseline in the lines without IFIT3 | 0.001 | ⚠ within organs, on part of the lines; also absent: GBP2, IFIT2, TRIM38; maybe low, not absent |
| [[DDX60]] | B | IFIT3 activity raises DDX60's level | lines that do not express IFIT3 (8) vs lines expressing it (42) | 3.10× lower at baseline in the lines without IFIT3 | 0.004 | ⚠ within organs, on part of the lines; also absent: GBP2, IFIT2, TRIM38; maybe low, not absent |
| [[OASL]] | B | IFIT3 activity raises OASL's level | lines that do not express IFIT3 (8) vs lines expressing it (42) | 3.83× lower at baseline in the lines without IFIT3 | 0.005 | ⚠ within organs, on part of the lines; also absent: GBP2, IFIT2, TRIM38; maybe low, not absent |
| [[RSAD2]] | B | IFIT3 activity raises RSAD2's level | lines that do not express IFIT3 (8) vs lines expressing it (42) | 4.07× lower at baseline in the lines without IFIT3 | 0.006 | ⚠ within organs, on part of the lines; also absent: GBP2, IFIT2, TRIM38; maybe low, not absent |
| [[IFIT1]] | B | IFIT3 activity raises IFIT1's level | lines that do not express IFIT3 (8) vs lines expressing it (42) | 2.53× lower at baseline in the lines without IFIT3 | 0.007 | ⚠ within organs, on part of the lines; also absent: GBP2, IFIT2, TRIM38; maybe low, not absent |
| [[IFI16]] | B | IFIT3 activity raises IFI16's level | lines that do not express IFIT3 (8) vs lines expressing it (42) | 6.81× lower at baseline in the lines without IFIT3 | 0.007 | ⚠ within organs, on part of the lines; also absent: GBP2, IFIT2, TRIM38; maybe low, not absent |
| [[CASP10]] | B | IFIT3 activity raises CASP10's level | lines that do not express IFIT3 (8) vs lines expressing it (42) | 3.70× lower at baseline in the lines without IFIT3 | 0.007 | ⚠ within organs, on part of the lines; also absent: GBP2, IFIT2, TRIM38; maybe low, not absent |
| [[B2M]] | B | IFIT3 activity raises B2M's level | lines that do not express IFIT3 (8) vs lines expressing it (42) | 2.62× lower at baseline in the lines without IFIT3 | 0.009 | ⚠ within organs, on part of the lines; also absent: GBP2, IFIT2, TRIM38; maybe low, not absent |
| [[IFI27]] | B | IFIT3 activity raises IFI27's level | lines that do not express IFIT3 (8) vs lines expressing it (42) | 4.91× lower at baseline in the lines without IFIT3 | 0.010 | ⚠ within organs, on part of the lines; also absent: GBP2, IFIT2, TRIM38; maybe low, not absent |
| [[TRIM22]] | B | IFIT3 activity raises TRIM22's level | lines that do not express IFIT3 (8) vs lines expressing it (42) | 4.89× lower at baseline in the lines without IFIT3 | 0.010 | ⚠ within organs, on part of the lines; also absent: GBP2, IFIT2, TRIM38; maybe low, not absent |
| [[CFB]] | B | IFIT3 activity raises CFB's level | lines that do not express IFIT3 (8) vs lines expressing it (42) | 4.93× lower at baseline in the lines without IFIT3 | 0.013 | ⚠ within organs, on part of the lines; also absent: GBP2, IFIT2, TRIM38; maybe low, not absent |
| [[GBP3]] | B | IFIT3 activity raises GBP3's level | lines that do not express IFIT3 (8) vs lines expressing it (42) | 3.21× lower at baseline in the lines without IFIT3 | 0.014 | ⚠ within organs, on part of the lines; also absent: GBP2, IFIT2, TRIM38; maybe low, not absent |

## Where it sits

- **Module**: [[Module 032]] — interferon alpha response; 139 genes; every member is in the + arm (projection on the module's main direction 0.958). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (47.9, 53.4); signed map (64.1, 31.4). **Vector** length 166, 64.6% of its response variance represented; |z| ≥ 3 in 1,674 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Interferon gamma signaling* (reactome, mean cos +0.78 to 17); *Modulation of host responses by IFN-stimulated genes* (reactome, mean cos +0.84 to 10); *ISG15 antiviral mechanism* (reactome, mean cos +0.85 to 11).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +12.7 | +10.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +10.9 | +4.9 |
|  | [[Harringtonine (drug)]] 5 µM |  | +8.8 | +5.2 |
|  | [[TAK-901 (drug)]] 5 µM |  | +8.1 | +5.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +6.8 | +2.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +6.7 | +2.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +6.3 | +5.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.2 | +2.6 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +4.5 | +4.4 |
| fall | [[Tofacitinib (drug)]] 5 µM |  | -10.6 | -9.0 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -9.4 | -7.0 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -9.1 | -6.7 |
|  | [[Selinexor (drug)]] 5 µM |  | -8.8 | -11.6 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -8.4 | -6.4 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -7.8 | -8.8 |

## What is on record

|  |  |
|---|---|
| Name | interferon induced protein with tetratricopeptide repeats 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q23.31 — chr10:89,327,307-89,377,473 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ISG60, RIG-G, CIG-49, IFI60, GARG-49, IRG2; previously IFIT4 |
| Gene groups (HGNC) | Tetratricopeptide repeat domain containing |
| Hallmark sets | INTERFERON_ALPHA_RESPONSE, INTERFERON_GAMMA_RESPONSE |
| Reactome | 6 pathways, smallest: Viral strategies to evade IFIT action; IFIT antiviral response; Interferon alpha/beta signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [O14879](https://www.uniprot.org/uniprotkb/O14879) (Interferon-induced protein with tetratricopeptide repeats 3):

> IFN-induced antiviral protein which acts as an inhibitor of cellular as well as viral processes, cell migration, proliferation, signaling, and viral replication. Enhances MAVS-mediated host antiviral responses by serving as an adapter bridging TBK1 to MAVS which leads to the activation of TBK1 and phosphorylation of IRF3 and phosphorylated IRF3 translocates into nucleus to promote antiviral gene transcription. Exhibits an antiproliferative activity via the up-regulation of cell cycle negative …

**Summary**, from NCBI Gene [3437](https://www.ncbi.nlm.nih.gov/gene/3437):

> Enables identical protein binding activity. Involved in antiviral innate immune response; negative regulation of apoptotic process; and negative regulation of cell population proliferation. Located in cytosol and mitochondrion. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:5411](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5411) · Entrez [3437](https://www.ncbi.nlm.nih.gov/gene/3437) · UniProt [O14879](https://www.uniprot.org/uniprotkb/O14879) · Ensembl [ENSG00000119917](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000119917)

## Data

Gene col 4135: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4135); `tables/drug_effects.parquet` (81 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4135, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4135]; `tensor/DDL_lfc|DDL_z.npy` [4135]; `embed/gene_vectors.npy` [4135]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4135 or target_col == 4135). Every well: [[IFIT3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IFIT3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
