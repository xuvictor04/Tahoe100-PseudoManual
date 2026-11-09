---
symbol: "PREPL"
type: "gene"
col: 6120
ensembl_id: "ENSG00000138078"
name: "prolyl endopeptidase like"
location: "2p21"
module: 45
arm: "+"
pooled_cpm: 114.96
n_lines_expressing: 50
n_dd_up: 22
n_dd_down: 17
n_dd_up_clean: 21
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/045"]
generated_by: "tahoemap"
---

# PREPL

*prolyl endopeptidase like* — 2p21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (1 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 1.97× (z +14.5, q 4e-45, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (1 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.05 µM: 0.724× (z -4.8, q 0.001, down in 26 of 45 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Temsirolimus (drug)]] 0.05 µM: 0.752× (z -4.6, q 0.001, down in 32 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SNX2]] (+0.68, fdr 7e-06), [[CAPN5]] (+0.66, fdr 7e-06), [[FIG4]] (+0.62, fdr 7e-06); moves opposite to [[KPNA4]] (-0.61, fdr 7e-06), [[CRK]] (-0.57, fdr 1e-05), [[RAB35]] (-0.57, fdr 1e-05).
> It sits in the **+** arm of [[Module 045]] (Iron uptake and transport).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[QPRT]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 2 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6120.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM |  | **1.97×** | +14.5 | 4e-45 | 47/48 (LOX-IMVI, SW480, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~1% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.12×** | +12.0 | 8e-31 | 41/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 0.5 µM |  | **1.96×** | +10.7 | 2e-24 | 45/48 (C-33 A, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.92×** | +10.4 | 3e-23 | 40/48 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.56×** | +9.6 | 9e-20 | 38/48 (SW1417, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 0.05 µM |  | **1.70×** | +8.5 | 2e-15 | 46/49 (NCI-H460, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.55×** | +7.0 | 2e-10 | 37/48 (A-172, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.31×** | +7.0 | 2e-10 | 39/49 (PANC-1, RKO, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.51×** | +6.6 | 2e-09 | 42/48 (C-33 A, NCI-H460, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM |  | **1.43×** | +5.7 | 6e-07 | 32/48 (SW480, A-172, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.42×** | +5.6 | 9e-07 | 28/48 (NCI-H460, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.44×** | +5.6 | 1e-06 | 28/48 (NCI-H460, RKO, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.41×** | +5.5 | 2e-06 | 30/48 (NCI-H460, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.37×** | +5.0 | 2e-05 | 31/48 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.29×** | +4.0 | 0.002 | 29/48 (C-33 A, NCI-H23, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.26×** | +3.7 | 0.008 | 24/48 (SW1417, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 2 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6120.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.724×** | -4.8 | 0.001 | 26/45 (RKO, SW1417, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Temsirolimus (drug)]] 0.05 µM |  | **0.752×** | -4.6 | 0.001 | 32/49 (CFPAC-1, A-172, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.748×** | -4.4 | 0.001 | 30/47 (LOX-IMVI, C32, …) | inconsistent across doses |  |
| [[Diphenhydramine (drug)]] 0.5 µM |  | **0.762×** | -4.4 | 0.001 | 27/48 (NCI-H1792, LS 180, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | **0.762×** | -4.3 | 0.001 | 35/48 (SW1417, AsPC-1, …) | inconsistent across doses |  |
| [[Busulfan (drug)]] 0.05 µM |  | **0.763×** | -4.3 | 0.001 | 30/49 (SW1417, A498, …) | inconsistent across doses |  |
| [[Larotrectinib (drug)]] 0.05 µM |  | **0.783×** | -3.9 | 0.008 | 29/49 (SW1417, CFPAC-1, …) | inconsistent across doses |  |
| [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | **0.787×** | -3.8 | 0.009 | 29/48 (SNU-1, SW1417, …) | inconsistent across doses |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.797×** | -3.6 | 0.018 | 24/48 (CFPAC-1, HEC-1-A, …) | inconsistent across doses |  |
| [[Megestrol (drug)]] 0.05 µM |  | **0.805×** | -3.5 | 0.031 | 23/48 (Panc 03.27, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Tirabrutinib (drug)]] 0.5 µM |  | **0.809×** | -3.4 | 0.036 | 23/48 (LS 180, NCI-H1573, …) | inconsistent across doses |  |
| [[(S)-Crizotinib (drug)]] 0.5 µM |  | **0.815×** | -3.3 | 0.047 | 18/48 (NCI-H1792, LS 180, …) | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.948× | -3.3 | 0.047 | 0/50 | inconsistent across doses |  |
| [[vincristine (drug)]] 0.5 µM |  | **0.739×** | -3.2 | 0.050 | 24/48 (HT-29, HOP62, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[(R)-Verapamil (hydrochloride) (drug)]] 0.05 µM |  | **0.821×** | -3.1 | 0.062 | 16/49 (CFPAC-1, SW48, …) | inconsistent across doses |  |
| [[Apalutamide (drug)]] 0.5 µM |  | **0.823×** | -3.1 | 0.064 | 19/48 (LS 180, AsPC-1, …) | inconsistent across doses |  |
| [[Mifepristone (drug)]] 0.5 µM |  | **0.824×** | -3.1 | 0.064 | 20/48 (LS 180, NCI-H1792, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6120. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 113 | 10 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.57× (z +20.5) | — |
| [[PANC-1 (line)]] | alt | 155 | 5 (1 ⚠) | 3 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.28× (z +16.9) | [[Homoharringtonine (drug)]] 0.05 µM 0.446× (z -11.4) |
| [[SW480 (line)]] | alt | 129 | 8 (1 ⚠) | 0 | [[Selinexor (drug)]] 5 µM 2.09× (z +13.9) | — |
| [[SW1417 (line)]] | alt | 136 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.11× (z +18.1) | [[Dinaciclib (drug)]] 5 µM 0.186× (z -19.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[LOX-IMVI (line)]] | wt | 95.3 | 4 | 0 | [[Selinexor (drug)]] 5 µM 3.21× (z +14.7) | — |
| [[NCI-H1573 (line)]] | alt | 99.7 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.15× (z +14.6) | — |
| [[NCI-H1792 (line)]] | alt | 76.9 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.69× (z +13.8) | — |
| [[RKO (line)]] | wt | 104 | 3 | 1 (1 ⚠) | [[Selinexor (drug)]] 5 µM 2.22× (z +10.8) | [[Dinaciclib (drug)]] 0.05 µM 0.302× (z -11.3) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 87.6 | 3 | 0 | [[Selinexor (drug)]] 5 µM 2.11× (z +10.3) | — |
| [[C-33 A (line)]] | alt | 111 | 3 | 0 | [[Selinexor (drug)]] 5 µM 2.44× (z +11.6) | — |
| [[HOP62 (line)]] | alt | 70.3 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.05× (z +13.2) | — |
| [[HT-29 (line)]] | alt | 184 | 2 | 1 (1 ⚠) | [[Selinexor (drug)]] 5 µM 2.15× (z +12.3) | [[Docetaxel (drug)]] 0.05 µM 0.464× (z -9.1) ⚠ transcription drop; cell-cycle shift, explains ~18% of this change |
| [[J82 (line)]] | alt | 60.7 | 3 | 0 | [[Selinexor (drug)]] 5 µM 2.18× (z +9.2) | — |
| [[NCI-H23 (line)]] | alt | 240 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.79× (z +12.8) | — |
| [[SNU-1 (line)]] | wt | 227 | 1 | 2 (2 ⚠) | [[Selinexor (drug)]] 0.5 µM 2.70× (z +10.0) | [[Dinaciclib (drug)]] 5 µM 0.0608× (z -27.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 222 | 2 (1 ⚠) | 0 | [[Selinexor (drug)]] 5 µM 2.00× (z +11.1) | — |
| [[A549 (line)]] | wt | 96.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.63× (z +11.6) | — |
| [[AsPC-1 (line)]] | alt | 76.0 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.01× (z +10.7) | — |
| [[BT-474 (line)]] | alt | 79.4 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.78× (z +8.9) | — |
| [[CFPAC-1 (line)]] | alt | 143 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.361× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HepG2_C3A (line)]] | wt | 61.0 | 2 | 0 | [[Selinexor (drug)]] 5 µM 2.38× (z +8.9) | — |
| [[KATO III (line)]] | alt | 165 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.83× (z +13.5) | — |
| [[LS 180 (line)]] | wt | 123 | 2 | 0 | [[Selinexor (drug)]] 5 µM 2.62× (z +10.1) | — |
| [[NCI-H2030 (line)]] | alt | 107 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.73× (z +10.9) | — |
| [[SHP-77 (line)]] | alt | 95.9 | 2 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.60× (z +10.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.52× (z +9.7) | — |
| [[SW 900 (line)]] | alt | 129 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.69× (z +10.3) | — |
| [[C32 (line)]] | wt | 75.7 | 1 | 0 | [[Selinexor (drug)]] 5 µM 2.18× (z +8.5) | — |
| [[HCT15 (line)]] | alt | 137 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.342× (z -8.6) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 99.2 | 1 | 0 | [[Selinexor (drug)]] 5 µM 2.06× (z +9.0) | — |
| [[LoVo (line)]] | wt | 102 | 1 | 0 | [[Selinexor (drug)]] 5 µM 2.49× (z +11.8) | — |
| [[MIA PaCa-2 (line)]] | alt | 90.6 | 1 | 0 | [[Selinexor (drug)]] 5 µM 2.32× (z +10.1) | — |
| [[Panc 03.27 (line)]] | alt | 112 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.62× (z +12.0) | — |
| [[A498 (line)]] | wt | 106 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 109 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 182 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 103 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 133 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 122 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 98.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 79.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 112 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 89.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 119 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 151 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 159 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 60.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 73.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 136 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 165 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 97.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6120), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*69 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNX2]] | +0.68 | +0.68 / +0.67 | both halves | 7e-06 |  |
| [[CAPN5]] | +0.66 | +0.64 / +0.76 | both halves | 7e-06 |  |
| [[FIG4]] | +0.62 | +0.61 / +0.66 | both halves | 7e-06 |  |
| [[DNASE2]] | +0.62 | +0.59 / +0.57 | both halves | 1e-05 |  |
| [[ATP6V1B2]] | +0.60 | +0.53 / +0.59 | both halves | 1e-05 |  |
| [[PPDPF]] | +0.60 | +0.53 / +0.58 | both halves | 1e-05 |  |
| [[BPNT1]] | +0.60 | +0.45 / +0.69 | both halves | 3e-05 |  |
| [[MBIP]] | +0.59 | +0.65 / +0.50 | both halves | 1e-05 |  |
| [[C20orf96]] | +0.59 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[EPHX2]] | +0.59 | +0.61 / +0.55 | both halves | 1e-05 |  |
| [[DYNC2LI1]] | +0.59 | +0.63 / +0.56 | both halves | 1e-05 |  |
| [[TMEM9]] | +0.58 | +0.53 / +0.62 | both halves | 1e-05 |  |

## Genes that move opposite

*31 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KPNA4]] | -0.61 | -0.60 / -0.60 | both halves | 7e-06 |  |
| [[CRK]] | -0.57 | -0.52 / -0.59 | both halves | 1e-05 |  |
| [[RAB35]] | -0.57 | -0.51 / -0.63 | both halves | 1e-05 |  |
| [[HNRNPAB]] | -0.57 | -0.54 / -0.60 | both halves | 1e-05 |  |
| [[PWP2]] | -0.56 | -0.51 / -0.57 | both halves | 1e-05 |  |
| [[SLFNL1-AS1]] | -0.56 | -0.55 / -0.50 | both halves | 1e-05 |  |
| [[TEAD4]] | -0.56 | -0.50 / -0.56 | both halves | 1e-05 |  |
| [[REXO1]] | -0.55 | -0.57 / -0.53 | both halves | 1e-05 |  |
| [[GHRLOS]] | -0.54 | -0.58 / -0.48 | both halves | 2e-05 |  |
| [[NOP2]] | -0.54 | -0.64 / -0.45 | both halves | 3e-05 |  |
| [[TLNRD1]] | -0.54 | -0.59 / -0.54 | both halves | 1e-05 |  |
| [[GATAD2A]] | -0.54 | -0.51 / -0.56 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[QPRT]] | B | QPRT activity raises PREPL's level | lines that do not express QPRT (21) vs lines expressing it (29) | 1.10× lower at baseline in the lines without QPRT | 0.090 | ⚠ within organs, on part of the lines; also absent: OPRD1, FREM2, SERPINF1 |
| [[FHIP1A]] | B | FHIP1A activity lowers PREPL's level | lines that do not express FHIP1A (7) vs lines expressing it (43) | 1.35× higher at baseline in the lines without FHIP1A | 0.093 | ⚠ within organs, on part of the lines; also absent: SLC18B1, NIPAL1, TXNIP; maybe low, not absent |
| [[KCNK15-AS1]] | B | KCNK15-AS1 activity raises PREPL's level | lines that do not express KCNK15-AS1 (5) vs lines expressing it (45) | 1.47× lower at baseline in the lines without KCNK15-AS1 | 0.097 | ⚠ within organs, on part of the lines; also absent: DNAI1, FBXO15, ENSG00000132832; maybe low, not absent |
| [[SNX2]] | C | SNX2's natural level weakens PREPL's drug response | SNX2's natural level across 49 lines (lineage-adjusted; a glimpse) | r -0.63, reverse -0.13; direction not clear | 0.059 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 045]] — Iron uptake and transport; 102 genes; this gene is in the **+** arm (projection on the module's main direction 0.688). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (3.0, -8.2); signed map (-25.2, -6.6). **Vector** length 133, 48.2% of its response variance represented; |z| ≥ 3 in 1,245 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +15.5 | +14.5 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +11.6 | +10.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +7.4 | +4.0 |
|  | [[Selinexor (drug)]] 0.05 µM |  | +7.3 | +8.5 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +6.2 | +6.6 |
|  | [[Radotinib (drug)]] 5 µM |  | +4.9 | +3.0 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +3.7 | +1.7 |
|  | [[Afatinib (drug)]] 5 µM |  | +3.6 | +2.0 |
| fall | [[TAK-901 (drug)]] 0.05 µM |  | -4.6 | -4.4 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~12% of this change | -4.1 | -0.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.6 | +3.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -3.6 | +1.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.5 | -1.6 |
|  | [[Peretinoin (drug)]] 5 µM |  | -3.2 | -2.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.1 | +1.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.1 | -2.9 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -3.0 | -4.6 |

## What is on record

|  |  |
|---|---|
| Name | prolyl endopeptidase like |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p21 — chr2:44,316,281-44,361,862 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0436 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q4J6C6](https://www.uniprot.org/uniprotkb/Q4J6C6) (Prolyl endopeptidase-like):

> Serine peptidase whose precise substrate specificity remains unclear. Does not cleave peptides after a arginine or lysine residue. Regulates trans-Golgi network morphology and sorting by regulating the membrane binding of the AP-1 complex. May play a role in the regulation of synaptic vesicle exocytosis.

**Summary**, from NCBI Gene [9581](https://www.ncbi.nlm.nih.gov/gene/9581):

> The protein encoded by this gene belongs to the prolyl oligopeptidase subfamily of serine peptidases. Mutations in this gene have been associated with hypotonia-cystinuria syndrome, also known as the 2p21 deletion syndrome. Several alternatively spliced transcript variants encoding either the same or different isoforms have been described for this gene.[provided by RefSeq, Jan 2010]

**Accessions** — [HGNC:30228](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30228) · Entrez [9581](https://www.ncbi.nlm.nih.gov/gene/9581) · UniProt [Q4J6C6](https://www.uniprot.org/uniprotkb/Q4J6C6) · Ensembl [ENSG00000138078](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000138078)

## Data

Gene col 6120: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6120); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6120, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6120]; `tensor/DDL_lfc|DDL_z.npy` [6120]; `embed/gene_vectors.npy` [6120]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6120 or target_col == 6120). Every well: [[PREPL — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PREPL.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
