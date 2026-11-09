---
symbol: "VPS54"
type: "gene"
col: 6827
ensembl_id: "ENSG00000143952"
name: "VPS54 subunit of GARP complex"
location: "2p15-p14"
module: 17
arm: "+"
pooled_cpm: 125.87
n_lines_expressing: 50
n_dd_up: 2
n_dd_down: 22
n_dd_up_clean: 2
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/017"]
generated_by: "tahoemap"
---

# VPS54

*VPS54 subunit of GARP complex* — 2p15-p14

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (none with an alert); the strongest is [[Cobimetinib (drug)]] 5 µM: 1.22× (z +3.8, q 0.052, up in 25 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (A-427 1.73×; ⚠ cell-cycle shift, explains ~47% of this change).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (12 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.348× (z -21.2, q 0e+00, down in 48 of 48 measured lines) ⚠ cell-cycle shift, explains ~25% of this change. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 0.377× (z -19.6, q 0e+00, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (92 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 8 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TATDN3]] (+0.60, fdr 3e-05), [[PAIP1]] (+0.59, fdr 1e-05), [[FAM169A]] (+0.59, fdr 1e-04); moves opposite to [[BAIAP2]] (-0.52, fdr 1e-05), [[TMBIM6]] (-0.52, fdr 1e-04), [[SUN1]] (-0.51, fdr 6e-04).
> It sits in the **+** arm of [[Module 017]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6827.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (A-427 1.73×; ⚠ cell-cycle shift, explains ~47% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 5 µM |  | **1.22×** | +3.8 | 0.052 | 25/47 (SW480, LS 180, …) | rises with dose |  |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | **1.20×** | +3.7 | 0.052 | 23/48 (NCI-H1792, SW480, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 1.12× | +3.2 | 0.30 | 15/48 (PANC-1, KATO III, …) | rises with dose | low cells (technical?) |
| [[TAK-901 (drug)]] 0.05 µM |  | 1.17× | +3.0 | 0.33 | 19/47 (HEC-1-A, BT-474, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 14 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6827.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.348×** | -21.2 | 0e+00 | 48/48 (HepG2/C3A, SW480, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.377×** | -19.6 | 0e+00 | 48/48 (HepG2/C3A, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.487×** | -14.5 | 4e-45 | 48/48 (HepG2/C3A, SW480, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | **0.508×** | -13.6 | 5e-40 | 46/49 (C32, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **0.510×** | -13.0 | 1e-36 | 41/44 (A549, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.528×** | -12.3 | 6e-33 | 42/48 (LOX-IMVI, RKO, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.657×** | -11.8 | 2e-30 | 41/49 (AsPC-1, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.546×** | -11.7 | 1e-29 | 45/50 (RKO, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~25% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **0.585×** | -10.0 | 1e-21 | 35/45 (C32, NCI-H2030, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.779×** | -7.0 | 1e-10 | 28/48 (SK-MEL-2, A-172, …) | rises with dose | composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.801×** | -6.2 | 3e-08 | 27/48 (A-172, hTERT-HPNE, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.738×** | -6.1 | 5e-08 | 33/48 (HepG2/C3A, SW1417, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.743×** | -6.0 | 1e-07 | 29/48 (SNU-423, C32, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.763×** | -5.4 | 2e-06 | 32/48 (HepG2/C3A, SW480, …) | two highest doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~39% of this change | **0.768×** | -5.3 | 4e-06 | 32/48 (SW 1271, C32, …) | inconsistent across doses | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.769×** | -5.3 | 5e-06 | 26/48 (A-172, HS-578T, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.804×** | -4.4 | 4e-04 | 26/48 (J82, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.865× | -4.1 | 0.001 | 15/48 (SW1417, SW 900, …) | top dose only |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.756×** | -2.9 | 0.077 | 24/48 (SW 1271, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.40 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6827. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 130 | 0 | 13 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.262× (z -17.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.324× (z -16.1) |
| [[C32 (line)]] | wt | 159 | 0 | 13 (8 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.173× (z -19.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.382× (z -11.5) |
| [[NCI-H460 (line)]] | wt | 127 | 0 | 13 (10 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.276× (z -17.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.410× (z -12.6) |
| [[HepG2_C3A (line)]] | wt | 482 | 0 | 12 (10 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.123× (z -20.5) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.128× (z -20.1) |
| [[HS-578T (line)]] | alt | 94.9 | 0 | 11 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.420× (z -14.8) ⚠ cell-cycle shift, explains ~47% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.308× (z -14.4) |
| [[A498 (line)]] | wt | 127 | 0 | 10 (7 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.255× (z -18.4) |
| [[HOP62 (line)]] | alt | 103 | 0 | 10 (6 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.335× (z -13.8) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.371× (z -12.5) |
| [[SW480 (line)]] | alt | 151 | 0 | 9 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.258× (z -19.3) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.289× (z -17.7) |
| [[NCI-H1792 (line)]] | alt | 224 | 0 | 8 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.199× (z -20.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.279× (z -16.5) |
| [[NCI-H2030 (line)]] | alt | 163 | 0 | 8 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.196× (z -19.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.339× (z -13.8) |
| [[A549 (line)]] | wt | 170 | 0 | 7 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0711× (z -32.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.405× (z -16.0) |
| [[LOX-IMVI (line)]] | wt | 116 | 0 | 7 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.403× (z -16.6) |
| [[A-427 (line)]] | wt | 148 | 1 (1 ⚠) | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.73× (z +9.9) ⚠ cell-cycle shift, explains ~47% of this change | [[Panobinostat (drug)]] 5 µM 0.418× (z -11.3) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.466× (z -9.5) |
| [[HEC-1-A (line)]] | alt | 134 | 0 | 6 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.429× (z -12.4) |
| [[LoVo (line)]] | wt | 116 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.307× (z -16.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.368× (z -14.1) |
| [[NCI-H1573 (line)]] | alt | 118 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.221× (z -18.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.377× (z -12.5) |
| [[SHP-77 (line)]] | alt | 155 | 0 | 6 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.396× (z -11.3) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.536× (z -10.7) |
| [[LS 180 (line)]] | wt | 99.7 | 0 | 5 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.247× (z -17.3) |
| [[MIA PaCa-2 (line)]] | alt | 110 | 0 | 5 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.267× (z -15.5) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.295× (z -14.3) |
| [[NCI-H23 (line)]] | alt | 135 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.310× (z -14.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.356× (z -12.1) |
| [[Panc 03.27 (line)]] | alt | 111 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.235× (z -18.4) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.267× (z -16.8) |
| [[PANC-1 (line)]] | alt | 131 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.420× (z -12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.520× (z -10.1) |
| [[RKO (line)]] | wt | 116 | 0 | 5 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.272× (z -13.9) |
| [[SW 900 (line)]] | alt | 139 | 0 | 5 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.210× (z -18.1) |
| [[SW1417 (line)]] | alt | 145 | 0 | 5 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.294× (z -16.3) |
| [[AsPC-1 (line)]] | alt | 128 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.335× (z -17.6) |
| [[hTERT-HPNE (line)]] | wt | 99.3 | 0 | 4 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.258× (z -13.1) |
| [[KATO III (line)]] | alt | 97.1 | 0 | 4 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.292× (z -14.4) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.298× (z -14.1) |
| [[RPMI-7951 (line)]] | alt | 106 | 0 | 4 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.342× (z -11.3) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.396× (z -9.7) |
| [[SNU-423 (line)]] | alt | 89.4 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.431× (z -14.0) ⚠ cell-cycle shift, explains ~47% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.340× (z -12.8) |
| [[HT-29 (line)]] | alt | 99.5 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.282× (z -13.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.323× (z -12.9) |
| [[NCI-H2347 (line)]] | alt | 91.2 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.393× (z -16.2) |
| [[SK-MEL-2 (line)]] | alt | 107 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.328× (z -18.6) ⚠ cell-cycle shift, explains ~47% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.456× (z -9.0) |
| [[AN3 CA (line)]] | alt | 197 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.284× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.343× (z -8.5) |
| [[BT-474 (line)]] | alt | 90.7 | 0 | 2 | — | [[Auranofin (drug)]] 5 µM 0.432× (z -8.9) |
| [[H4 (line)]] | wt | 124 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.296× (z -12.1) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.358× (z -10.2) |
| [[Hs 766T (line)]] | wt | 63.8 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.390× (z -9.1) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.410× (z -8.6) |
| [[SW48 (line)]] | wt | 123 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.294× (z -10.0) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.320× (z -9.3) |
| [[C-33 A (line)]] | alt | 142 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.280× (z -13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change |
| [[CFPAC-1 (line)]] | alt | 65.0 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.466× (z -8.5) ⚠ cell-cycle shift, explains ~25% of this change |
| [[HCT15 (line)]] | alt | 143 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.166× (z -18.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change |
| [[J82 (line)]] | alt | 60.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.580× (z -8.5) ⚠ cell-cycle shift, explains ~47% of this change |
| [[SW 1271 (line)]] | alt | 120 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0942× (z -11.6) ⚠ transcription drop; cell-cycle shift, explains ~39% of this change |
| [[CHP-212 (line)]] | wt | 138 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 95.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 122 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 134 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 194 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 104 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 121 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6827), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 8 of them with an alert (⚠; 8 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TATDN3]] | +0.60 | +0.44 / +0.53 | both halves | 3e-05 |  |
| [[PAIP1]] | +0.59 | +0.50 / +0.59 | both halves | 1e-05 |  |
| [[FAM169A]] | +0.59 | +0.34 / +0.65 | both halves | 1e-04 |  |
| [[ZNHIT6]] | +0.59 | +0.52 / +0.61 | both halves | 1e-05 |  |
| [[RWDD3]] | +0.58 | +0.54 / +0.48 | both halves | 2e-05 |  |
| [[NDUFAF5]] | +0.58 | +0.62 / +0.56 | both halves | 1e-05 |  |
| [[NEK3]] | +0.56 | +0.46 / +0.67 | both halves | 2e-05 |  |
| [[SLC16A14]] | +0.56 | +0.37 / +0.47 | both halves | 8e-05 |  |
| [[C3orf33]] | +0.56 | +0.46 / +0.45 | both halves | 3e-05 |  |
| [[ZNF282]] | +0.56 | +0.45 / +0.51 | both halves | 3e-05 |  |
| [[TMLHE]] | +0.55 | +0.50 / +0.53 | both halves | 1e-05 |  |
| [[PTPMT1]] | +0.55 | +0.48 / +0.50 | both halves | 2e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BAIAP2]] | -0.52 | -0.51 / -0.53 | both halves | 1e-05 |  |
| [[TMBIM6]] | -0.52 | -0.35 / -0.51 | both halves | 1e-04 |  |
| [[SUN1]] | -0.51 | -0.22 / -0.45 | both halves | 6e-04 |  |
| [[MICALL2]] | -0.49 | -0.47 / -0.53 | both halves | 2e-05 |  |
| [[APLP2]] | -0.48 | -0.35 / -0.45 | both halves | 1e-04 |  |
| [[PITRM1]] | -0.48 | -0.50 / -0.49 | both halves | 1e-05 |  |
| [[EIF4A1]] | -0.47 | -0.29 / -0.50 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 1, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises VPS54's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.9% of all compounds | 0.020 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[LRRC8D]] | C | LRRC8D activity raises VPS54's level | lines that do not express LRRC8D (3) vs lines expressing it (47) | 1.48× lower at baseline in the lines without LRRC8D | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: PPFIBP2, USP31, EID2; maybe low, not absent; its own permutation p |
| [[NEK3]] | C | NEK3 activity strengthens VPS54's drug response | lines that do not express NEK3 (3) vs lines expressing it (47) | the lines without NEK3 respond 0.59× as strongly (z diff +2.88); strongest at Idarubicin (hydrochloride) 5 µM: 0.98x vs 0.59x (z diff +6.4) | 0.083 | ⚠ few lines (3 vs 47); across organs; also absent: ZFP36, IQCN, SLC22A20P; artifact flags |
| [[PFKP]] | C | PFKP activity lowers VPS54's level | lines that do not express PFKP (3) vs lines expressing it (47) | 1.47× higher at baseline in the lines without PFKP | 0.091 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: ASPH, MAP3K5, CFAP45; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 017]] — Intraflagellar transport; 202 genes; this gene is in the **+** arm (projection on the module's main direction 0.412). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-21.4, -1.5); signed map (-11.2, -23.4). **Vector** length 83.2, 23.7% of its response variance represented; |z| ≥ 3 in 1,214 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +7.6 | +3.2 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +6.0 | +2.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~64% of this change | +5.2 | -3.1 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.5 | +0.1 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.0 | +2.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.7 | +2.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.5 | +1.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.4 | +0.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.3 | +3.8 |
|  | [[venetoclax (drug)]] 5 µM |  | +2.3 | -0.3 |
| fall | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.3 | -6.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -3.1 | -11.7 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | -2.6 | -21.2 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.3 | -1.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -2.3 | -12.3 |
|  | [[Clopidogrel (drug)]] 0.05 µM |  | -1.5 | -0.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.4 | -6.0 |
|  | [[Fusidic acid (drug)]] 5 µM |  | -1.4 | +0.6 |

## What is on record

|  |  |
|---|---|
| Name | VPS54 subunit of GARP complex |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p15-p14 — chr2:63,892,146-64,019,428 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HCC8, PPP1R164 |
| Gene groups (HGNC) | Protein phosphatase 1 regulatory subunits; Golgi associated retrograde protein (GARP) complex |
| Reactome | 4 pathways, smallest: Retrograde transport at the Trans-Golgi-Network; Intra-Golgi and retrograde Golgi-to-ER traffic; Membrane Trafficking |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9P1Q0](https://www.uniprot.org/uniprotkb/Q9P1Q0) (Vacuolar protein sorting-associated protein 54):

> Acts as a component of the GARP complex that is involved in retrograde transport from early and late endosomes to the trans-Golgi network (TGN). The GARP complex is required for the maintenance of the cycling of mannose 6-phosphate receptors between the TGN and endosomes, this cycling is necessary for proper lysosomal sorting of acid hydrolases such as CTSD. Within the GARP complex, required to tether the complex to the TGN. Not involved in endocytic recycling.

**Summary**, from NCBI Gene [51542](https://www.ncbi.nlm.nih.gov/gene/51542):

> This gene encodes for a protein that in yeast forms part of a trimeric vacuolar-protein-sorting complex that is required for retrograde transport of proteins from prevacuoles to the late Golgi compartment. As in yeast, mammalian Vps54 proteins contain a coiled-coil region and dileucine motifs. Alternative splicing results in multiple transcript variants encoding different isoforms [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:18652](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18652) · Entrez [51542](https://www.ncbi.nlm.nih.gov/gene/51542) · UniProt [Q9P1Q0](https://www.uniprot.org/uniprotkb/Q9P1Q0) · Ensembl [ENSG00000143952](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000143952)

## Data

Gene col 6827: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6827); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6827, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6827]; `tensor/DDL_lfc|DDL_z.npy` [6827]; `embed/gene_vectors.npy` [6827]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6827 or target_col == 6827). Every well: [[VPS54 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/VPS54.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
