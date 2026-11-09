---
symbol: "VRK2"
type: "gene"
col: 381
ensembl_id: "ENSG00000028116"
name: "VRK serine/threonine kinase 2"
location: "2p16.1"
module: 40
arm: "-"
pooled_cpm: 118.22
n_lines_expressing: 46
n_dd_up: 0
n_dd_down: 13
n_dd_up_clean: 0
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 2
direction_downstream: 12
tags: ["gene", "module/040"]
generated_by: "tahoemap"
---

# VRK2

*VRK serine/threonine kinase 2* — 2p16.1

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Selinexor (drug)]] 5 µM in 1 line (PANC-1 1.51×; ⚠ cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (LoVo 1.84×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.322× (z -32.2, q 0e+00, down in 44 of 44 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[VPS36]] (+0.62, fdr 1e-05), [[ZNF326]] (+0.58, fdr 1e-05), [[HACD2]] (+0.57, fdr 3e-05); moves opposite to [[ATG101]] (-0.56, fdr 4e-05), [[NAB2]] (-0.56, fdr 3e-05), [[SEC16A]] (-0.55, fdr 3e-05).
> It sits in the **-** arm of [[Module 040]] (Asparagine N-linked glycosylation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 12 go from it, the strongest it → cells under [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 7 with an alert ⚠. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 381.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Selinexor (drug)]] 5 µM in 1 line (PANC-1 1.51×; ⚠ cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (LoVo 1.84×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~39% of this change | 1.20× | +5.1 | 1e-04 | 19/45 (PANC-1, C-33 A, …) | all doses, flat |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.13× | +4.9 | 1e-04 | 10/44 (A498, MIA PaCa-2, …) | rises with dose |  |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | 1.19× | +4.9 | 1e-04 | 18/44 (C-33 A, PANC-1, …) | top dose only |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~64% of this change | 1.19× | +4.9 | 1e-04 | 20/44 (PANC-1, C-33 A, …) | all doses, flat |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | 1.20× | +4.9 | 1e-04 | 17/44 (SW 900, NCI-H460, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +4.8 | 2e-04 | 18/44 (hTERT-HPNE, NCI-H2347, …) | two highest doses |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | 1.17× | +4.5 | 5e-04 | 15/46 (NCI-H1573, A549, …) | rises with dose | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | 1.17× | +4.3 | 0.001 | 18/44 (LoVo, HepG2/C3A, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 1.16× | +4.0 | 0.005 | 15/44 (LOX-IMVI, A549, …) | all doses, flat |  |
| [[Belumosudil (drug)]] 5 µM |  | 1.15× | +3.8 | 0.007 | 18/44 (PANC-1, HS-578T, …) | top dose only |  |
| [[Neratinib (drug)]] 5 µM |  | 1.14× | +3.6 | 0.015 | 15/44 (NCI-H460, A498, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | 1.13× | +3.5 | 0.024 | 14/45 (A-427, SW 900, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 1.15× | +3.4 | 0.028 | 11/44 (A-427, C32, …) | all doses, flat |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | 1.13× | +3.3 | 0.046 | 18/44 (SNU-1, SHP-77, …) | two highest doses |  |
| [[Trametinib (drug)]] 0.5 µM |  | 1.09× | +3.2 | 0.046 | 6/44 (A-427, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | 1.11× | +3.1 | 0.072 | 12/44 (SW1417, SW 900, …) | inconsistent across doses | low cells (technical?) |
| [[Cobimetinib (drug)]] 5 µM |  | 1.12× | +3.1 | 0.073 | 16/44 (A-427, BT-474, …) | rises with dose |  |
| [[Verteporfin (drug)]] 5 µM |  | 1.12× | +3.0 | 0.073 | 12/45 (A-427, NCI-H2030, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 5 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 381.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.322×** | -32.2 | 0e+00 | 44/44 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.362×** | -28.8 | 0e+00 | 44/44 (SW480, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.378×** | -27.6 | 0e+00 | 44/44 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.542×** | -17.4 | 0e+00 | 41/44 (SW 900, HEC-1-A, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.669×** | -16.1 | 0e+00 | 38/45 (A549, LS 180, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.719×** | -13.2 | 5e-38 | 33/44 (RPMI-7951, NCI-H1792, …) | top dose only | composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.640×** | -12.4 | 2e-33 | 41/44 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.661×** | -11.7 | 7e-30 | 37/44 (PANC-1, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.498×** | -10.3 | 3e-23 | 37/45 (NCI-H1792, NCI-H23, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.734×** | -8.4 | 2e-15 | 28/44 (LS 180, NCI-H460, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.815×** | -8.2 | 1e-14 | 26/44 (SW1417, HEC-1-A, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **0.676×** | -5.8 | 3e-07 | 22/45 (MIA PaCa-2, A549, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~38% of this change | **0.826×** | -5.4 | 3e-06 | 23/44 (NCI-H2030, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.949× | -4.9 | 3e-05 | 0/46 | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~69% of this change | 0.853× | -4.3 | 6e-04 | 20/46 (LS 180, NCI-H460, …) | top dose only |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 0.882× | -3.5 | 0.014 | 10/45 (LS 180, Hs 766T, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.916× | -3.5 | 0.015 | 9/44 (SW480, RKO, …) | top dose only |  |
| [[Belinostat (drug)]] 0.05 µM |  | 0.891× | -3.2 | 0.044 | 10/44 (HepG2/C3A, SNU-423, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.29 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 381. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 174 | 0 | 9 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.191× (z -24.7) |
| [[HEC-1-A (line)]] | alt | 112 | 0 | 6 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.388× (z -15.8) |
| [[HS-578T (line)]] | alt | 77.4 | 0 | 6 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.180× (z -18.1) |
| [[MIA PaCa-2 (line)]] | alt | 96.3 | 0 | 6 | — | [[Panobinostat (drug)]] 5 µM 0.217× (z -21.9) |
| [[NCI-H2030 (line)]] | alt | 260 | 0 | 6 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.292× (z -17.3) |
| [[NCI-H23 (line)]] | alt | 133 | 0 | 6 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.335× (z -14.7) |
| [[PANC-1 (line)]] | alt | 102 | 1 (1 ⚠) | 5 | [[Selinexor (drug)]] 5 µM 1.51× (z +9.9) ⚠ cell-cycle shift, would explain all of this change | [[Panobinostat (drug)]] 0.5 µM 0.340× (z -18.4) |
| [[SW480 (line)]] | alt | 128 | 0 | 6 | — | [[Panobinostat (drug)]] 5 µM 0.180× (z -30.7) |
| [[A549 (line)]] | wt | 248 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.141× (z -22.5) |
| [[NCI-H1792 (line)]] | alt | 343 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.321× (z -15.2) ⚠ cell-cycle shift, explains ~24% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.204× (z -15.0) |
| [[NCI-H2347 (line)]] | alt | 91.3 | 0 | 5 | — | [[Panobinostat (drug)]] 0.5 µM 0.407× (z -13.3) |
| [[A-427 (line)]] | wt | 152 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.478× (z -10.9) |
| [[A498 (line)]] | wt | 137 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.296× (z -18.8) |
| [[C32 (line)]] | wt | 103 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.323× (z -12.7) |
| [[HepG2_C3A (line)]] | wt | 112 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.290× (z -13.3) |
| [[Hs 766T (line)]] | wt | 102 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.225× (z -16.1) |
| [[LoVo (line)]] | wt | 115 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 1.84× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | [[Panobinostat (drug)]] 5 µM 0.332× (z -16.0) |
| [[LOX-IMVI (line)]] | wt | 83.5 | 0 | 4 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.324× (z -15.4) |
| [[LS 180 (line)]] | wt | 156 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.254× (z -19.7) |
| [[Panc 03.27 (line)]] | alt | 108 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.223× (z -17.4) |
| [[SK-MEL-2 (line)]] | alt | 80.6 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.346× (z -11.5) |
| [[SNU-1 (line)]] | wt | 118 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.273× (z -12.3) |
| [[SW 900 (line)]] | alt | 108 | 0 | 4 | — | [[Auranofin (drug)]] 5 µM 0.297× (z -13.3) |
| [[SW1417 (line)]] | alt | 139 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.382× (z -13.4) |
| [[AsPC-1 (line)]] | alt | 256 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.242× (z -14.8) |
| [[C-33 A (line)]] | alt | 78.7 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.288× (z -12.0) |
| [[CFPAC-1 (line)]] | alt | 93.1 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.542× (z -10.0) |
| [[HT-29 (line)]] | alt | 65.6 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.396× (z -10.4) |
| [[J82 (line)]] | alt | 47.9 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.322× (z -12.4) |
| [[KATO III (line)]] | alt | 140 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.191× (z -22.1) |
| [[RKO (line)]] | wt | 83.7 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.267× (z -14.6) |
| [[SNU-423 (line)]] | alt | 52.8 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.262× (z -12.7) |
| [[SW48 (line)]] | wt | 131 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.186× (z -16.9) |
| [[BT-474 (line)]] | alt | 65.0 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.364× (z -10.0) |
| [[COLO 205 (line)]] | alt | 64.2 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.382× (z -8.6) |
| [[HCT15 (line)]] | alt | 112 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.321× (z -11.6) |
| [[HOP62 (line)]] | alt | 44.8 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.388× (z -9.8) |
| [[NCI-H1573 (line)]] | alt | 127 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.508× (z -12.2) ⚠ cell-cycle shift, explains ~24% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.518× (z -11.9) |
| [[SHP-77 (line)]] | alt | 92.1 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.441× (z -9.3) |
| [[AN3 CA (line)]] | alt | 83.4 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.212× (z -10.0) |
| [[NCI-H596 (line)]] | alt | 117 | 0 | 1 | — | [[L-Eflornithine (monohydrochloride) (drug)]] 0.05 µM 0.178× (z -10.8) |
| [[RPMI-7951 (line)]] | alt | 76.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.310× (z -15.3) ⚠ cell-cycle shift, explains ~24% of this change |
| [[A-172 (line)]] | wt | 11.6 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 14.1 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 13.6 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 59.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 142 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 135 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 22.1 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 120 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 381), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*56 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VPS36]] | +0.62 | +0.70 / +0.54 | both halves | 1e-05 |  |
| [[ZNF326]] | +0.58 | +0.49 / +0.54 | both halves | 1e-05 |  |
| [[HACD2]] | +0.57 | +0.45 / +0.54 | both halves | 3e-05 |  |
| [[PAIP1]] | +0.56 | +0.48 / +0.53 | both halves | 2e-05 |  |
| [[FAIM]] | +0.56 | +0.44 / +0.46 | both halves | 3e-05 |  |
| [[RWDD3]] | +0.54 | +0.52 / +0.39 | both halves | 5e-05 |  |
| [[USP46]] | +0.53 | +0.45 / +0.45 | both halves | 3e-05 |  |
| [[NAE1]] | +0.53 | +0.58 / +0.44 | both halves | 3e-05 |  |
| [[DENND1B]] | +0.53 | +0.53 / +0.47 | both halves | 2e-05 |  |
| [[DCAF17]] | +0.53 | +0.39 / +0.50 | both halves | 6e-05 |  |
| [[TADA2A]] | +0.53 | +0.52 / +0.43 | both halves | 3e-05 |  |
| [[SLTM]] | +0.52 | +0.45 / +0.47 | both halves | 3e-05 |  |

## Genes that move opposite

*44 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATG101]] | -0.56 | -0.41 / -0.58 | both halves | 4e-05 |  |
| [[NAB2]] | -0.56 | -0.44 / -0.43 | both halves | 3e-05 |  |
| [[SEC16A]] | -0.55 | -0.46 / -0.54 | both halves | 3e-05 |  |
| [[ASMTL]] | -0.55 | -0.56 / -0.46 | both halves | 3e-05 |  |
| [[ELK1]] | -0.54 | -0.52 / -0.39 | both halves | 6e-05 |  |
| [[TGFB1]] | -0.54 | -0.40 / -0.52 | both halves | 5e-05 |  |
| [[NCKAP5L]] | -0.53 | -0.47 / -0.49 | both halves | 2e-05 |  |
| [[WDR26]] | -0.53 | -0.59 / -0.48 | both halves | 2e-05 |  |
| [[DMPK]] | -0.52 | -0.49 / -0.49 | both halves | 1e-05 |  |
| [[ZKSCAN5]] | -0.52 | -0.55 / -0.45 | both halves | 3e-05 |  |
| [[ELL]] | -0.52 | -0.36 / -0.53 | both halves | 9e-05 |  |
| [[FER1L4]] | -0.51 | -0.47 / -0.50 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises VRK2's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Idarubicin, Mitoxantrone) | 60% of the class's compounds vs 2.8% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[SLC9B2]] | C | SLC9B2 activity raises VRK2's level | lines that do not express SLC9B2 (3) vs lines expressing it (47) | 1.33× lower at baseline in the lines without SLC9B2 | 0.087 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: TMEM132A, HOMER3, SOAT1; maybe low, not absent |

### Downstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 0, C 12.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM | C | VRK2 activity raises the cells' numbers under Mitoxantrone (dihydrochloride) 0.5 µM (protects the cells) | lines that do not express VRK2 (4) vs lines expressing it (44) | the lines without VRK2: 0.64× the cells of the other lines | 0.002 | ⚠ few lines (4 vs 46); tissue-confounded; across organs; also absent: PTER, ZC3HAV1L, OSR2 |
| cells under [[Topotecan (hydrochloride) (drug)]] 0.5 µM | C | VRK2 activity raises the cells' numbers under Topotecan (hydrochloride) 0.5 µM (protects the cells) | lines that do not express VRK2 (4) vs lines expressing it (44) | the lines without VRK2: 0.67× the cells of the other lines | 0.002 | ⚠ few lines (4 vs 46); tissue-confounded; across organs; also absent: PTER, ZC3HAV1L, OSR2 |
| cells under [[Amsacrine (drug)]] 5 µM | C | VRK2 activity raises the cells' numbers under Amsacrine 5 µM (protects the cells) | lines that do not express VRK2 (4) vs lines expressing it (44) | the lines without VRK2: 0.74× the cells of the other lines | 0.012 | ⚠ few lines (4 vs 46); tissue-confounded; across organs; also absent: PTER, ZC3HAV1L, OSR2 |
| cells under [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM | C | VRK2 activity raises the cells' numbers under Fedratinib (hydrochloride hydrate) 5 µM (protects the cells) | lines that do not express VRK2 (4) vs lines expressing it (44) | the lines without VRK2: 0.69× the cells of the other lines | 0.022 | ⚠ few lines (4 vs 46); tissue-confounded; across organs; also absent: PTER, ZC3HAV1L, OSR2 |
| cells under [[Bortezomib (drug)]] 0.5 µM | C | VRK2 activity raises the cells' numbers under Bortezomib 0.5 µM (protects the cells) | lines that do not express VRK2 (4) vs lines expressing it (44) | the lines without VRK2: 0.77× the cells of the other lines | 0.025 | ⚠ few lines (4 vs 46); tissue-confounded; across organs; also absent: PTER, ZC3HAV1L, OSR2 |
| cells under [[Elimusertib hydrochloride (drug)]] 0.05 µM | C | VRK2 activity raises the cells' numbers under Elimusertib hydrochloride 0.05 µM (protects the cells) | lines that do not express VRK2 (4) vs lines expressing it (44) | the lines without VRK2: 0.74× the cells of the other lines | 0.034 | ⚠ few lines (4 vs 46); tissue-confounded; across organs; also absent: PTER, ZC3HAV1L, OSR2 |
| cells under [[Elimusertib hydrochloride (drug)]] 5 µM | C | VRK2 activity raises the cells' numbers under Elimusertib hydrochloride 5 µM (protects the cells) | lines that do not express VRK2 (4) vs lines expressing it (44) | the lines without VRK2: 0.68× the cells of the other lines | 0.036 | ⚠ few lines (4 vs 46); tissue-confounded; across organs; also absent: PTER, ZC3HAV1L, OSR2 |
| cells under [[Tucidinostat (drug)]] 5 µM | C | VRK2 activity raises the cells' numbers under Tucidinostat 5 µM (protects the cells) | lines that do not express VRK2 (4) vs lines expressing it (44) | the lines without VRK2: 0.85× the cells of the other lines | 0.041 | ⚠ few lines (4 vs 46); tissue-confounded; across organs; also absent: PTER, ZC3HAV1L, OSR2 |
| cells under [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | C | VRK2 activity raises the cells' numbers under Idarubicin (hydrochloride) 0.5 µM (protects the cells) | lines that do not express VRK2 (4) vs lines expressing it (44) | the lines without VRK2: 0.67× the cells of the other lines | 0.049 | ⚠ few lines (4 vs 46); tissue-confounded; across organs; also absent: PTER, ZC3HAV1L, OSR2 |
| cells under [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM | C | VRK2 activity raises the cells' numbers under Trametinib (DMSO_TF solvate) 5 µM (protects the cells) | lines that do not express VRK2 (4) vs lines expressing it (44) | the lines without VRK2: 0.77× the cells of the other lines | 0.063 | ⚠ few lines (4 vs 46); tissue-confounded; across organs; also absent: PTER, ZC3HAV1L, OSR2 |
| cells under [[Dabrafenib (drug)]] 5 µM | C | VRK2 activity lowers the cells' numbers under Dabrafenib 5 µM (makes them more sensitive) | lines that do not express VRK2 (4) vs lines expressing it (44) | the lines without VRK2: 1.41× the cells of the other lines | 0.068 | ⚠ few lines (4 vs 46); tissue-confounded; across organs; also absent: PTER, ZC3HAV1L, OSR2 |
| cells under [[Cabozantinib (S-malate) (drug)]] 5 µM | C | VRK2 activity raises the cells' numbers under Cabozantinib (S-malate) 5 µM (protects the cells) | lines that do not express VRK2 (4) vs lines expressing it (44) | the lines without VRK2: 0.78× the cells of the other lines | 0.083 | ⚠ few lines (4 vs 46); tissue-confounded; across organs; also absent: PTER, ZC3HAV1L, OSR2 |

## Where it sits

- **Module**: [[Module 040]] — Asparagine N-linked glycosylation; 111 genes; this gene is in the **-** arm (projection on the module's main direction -0.204). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (21.5, -28.4); signed map (12.4, -36.6). **Vector** length 109, 30.0% of its response variance represented; |z| ≥ 3 in 1,198 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +7.7 | +2.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | +6.5 | +3.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +5.4 | +4.8 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~64% of this change | +4.4 | +4.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.0 | +2.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.6 | +3.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +3.2 | +3.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.2 | +3.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +3.1 | +4.0 |
| fall | [[Auranofin (drug)]] 5 µM |  | -7.6 | -17.4 |
|  | [[TAK-901 (drug)]] 5 µM |  | -5.7 | -10.3 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -5.2 | -11.7 |
|  | [[Belinostat (drug)]] 5 µM |  | -3.7 | -27.6 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -3.6 | -28.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.5 | -2.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.4 | -8.2 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -2.3 | -2.7 |
|  | [[Filgotinib (drug)]] 0.05 µM |  | -2.1 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | VRK serine/threonine kinase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p16.1 — chr2:57,907,629-58,159,920 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | VRK serine/threonine kinase family |
| Reactome | 17 pathways, smallest: Initiation of Nuclear Envelope (NE) Reformation; RHOD GTPase cycle; Nuclear Envelope Breakdown |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86Y07](https://www.uniprot.org/uniprotkb/Q86Y07) (Serine/threonine-protein kinase VRK2):

> Serine/threonine kinase that regulates several signal transduction pathways. Isoform 1 modulates the stress response to hypoxia and cytokines, such as interleukin-1 beta (IL1B) and this is dependent on its interaction with MAPK8IP1, which assembles mitogen-activated protein kinase (MAPK) complexes. Inhibition of signal transmission mediated by the assembly of MAPK8IP1-MAPK complexes reduces JNK phosphorylation and JUN-dependent transcription. Phosphorylates 'Thr-18' of p53/TP53, histone H3, and …

**Summary**, from NCBI Gene [7444](https://www.ncbi.nlm.nih.gov/gene/7444):

> This gene encodes a member of the vaccinia-related kinase (VRK) family of serine/threonine protein kinases. The encoded protein acts as an effector of signaling pathways that regulate apoptosis and tumor cell growth. Variants in this gene have been associated with schizophrenia. Alternative splicing results in multiple transcript variants that differ in their subcellular localization and biological activity. [provided by RefSeq, Jan 2014]

**Accessions** — [HGNC:12719](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12719) · Entrez [7444](https://www.ncbi.nlm.nih.gov/gene/7444) · UniProt [Q86Y07](https://www.uniprot.org/uniprotkb/Q86Y07) · Ensembl [ENSG00000028116](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000028116)

## Data

Gene col 381: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 381); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 381, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 381]; `tensor/DDL_lfc|DDL_z.npy` [381]; `embed/gene_vectors.npy` [381]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 381 or target_col == 381). Every well: [[VRK2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/VRK2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
