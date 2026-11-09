---
symbol: "INPP4B"
type: "gene"
col: 3051
ensembl_id: "ENSG00000109452"
name: "inositol polyphosphate-4-phosphatase type II B"
location: "4q31.21"
module: 8
arm: "+"
pooled_cpm: 146.65
n_lines_expressing: 40
n_dd_up: 6
n_dd_down: 20
n_dd_up_clean: 6
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 25
direction_downstream: 15
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# INPP4B

*inositol polyphosphate-4-phosphatase type II B* — 4q31.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (none with an alert); the strongest is [[Selinexor (drug)]] 5 µM: 1.55× (z +9.9, q 2e-20, up in 24 of 38 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.619× (z -10.7, q 3e-24, down in 23 of 38 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[COLEC10]] (+0.58, fdr 4e-05), [[SAMD12]] (+0.56, fdr 1e-05), [[PRSS51]] (+0.55, fdr 1e-05); moves opposite to [[FAM228B]] (-0.59, fdr 1e-05), [[CCM2]] (-0.53, fdr 3e-05), [[ZIM2-AS1]] (-0.51, fdr 1e-05).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 25 arrows point to it, the strongest [[ITGB8]] → it (grade B ⚠); 15 go from it, the strongest it → [[EHF]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, none with an alert. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3051.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM |  | **1.55×** | +9.9 | 2e-20 | 24/38 (PANC-1, LOX-IMVI, …) | all doses, flat | low cells (technical?); cell-cycle shift (explains ~19% here) |
| [[Selinexor (drug)]] 0.05 µM |  | **1.83×** | +9.6 | 2e-19 | 29/39 (PANC-1, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~10% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.68×** | +8.3 | 3e-14 | 25/38 (PANC-1, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~20% here) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.46×** | +6.1 | 2e-07 | 22/38 (PANC-1, HS-578T, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.37×** | +5.0 | 7e-05 | 22/39 (LOX-IMVI, J82, …) | two highest doses | cell-cycle shift (explains ~8% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.22×** | +4.4 | 9e-04 | 17/38 (A-172, PANC-1, …) | two highest doses |  |
| [[Demeclocycline (drug)]] 5 µM |  | 1.16× | +3.3 | 0.075 | 10/38 (AsPC-1, SW1417, …) | top dose only |  |
| [[TAK-901 (drug)]] 0.05 µM |  | 1.23× | +3.1 | 0.11 | 11/37 (NCI-H23, NCI-H2030, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | 1.22× | +3.1 | 0.11 | 16/38 (MIA PaCa-2, Panc 03.27, …) | top dose only |  |
| [[Busulfan (drug)]] 0.05 µM |  | 1.21× | +3.0 | 0.14 | 12/39 (CFPAC-1, HOP62, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 7 with an alert ⚠. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3051.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.619×** | -10.7 | 3e-24 | 23/38 (COLO 205, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.537×** | -9.5 | 7e-19 | 27/37 (SNU-1, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.551×** | -9.4 | 7e-19 | 26/38 (COLO 205, Panc 03.27, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.577×** | -8.7 | 4e-16 | 24/38 (SNU-1, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.602×** | -8.0 | 1e-13 | 24/38 (COLO 205, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **0.683×** | -6.0 | 1e-07 | 23/38 (COLO 205, SNU-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.695×** | -5.7 | 7e-07 | 23/38 (Panc 03.27, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.775×** | -5.7 | 8e-07 | 21/39 (CFPAC-1, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.692×** | -5.6 | 1e-06 | 21/38 (C32, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~27% of this change | **0.720×** | -5.2 | 1e-05 | 24/38 (Hs 766T, CFPAC-1, …) | inconsistent across doses | low cells (technical?) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.561×** | -4.8 | 9e-05 | 23/38 (CFPAC-1, Panc 03.27, …) | rises with dose | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.758×** | -4.4 | 5e-04 | 20/38 (LS 180, AN3 CA, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.762×** | -4.3 | 8e-04 | 19/38 (COLO 205, LS 180, …) | rises with dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.771×** | -4.1 | 0.002 | 19/38 (COLO 205, Panc 03.27, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.784×** | -3.9 | 0.004 | 20/38 (LS 180, LoVo, …) | rises with dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.787×** | -3.8 | 0.005 | 16/38 (NCI-H1792, NCI-H2030, …) | top dose only |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.797×** | -3.6 | 0.012 | 19/39 (LoVo, NCI-H2030, …) | top dose only |  |
| [[Terfenadine (drug)]] 5 µM |  | 0.865× | -3.2 | 0.038 | 10/38 (NCI-H2347, HT-29, …) | top dose only |  |
| [[Pasireotide (acetate) (drug)]] 5 µM |  | 0.867× | -3.2 | 0.045 | 7/39 (NCI-H2030, SNU-1, …) | rises with dose | position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.819×** | -3.2 | 0.045 | 17/38 (CFPAC-1, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.816×** | -3.0 | 0.067 | 19/38 (CFPAC-1, COLO 205, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.830×** | -2.9 | 0.086 | 14/38 (CFPAC-1, KATO III, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3051. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CFPAC-1 (line)]] | alt | 808 | 0 | 14 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.218× (z -22.7) |
| [[COLO 205 (line)]] | alt | 302 | 0 | 14 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0599× (z -33.3) |
| [[SNU-1 (line)]] | wt | 834 | 0 | 13 (7 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.173× (z -16.9) |
| [[NCI-H2030 (line)]] | alt | 208 | 0 | 11 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.184× (z -18.7) |
| [[Panc 03.27 (line)]] | alt | 526 | 0 | 10 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.202× (z -18.3) |
| [[LS 180 (line)]] | wt | 172 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.336× (z -12.4) |
| [[LoVo (line)]] | wt | 90.5 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.296× (z -13.4) |
| [[AsPC-1 (line)]] | alt | 270 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.236× (z -16.3) |
| [[H4 (line)]] | wt | 67.4 | 6 (2 ⚠) | 0 | [[Selinexor (drug)]] 5 µM 3.95× (z +13.6) | — |
| [[KATO III (line)]] | alt | 141 | 0 | 6 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.155× (z -13.9) |
| [[PANC-1 (line)]] | alt | 38.3 | 6 (2 ⚠) | 0 | [[Selinexor (drug)]] 5 µM 4.39× (z +21.0) | — |
| [[A-172 (line)]] | wt | 89.2 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.47× (z +13.4) | — |
| [[A-427 (line)]] | wt | 42.7 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.73× (z +16.0) | — |
| [[C32 (line)]] | wt | 586 | 2 | 3 (1 ⚠) | [[Selinexor (drug)]] 5 µM 1.95× (z +8.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.330× (z -14.5) |
| [[NCI-H2347 (line)]] | alt | 299 | 0 | 5 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.282× (z -13.3) |
| [[SW1417 (line)]] | alt | 97.4 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.300× (z -12.3) |
| [[HS-578T (line)]] | alt | 46.0 | 4 (2 ⚠) | 0 | [[Selinexor (drug)]] 0.05 µM 4.98× (z +11.6) | — |
| [[hTERT-HPNE (line)]] | wt | 92.2 | 4 (1 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 9.51× (z +11.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Selinexor (drug)]] 5 µM 3.70× (z +9.7) | — |
| [[MIA PaCa-2 (line)]] | alt | 114 | 1 | 3 (2 ⚠) | [[Selinexor (drug)]] 5 µM 2.45× (z +9.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.257× (z -14.4) |
| [[SK-MEL-2 (line)]] | alt | 168 | 4 (1 ⚠) | 0 | [[Selinexor (drug)]] 5 µM 3.21× (z +13.8) | — |
| [[HT-29 (line)]] | alt | 150 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.352× (z -12.1) |
| [[LOX-IMVI (line)]] | wt | 57.2 | 3 | 0 | [[Selinexor (drug)]] 5 µM 5.60× (z +19.6) | — |
| [[NCI-H1792 (line)]] | alt | 381 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.181× (z -21.4) |
| [[RPMI-7951 (line)]] | alt | 155 | 3 | 0 | [[Selinexor (drug)]] 5 µM 4.49× (z +14.0) | — |
| [[J82 (line)]] | alt | 82.0 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.45× (z +12.0) | — |
| [[NCI-H1573 (line)]] | alt | 61.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.121× (z -19.3) |
| [[A549 (line)]] | wt | 81.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.202× (z -11.3) |
| [[HOP62 (line)]] | alt | 43.9 | 1 | 0 | [[Selinexor (drug)]] 0.05 µM 2.93× (z +8.6) | — |
| [[Hs 766T (line)]] | wt | 184 | 0 | 1 | — | [[Binimetinib (drug)]] 0.5 µM 0.404× (z -8.9) |
| [[NCI-H23 (line)]] | alt | 47.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.229× (z -10.0) |
| [[SW 1271 (line)]] | alt | 60.1 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.0597× (z -9.3) |
| [[SW 900 (line)]] | alt | 83.1 | 1 | 0 | [[Selinexor (drug)]] 5 µM 2.08× (z +8.8) | — |
| [[A498 (line)]] | wt | 27.4 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 191 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 348 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 16.2 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 17.5 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 13.7 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 107 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 12.6 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 308 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 33.9 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 123 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 137 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 11.4 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 19.7 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 186 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 51.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 14.8 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 14.6 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3051), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COLEC10]] | +0.58 | +0.63 / +0.42 | both halves | 4e-05 |  |
| [[SAMD12]] | +0.56 | +0.58 / +0.49 | both halves | 1e-05 |  |
| [[PRSS51]] | +0.55 | +0.50 / +0.55 | both halves | 1e-05 |  |
| [[MECOM]] | +0.55 | +0.53 / +0.50 | both halves | 1e-05 |  |
| [[UCA1]] | +0.54 | +0.61 / +0.41 | both halves | 4e-05 |  |
| [[SAMD12-AS1]] | +0.54 | +0.61 / +0.46 | both halves | 2e-05 |  |
| [[RBM47]] | +0.54 | +0.57 / +0.46 | both halves | 2e-05 |  |
| [[MTUS1]] | +0.53 | +0.49 / +0.50 | both halves | 1e-05 |  |
| [[PLCH1]] | +0.52 | +0.55 / +0.42 | both halves | 4e-05 | pathway: Inositol phosphate metabolism |
| [[ITGB6]] | +0.52 | +0.56 / +0.45 | both halves | 3e-05 |  |
| [[DNAH7]] | +0.51 | +0.41 / +0.46 | both halves | 4e-05 |  |
| [[GPR87]] | +0.51 | +0.48 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM228B]] | -0.59 | -0.64 / -0.53 | both halves | 1e-05 |  |
| [[CCM2]] | -0.53 | -0.44 / -0.59 | both halves | 3e-05 |  |
| [[ZIM2-AS1]] | -0.51 | -0.49 / -0.49 | both halves | 1e-05 |  |
| [[LINC01615]] | -0.51 | -0.59 / -0.36 | both halves | 1e-04 |  |
| [[FAM156A]] | -0.50 | -0.46 / -0.46 | both halves | 3e-05 |  |
| [[TSHZ3-AS1]] | -0.49 | -0.56 / -0.43 | both halves | 3e-05 |  |
| [[DCUN1D2]] | -0.47 | -0.31 / -0.56 | both halves | 2e-04 |  |
| [[DNAAF9]] | -0.47 | -0.47 / -0.41 | both halves | 4e-05 |  |
| [[TMCO3]] | -0.47 | -0.44 / -0.47 | both halves | 3e-05 |  |
| [[DENND2A]] | -0.47 | -0.59 / -0.33 | both halves | 1e-04 |  |
| [[SLC28A2-AS1]] | -0.46 | -0.37 / -0.51 | both halves | 9e-05 |  |
| [[PRSS53]] | -0.45 | -0.45 / -0.39 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*25 arrows, 25 of them with an alert ⚠; grade A 0, B 25, C 0. Shown: the 12 strongest; 13 more arrows (13 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ITGB8]] | B | ITGB8 activity raises INPP4B's level | lines that do not express ITGB8 (17) vs lines expressing it (33) | 2.41× lower at baseline in the lines without ITGB8 | 0.004 | ⚠ within organs, on part of the lines; also absent: LRATD2, HNMT, B3GALT5 |
| [[EHF]] | B | EHF activity raises INPP4B's level | lines that do not express EHF (27) vs lines expressing it (23) | 3.06× lower at baseline in the lines without EHF | 0.005 | ⚠ within organs, on part of the lines; also absent: TMPRSS4, IRF6, GJB3 |
| [[THRB]] | B | THRB activity strengthens INPP4B's drug response | lines that do not express THRB (15) vs lines expressing it (24) | the lines without THRB respond 0.72× as strongly (z diff +1.15); strongest at Homoharringtonine 5 µM: 1.32x vs 0.42x (z diff +7.8) | 0.006 | ⚠ within organs, on part of the lines; also absent: GOLT1A, SIDT1, P2RY2; target measured in part of the lines; both ways; artifact flags |
| [[DPP4]] | B | DPP4 activity raises INPP4B's level | lines that do not express DPP4 (29) vs lines expressing it (21) | 1.69× lower at baseline in the lines without DPP4 | 0.012 | ⚠ within organs, on part of the lines; also absent: LCN2, INAVA, KLK10 |
| [[UCA1]] | B | UCA1 activity raises INPP4B's level | lines that do not express UCA1 (37) vs lines expressing it (13) | 3.01× lower at baseline in the lines without UCA1 | 0.013 | ⚠ within organs, on part of the lines; also absent: TM4SF4, AGR3, LYZ |
| [[ADGRF1]] | B | ADGRF1 activity raises INPP4B's level | lines that do not express ADGRF1 (35) vs lines expressing it (15) | 2.64× lower at baseline in the lines without ADGRF1 | 0.024 | ⚠ within organs, on part of the lines; also absent: STEAP4, TMPRSS2, TMPRSS4 |
| [[XDH]] | B | XDH activity weakens INPP4B's drug response | lines that do not express XDH (16) vs lines expressing it (23) | the lines without XDH respond 0.79× as strongly (z diff +0.96); strongest at Selinexor 0.5 µM: 2.34x vs 1.55x (z diff -3.3) | 0.046 | ⚠ within organs, on part of the lines; also absent: ENSG00000226281, SYT13, LINC01564; target measured in part of the lines; both ways; artifact flags |
| [[ARHGEF38]] | B | ARHGEF38 activity raises INPP4B's level | lines that do not express ARHGEF38 (36) vs lines expressing it (14) | 2.12× lower at baseline in the lines without ARHGEF38 | 0.048 | ⚠ within organs, on part of the lines; also absent: TMPRSS2, TMEM125, SLC5A1 |
| [[THRB]] | B | THRB activity raises INPP4B's level | lines that do not express THRB (21) vs lines expressing it (29) | 1.97× lower at baseline in the lines without THRB | 0.049 | ⚠ within organs, on part of the lines; also absent: GOLT1A, SIDT1, P2RY2 |
| [[TSPAN1]] | B | TSPAN1 activity strengthens INPP4B's drug response | lines that do not express TSPAN1 (21) vs lines expressing it (18) | the lines without TSPAN1 respond 0.68× as strongly (z diff +1.47); strongest at Homoharringtonine 5 µM: 1.17x vs 0.33x (z diff +9.8) | 0.049 | ⚠ within organs, on part of the lines; also absent: TRIM29, CDH1, IRF6; target measured in part of the lines; both ways; artifact flags |
| [[ITGB6]] | B | ITGB6 activity raises INPP4B's level | lines that do not express ITGB6 (32) vs lines expressing it (18) | 1.82× lower at baseline in the lines without ITGB6 | 0.050 | ⚠ within organs, on part of the lines; also absent: ST14, TMPRSS2, TMPRSS4 |
| [[DENND2D]] | B | DENND2D activity raises INPP4B's level | lines that do not express DENND2D (21) vs lines expressing it (29) | 1.78× lower at baseline in the lines without DENND2D | 0.065 | ⚠ within organs, on part of the lines; also absent: SAMD12, SLC52A3, AREG |

### Downstream of this gene

*15 arrows, 15 of them with an alert ⚠; grade A 0, B 15, C 0. Shown: the 12 strongest; 3 more arrows (3 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EHF]] | B | INPP4B activity raises EHF's level | lines that do not express INPP4B (10) vs lines expressing it (40) | 2.77× lower at baseline in the lines without INPP4B | 0.032 | ⚠ within organs, on part of the lines; also absent: RAB32, CD82, IFIT2 |
| [[ITGB6]] | B | INPP4B activity raises ITGB6's level | lines that do not express INPP4B (10) vs lines expressing it (40) | 2.28× lower at baseline in the lines without INPP4B | 0.035 | ⚠ within organs, on part of the lines; also absent: RAB32, CD82, IFIT2 |
| [[IKZF2]] | B | INPP4B activity raises IKZF2's level | lines that do not express INPP4B (10) vs lines expressing it (40) | 2.11× lower at baseline in the lines without INPP4B | 0.044 | ⚠ within organs, on part of the lines; also absent: RAB32, CD82, IFIT2 |
| [[MECOM]] | B | INPP4B activity raises MECOM's level | lines that do not express INPP4B (10) vs lines expressing it (40) | 2.03× lower at baseline in the lines without INPP4B | 0.074 | ⚠ within organs, on part of the lines; also absent: RAB32, CD82, IFIT2 |
| cells under [[Gemcitabine (drug)]] 5 µM | B | INPP4B activity raises the cells' numbers under Gemcitabine 5 µM (protects the cells) | lines that do not express INPP4B (10) vs lines expressing it (38) | the lines without INPP4B: 0.82× the cells of the other lines | 0.079 | ⚠ within organs, on part of the lines; also absent: RAB32, CD82, IFIT2 |
| cells under [[Medroxyprogesterone acetate (drug)]] 0.5 µM | B | INPP4B activity raises the cells' numbers under Medroxyprogesterone acetate 0.5 µM (protects the cells) | lines that do not express INPP4B (10) vs lines expressing it (38) | the lines without INPP4B: 0.76× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; also absent: RAB32, CD82, IFIT2 |
| cells under [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM | B | INPP4B activity raises the cells' numbers under Dapagliflozin ((2S)-1,2-propanediol, hydrate) 0.05 µM (protects the cells) | lines that do not express INPP4B (10) vs lines expressing it (38) | the lines without INPP4B: 0.85× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; also absent: RAB32, CD82, IFIT2 |
| [[HS3ST1]] | B | INPP4B activity raises HS3ST1's level | lines that do not express INPP4B (10) vs lines expressing it (40) | 2.26× lower at baseline in the lines without INPP4B | 0.081 | ⚠ within organs, on part of the lines; also absent: RAB32, CD82, IFIT2 |
| cells under [[Glycyrrhizic acid (drug)]] 0.05 µM | B | INPP4B activity raises the cells' numbers under Glycyrrhizic acid 0.05 µM (protects the cells) | lines that do not express INPP4B (10) vs lines expressing it (38) | the lines without INPP4B: 0.68× the cells of the other lines | 0.089 | ⚠ within organs, on part of the lines; also absent: RAB32, CD82, IFIT2 |
| [[UCA1]] | B | INPP4B activity raises UCA1's level | lines that do not express INPP4B (10) vs lines expressing it (40) | 2.45× lower at baseline in the lines without INPP4B | 0.090 | ⚠ within organs, on part of the lines; also absent: RAB32, CD82, IFIT2 |
| [[DENND2D]] | B | INPP4B activity raises DENND2D's level | lines that do not express INPP4B (10) vs lines expressing it (40) | 1.40× lower at baseline in the lines without INPP4B | 0.091 | ⚠ within organs, on part of the lines; also absent: RAB32, CD82, IFIT2 |
| [[ARHGEF38]] | B | INPP4B activity raises ARHGEF38's level | lines that do not express INPP4B (10) vs lines expressing it (40) | 2.00× lower at baseline in the lines without INPP4B | 0.091 | ⚠ within organs, on part of the lines; also absent: RAB32, CD82, IFIT2 |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.593). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (27.4, 55.3); signed map (58.7, 1.4). **Vector** length 124, 36.0% of its response variance represented; |z| ≥ 3 in 1,398 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +8.7 | +9.9 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +7.4 | +8.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +6.8 | -0.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +6.5 | -0.5 |
|  | [[Selinexor (drug)]] 0.05 µM |  | +5.8 | +9.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.3 | +4.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.0 | +1.7 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +3.9 | +6.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.0 | +2.7 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +2.4 | +2.3 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -3.8 | -9.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.7 | -3.8 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -3.4 | -4.8 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -3.2 | -3.6 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.5 | -0.9 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.1 | +1.4 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -2.1 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | inositol polyphosphate-4-phosphatase type II B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q31.21 — chr4:142,023,160-142,847,432 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | C2 domain containing; Phosphoinositide phosphatases |
| Hallmark sets | ANDROGEN_RESPONSE, UV_RESPONSE_DN |
| Reactome | 7 pathways, smallest: Synthesis of IP2, IP, and Ins in the cytosol; Synthesis of PIPs at the early endosome membrane; Synthesis of PIPs at the plasma membrane |
| Matched by | ensembl_id |

**Function**, from UniProt [O15327](https://www.uniprot.org/uniprotkb/O15327) (Inositol polyphosphate 4-phosphatase type II):

> Catalyzes the hydrolysis of the 4-position phosphate of phosphatidylinositol 3,4-bisphosphate, inositol 1,3,4-trisphosphate and inositol 3,4-trisphosphate. Plays a role in the late stages of macropinocytosis by dephosphorylating phosphatidylinositol 3,4-bisphosphate in membrane ruffles. The lipid phosphatase activity is critical for tumor suppressor function. Antagonizes the PI3K-AKT/PKB signaling pathway by dephosphorylating phosphoinositides and thereby modulating cell cycle progression and …

**Summary**, from NCBI Gene [8821](https://www.ncbi.nlm.nih.gov/gene/8821):

> INPP4B encodes the inositol polyphosphate 4-phosphatase type II, one of the enzymes involved in phosphatidylinositol signaling pathways. This enzyme removes the phosphate group at position 4 of the inositol ring from inositol 3,4-bisphosphate. There is limited data to suggest that the human type II enzyme is subject to alternative splicing, as has been established for the type I enzyme. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:6075](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6075) · Entrez [8821](https://www.ncbi.nlm.nih.gov/gene/8821) · UniProt [O15327](https://www.uniprot.org/uniprotkb/O15327) · Ensembl [ENSG00000109452](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000109452)

## Data

Gene col 3051: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3051); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3051, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3051]; `tensor/DDL_lfc|DDL_z.npy` [3051]; `embed/gene_vectors.npy` [3051]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3051 or target_col == 3051). Every well: [[INPP4B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/INPP4B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
