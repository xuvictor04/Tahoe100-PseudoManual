---
symbol: "TBC1D23"
type: "gene"
col: 435
ensembl_id: "ENSG00000036054"
name: "TBC1 domain family member 23"
location: "3q12.1-q12.2"
module: 41
arm: "+"
pooled_cpm: 154.22
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 31
n_dd_up_clean: 5
n_dd_down_clean: 19
in_vector_space: true
direction_upstream: 2
direction_downstream: 1
tags: ["gene", "module/041"]
generated_by: "tahoemap"
---

# TBC1D23

*TBC1 domain family member 23* — 3q12.1-q12.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (2 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 2.41× (z +7.3, q 1e-10, up in 41 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 31 drug-doses (12 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.442× (z -12.5, q 4e-33, down in 41 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.657× (z -8.7, q 5e-16, down in 35 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[COPB1]] (+0.82, fdr 7e-06), [[SRP54]] (+0.78, fdr 7e-06), [[TMEM263]] (+0.78, fdr 7e-06); moves opposite to [[TULP4]] (-0.62, fdr 1e-05), [[PRRC2B]] (-0.60, fdr 1e-05), [[SLC25A13]] (-0.59, fdr 1e-05).
> It sits in the **+** arm of [[Module 041]] (Intra-Golgi and retrograde Golgi-to-ER traffic).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 1 goes from it, the strongest it → [[MON2]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 3 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 435.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **2.41×** | +7.3 | 1e-10 | 41/49 (MIA PaCa-2, A-427, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.83×** | +5.1 | 1e-04 | 34/48 (A-427, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.31×** | +4.4 | 0.002 | 28/48 (RKO, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.22×** | +4.4 | 0.002 | 25/48 (A-427, A498, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.28×** | +3.9 | 0.009 | 27/48 (A-427, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **1.26×** | +3.8 | 0.016 | 27/48 (MIA PaCa-2, A-427, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~9% of this change | **1.24×** | +3.3 | 0.084 | 24/48 (PANC-1, SHP-77, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.16× | +3.1 | 0.13 | 19/49 (A-427, A-172, …) | rises with dose |  |
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | 1.30× | +3.0 | 0.15 | 19/48 (A-172, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 14 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 31 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 435.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.442×** | -12.5 | 4e-33 | 41/44 (A-427, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **0.476×** | -11.8 | 8e-30 | 43/49 (A-172, J82, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.657×** | -8.7 | 5e-16 | 35/49 (A-172, A498, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.650×** | -6.9 | 1e-09 | 43/48 (CFPAC-1, NCI-H1792, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **0.629×** | -6.8 | 1e-09 | 33/45 (RPMI-7951, hTERT-HPNE, …) | all doses, stronger at high dose | composition shift |
| [[Belumosudil (drug)]] 5 µM |  | **0.683×** | -5.8 | 5e-07 | 35/48 (J82, LoVo, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.784×** | -5.1 | 2e-05 | 33/48 (A-172, SW1417, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~36% of this change | **0.735×** | -4.7 | 2e-04 | 36/47 (HCT15, CFPAC-1, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.764×** | -4.1 | 0.002 | 33/48 (HS-578T, A-172, …) | top dose only |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.774×** | -4.1 | 0.003 | 30/48 (NCI-H1573, HT-29, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~69% of this change | **0.777×** | -4.0 | 0.003 | 28/48 (AsPC-1, SW480, …) | all doses, stronger at high dose |  |
| [[Busulfan (drug)]] 0.05 µM |  | **0.782×** | -3.9 | 0.005 | 26/49 (HEC-1-A, KATO III, …) | inconsistent across doses |  |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | **0.793×** | -3.7 | 0.010 | 29/49 (HT-29, LS 180, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.795×** | -3.6 | 0.011 | 25/48 (AsPC-1, HS-578T, …) | inconsistent across doses | cell-cycle shift (explains ~6% here) |
| [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~21% of this change | **0.797×** | -3.6 | 0.012 | 29/48 (HT-29, H4, …) | inconsistent across doses |  |
| [[Berbamine (drug)]] 0.05 µM |  | **0.798×** | -3.6 | 0.013 | 29/48 (NCI-H1573, KATO III, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | **0.814×** | -3.3 | 0.031 | 22/48 (LoVo, KATO III, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.679×** | -3.2 | 0.034 | 23/48 (RKO, AsPC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[(R)-Verapamil (hydrochloride) (drug)]] 0.05 µM |  | **0.818×** | -3.2 | 0.036 | 20/49 (KATO III, HT-29, …) | inconsistent across doses |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.693×** | -3.0 | 0.053 | 24/48 (AsPC-1, SNU-1, …) | top dose only | noisy plate (z scaled) |
| [[Pralsetinib (drug)]] 5 µM |  | **0.696×** | -3.0 | 0.055 | 22/49 (C32, HS-578T, …) | top dose only | noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.827×** | -3.0 | 0.055 | 22/48 (SW 1271, NCI-H1573, …) | inconsistent across doses |  |
| [[Belzutifan (drug)]] 5 µM |  | **0.697×** | -3.0 | 0.056 | 21/47 (CHP-212, AsPC-1, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.33 per unit of S-phase module lfc, +0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 435. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 163 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.290× (z -14.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.451× (z -12.3) |
| [[HS-578T (line)]] | alt | 301 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.301× (z -14.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.528× (z -10.4) |
| [[A-427 (line)]] | wt | 147 | 2 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.22× (z +10.5) ⚠ cell-cycle shift, explains ~17% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 1.81× (z +10.2) | [[Dinaciclib (drug)]] 5 µM 0.163× (z -22.8) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 259 | 1 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.68× (z +8.6) | [[Dinaciclib (drug)]] 0.5 µM 0.367× (z -12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.502× (z -11.3) |
| [[CFPAC-1 (line)]] | alt | 184 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.215× (z -17.5) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 155 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.337× (z -11.4) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 229 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.257× (z -17.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.577× (z -9.7) |
| [[RPMI-7951 (line)]] | alt | 254 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.326× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.539× (z -9.5) |
| [[hTERT-HPNE (line)]] | wt | 199 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.255× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[LOX-IMVI (line)]] | wt | 131 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.78× (z +8.5) | [[Dinaciclib (drug)]] 5 µM 0.370× (z -10.4) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 150 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.345× (z -10.7) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 172 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.478× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.573× (z -9.3) |
| [[BT-474 (line)]] | alt | 93.4 | 0 | 2 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.408× (z -8.9) ⚠ cell-cycle shift, explains ~47% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.532× (z -8.7) |
| [[HOP62 (line)]] | alt | 184 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.293× (z -11.3) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 152 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.360× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[KATO III (line)]] | alt | 173 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.122× (z -19.8) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 116 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.224× (z -11.7) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 113 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.13× (z +11.5) ⚠ cell-cycle shift, explains ~17% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 6.51× (z +9.9) | — |
| [[Panc 03.27 (line)]] | alt | 166 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.350× (z -12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[RKO (line)]] | wt | 161 | 0 | 2 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.415× (z -8.9) ⚠ unreliable plate only · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.519× (z -8.8) |
| [[AsPC-1 (line)]] | alt | 177 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.452× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[C32 (line)]] | wt | 114 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.73× (z +8.6) ⚠ cell-cycle shift, explains ~17% of this change | — |
| [[CHP-212 (line)]] | wt | 137 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.141× (z -13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[COLO 205 (line)]] | alt | 156 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.225× (z -13.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[H4 (line)]] | wt | 241 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.295× (z -9.6) ⚠ cell-cycle shift, explains ~47% of this change |
| [[HCT15 (line)]] | alt | 212 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.340× (z -9.2) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 111 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.340× (z -12.0) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 136 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.309× (z -11.8) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 140 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.414× (z -9.1) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 155 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.326× (z -12.0) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 119 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.194× (z -13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[SNU-423 (line)]] | alt | 158 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.597× (z -8.8) |
| [[SW 900 (line)]] | alt | 184 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.377× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[SW1417 (line)]] | alt | 158 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.405× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[SW480 (line)]] | alt | 136 | 1 | 0 | [[Binimetinib (drug)]] 0.5 µM 1.84× (z +9.0) | — |
| [[A549 (line)]] | wt | 164 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 96.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 64.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 92.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 110 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 145 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 158 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 82.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 152 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 108 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 142 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 70.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 248 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 172 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 107 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 435), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COPB1]] | +0.82 | +0.84 / +0.77 | both halves | 7e-06 | **novel candidate** |
| [[SRP54]] | +0.78 | +0.85 / +0.66 | both halves | 7e-06 |  |
| [[TMEM263]] | +0.78 | +0.78 / +0.72 | both halves | 7e-06 |  |
| [[ACBD3]] | +0.75 | +0.84 / +0.59 | both halves | 7e-06 |  |
| [[GOLGA2]] | +0.74 | +0.76 / +0.63 | both halves | 7e-06 |  |
| [[RAB1A]] | +0.73 | +0.77 / +0.63 | both halves | 7e-06 |  |
| [[OSBP]] | +0.73 | +0.76 / +0.63 | both halves | 7e-06 |  |
| [[GOLPH3L]] | +0.73 | +0.75 / +0.63 | both halves | 7e-06 |  |
| [[EIF2AK3]] | +0.72 | +0.76 / +0.64 | both halves | 7e-06 |  |
| [[COG6]] | +0.72 | +0.75 / +0.67 | both halves | 7e-06 |  |
| [[TMF1]] | +0.70 | +0.71 / +0.65 | both halves | 7e-06 |  |
| [[SEC31A]] | +0.70 | +0.74 / +0.63 | both halves | 7e-06 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TULP4]] | -0.62 | -0.63 / -0.54 | both halves | 1e-05 |  |
| [[PRRC2B]] | -0.60 | -0.66 / -0.50 | both halves | 1e-05 |  |
| [[SLC25A13]] | -0.59 | -0.66 / -0.53 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises TBC1D23's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 7.6% of all compounds | 0.071 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[PSMB5]] | B | PSMB5 activity lowers TBC1D23's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MON2]] | C | TBC1D23's natural level strengthens MON2's drug response | TBC1D23's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.64, reverse +0.34; direction not clear | 0.053 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 041]] — Intra-Golgi and retrograde Golgi-to-ER traffic; 111 genes; this gene is in the **+** arm (projection on the module's main direction 0.818). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (11.3, -35.4); signed map (-50.3, 13.1). **Vector** length 116, 43.2% of its response variance represented; |z| ≥ 3 in 1,167 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Intra-Golgi and retrograde Golgi-to-ER traffic* (reactome, mean cos +0.56 to 12); *Asparagine N-linked glycosylation* (reactome, mean cos +0.54 to 12); *ER to Golgi Anterograde Transport* (reactome, mean cos +0.59 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Binimetinib (drug)]] 5 µM |  | +3.5 | +1.2 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +3.2 | +1.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.9 | +1.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.9 | +3.1 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | +2.8 | +2.2 |
|  | [[Terfenadine (drug)]] 5 µM |  | +2.7 | +2.0 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -7.5 | -6.9 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.8 | +0.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | -5.1 | -5.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.5 | +0.6 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -4.5 | +0.2 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -3.5 | -1.3 |
|  | [[EX229 (drug)]] 5 µM |  | -3.5 | -2.9 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -3.4 | -3.2 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -3.0 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | TBC1 domain family member 23 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q12.1-q12.2 — chr3:100,260,992-100,325,251 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ11046 |
| Gene groups (HGNC) | TBC1 domain family members |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NUY8](https://www.uniprot.org/uniprotkb/Q9NUY8) (TBC1 domain family member 23):

> Putative Rab GTPase-activating protein which plays a role in vesicular trafficking. Involved in endosome-to-Golgi trafficking. Acts as a bridging protein by binding simultaneously to golgins, including GOLGA1 and GOLGA4, located at the trans-Golgi, and to the WASH complex, located on endosome-derived vesicles. Together with WDR11 complex facilitates the golgin-mediated capture of vesicles generated using AP-1. Plays a role in brain development, including in cortical neuron positioning (By …

**Summary**, from NCBI Gene [55773](https://www.ncbi.nlm.nih.gov/gene/55773):

> Involved in brain development; retrograde transport, endosome to Golgi; and vesicle tethering to Golgi. Located in WASH complex; cytoplasmic vesicle; and trans-Golgi network. Implicated in pontocerebellar hypoplasia type 11. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:25622](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25622) · Entrez [55773](https://www.ncbi.nlm.nih.gov/gene/55773) · UniProt [Q9NUY8](https://www.uniprot.org/uniprotkb/Q9NUY8) · Ensembl [ENSG00000036054](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000036054)

## Data

Gene col 435: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 435); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 435, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 435]; `tensor/DDL_lfc|DDL_z.npy` [435]; `embed/gene_vectors.npy` [435]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 435 or target_col == 435). Every well: [[TBC1D23 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TBC1D23.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
