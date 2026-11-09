---
symbol: "HAUS8"
type: "gene"
col: 5193
ensembl_id: "ENSG00000131351"
name: "HAUS augmin like complex subunit 8"
location: "19p13.11"
module: 71
arm: "+"
pooled_cpm: 11.94
n_lines_expressing: 50
n_dd_up: 21
n_dd_down: 16
n_dd_up_clean: 7
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/071"]
generated_by: "tahoemap"
---

# HAUS8

*HAUS augmin like complex subunit 8* — 19p13.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (14 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.80× (z +21.3, q 0e+00, up in 40 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (9 with an alert ⚠); the strongest is [[Selinexor (drug)]] 0.5 µM: 0.552× (z -8.7, q 2e-15, down in 31 of 45 measured lines) ⚠ cell-cycle shift, explains ~50% of this change. The strongest without an alert is [[Cobimetinib (drug)]] 5 µM: 0.753× (z -4.0, q 0.004, down in 17 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CDCA5]] (+0.85, fdr 7e-06), [[WDR62]] (+0.82, fdr 7e-06), [[ORC6]] (+0.82, fdr 7e-06).
> It is in [[Module 071]], a single-armed module (Metabolism of non-coding RNA).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 17 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5193.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.80×** | +21.3 | 0e+00 | 40/45 (SW480, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **2.14×** | +11.1 | 3e-26 | 41/47 (SW480, RKO, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~79% of this change | **2.05×** | +10.5 | 2e-23 | 39/47 (SW480, LoVo, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.85×** | +9.0 | 4e-17 | 37/47 (SW480, LoVo, …) | two highest doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~84% of this change | **1.83×** | +8.8 | 2e-16 | 30/47 (SW480, LoVo, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.77×** | +8.4 | 6e-15 | 37/47 (SW480, LoVo, …) | two highest doses | cell-cycle shift (explains ~12% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~88% of this change | **1.46×** | +5.3 | 9e-06 | 20/44 (SNU-423, MIA PaCa-2, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~86% of this change | **1.44×** | +5.1 | 2e-05 | 18/47 (MIA PaCa-2, SW480, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.41×** | +4.7 | 2e-04 | 20/46 (SW480, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.25×** | +4.6 | 2e-04 | 14/48 (MIA PaCa-2, SW480, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **1.37×** | +4.6 | 2e-04 | 17/45 (SNU-1, MIA PaCa-2, …) | all doses, flat | position effect removed |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **1.35×** | +4.4 | 5e-04 | 8/44 (HT-29, A549, …) | rises with dose |  |
| [[Trifluridine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~73% of this change | **1.23×** | +4.3 | 9e-04 | 14/48 (SNU-423, LOX-IMVI, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.09× | +4.1 | 0.002 | 2/48 (NCI-H1792, hTERT-HPNE) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~92% of this change | **1.32×** | +4.1 | 0.002 | 17/47 (A-427, SNU-423, …) | all doses, flat |  |
| [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | **1.24×** | +3.1 | 0.051 | 8/47 (A498, HOP62, …) | inconsistent across doses |  |
| [[DT-061 (drug)]] 5 µM |  | **1.49×** | +3.0 | 0.055 | 2/41 (SW 900, H4) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 9 with an alert ⚠. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5193.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.552×** | -8.7 | 2e-15 | 31/45 (LS 180, A498, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **0.698×** | -7.5 | 2e-11 | 26/47 (A498, A-427, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.583×** | -7.3 | 5e-11 | 20/29 (NCI-H460, J82, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~56% of this change | **0.712×** | -5.0 | 8e-05 | 23/48 (SNU-1, SNU-423, …) | all doses, stronger at high dose |  |
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~78% of this change | **0.667×** | -4.2 | 0.002 | 7/48 (SW480, A498, …) | two highest doses | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.752×** | -4.2 | 0.003 | 18/46 (LS 180, RKO, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.756×** | -4.1 | 0.003 | 20/38 (SHP-77, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.751×** | -4.1 | 0.004 | 9/18 (SW480, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Cobimetinib (drug)]] 5 µM |  | **0.753×** | -4.0 | 0.004 | 17/46 (SK-MEL-2, NCI-H2030, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~75% of this change | **0.769×** | -3.9 | 0.005 | 12/48 (A-427, HOP62, …) | all doses, flat | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.829×** | -3.9 | 0.005 | 19/48 (SW 1271, HOP62, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.771×** | -3.7 | 0.011 | 12/46 (SNU-423, HOP62, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.781×** | -3.4 | 0.034 | 8/47 (HEC-1-A, CHP-212, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.801×** | -3.3 | 0.043 | 14/46 (SK-MEL-2, PANC-1, …) | rises with dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **0.807×** | -3.2 | 0.057 | 9/48 (A-427, NCI-H23, …) | rises with dose | noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 0.861× | -3.1 | 0.059 | 12/48 (SW480, KATO III, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | 0.858× | -3.1 | 0.059 | 18/48 (A-427, SNU-423, …) | all doses, flat |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **0.801×** | -3.1 | 0.062 | 6/46 (SW480, HEC-1-A, …) | inconsistent across doses |  |
| [[Cepharanthine (drug)]] 5 µM |  | 0.865× | -3.0 | 0.069 | 11/48 (BT-474, NCI-H1792, …) | top dose only |  |
| [[Trametinib (drug)]] 0.5 µM |  | 0.855× | -2.9 | 0.097 | 11/48 (A-427, HOP62, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | 0.851× | -2.9 | 0.097 | 10/47 (HOP62, SW480, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.83 per unit of S-phase module lfc, +0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5193. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 18.3 | 2 (1 ⚠) | 3 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.84× (z +12.9) | [[palbociclib (drug)]] 5 µM 0.126× (z -9.5) |
| [[A498 (line)]] | wt | 20.3 | 0 | 4 (4 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.293× (z -12.4) ⚠ cell-cycle shift, explains ~58% of this change |
| [[NCI-H460 (line)]] | wt | 6.51 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.65× (z +9.5) | [[Dinaciclib (drug)]] 0.05 µM 0.127× (z -10.0) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 20.2 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.174× (z -11.1) ⚠ cell-cycle shift, explains ~14% of this change |
| [[A-172 (line)]] | wt | 18.0 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.304× (z -9.2) ⚠ cell-cycle shift, explains ~58% of this change |
| [[A549 (line)]] | wt | 7.99 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.90× (z +10.5) | — |
| [[COLO 205 (line)]] | alt | 11.1 | 0 | 1 | — | [[Saquinavir (drug)]] 0.5 µM 0.0868× (z -9.7) |
| [[HS-578T (line)]] | alt | 12.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.76× (z +10.2) | — |
| [[J82 (line)]] | alt | 19.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.253× (z -8.9) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 7.74 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.60× (z +10.0) | — |
| [[LS 180 (line)]] | wt | 9.39 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 0.5 µM 0.0645× (z -12.5) ⚠ cell-cycle shift, explains ~50% of this change |
| [[MIA PaCa-2 (line)]] | alt | 13.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.44× (z +10.3) | — |
| [[NCI-H2347 (line)]] | alt | 5.92 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.14× (z +10.1) | — |
| [[Panc 03.27 (line)]] | alt | 14.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.04× (z +12.9) | — |
| [[PANC-1 (line)]] | alt | 11.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.89× (z +10.7) | — |
| [[RKO (line)]] | wt | 16.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.66× (z +9.9) | — |
| [[SHP-77 (line)]] | alt | 29.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.101× (z -14.8) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 9.92 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.01× (z +10.0) | — |
| [[SW1417 (line)]] | alt | 9.72 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.144× (z -9.6) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[AN3 CA (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.59 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 8.34 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.97 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.99 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 13.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.09 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.65 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.44 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.48 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 8.32 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 7.96 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.61 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.48 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.96 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.53 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 9.27 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.95 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.63 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 13.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5193), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDCA5]] | +0.85 | +0.80 / +0.86 | both halves | 7e-06 | pathway: Mitotic Prometaphase |
| [[WDR62]] | +0.82 | +0.79 / +0.83 | both halves | 7e-06 | **novel candidate** |
| [[ORC6]] | +0.82 | +0.77 / +0.85 | both halves | 7e-06 | **novel candidate** |
| [[CENPO]] | +0.81 | +0.81 / +0.84 | both halves | 7e-06 | pathway: Mitotic Prometaphase |
| [[RFWD3]] | +0.80 | +0.75 / +0.81 | both halves | 7e-06 |  |
| [[TRAIP]] | +0.79 | +0.76 / +0.79 | both halves | 7e-06 | **novel candidate** |
| [[POLQ]] | +0.79 | +0.84 / +0.76 | both halves | 7e-06 |  |
| [[ATAD5]] | +0.78 | +0.78 / +0.80 | both halves | 7e-06 |  |
| [[POC1A]] | +0.77 | +0.65 / +0.81 | both halves | 7e-06 |  |
| [[RAD51]] | +0.76 | +0.77 / +0.76 | both halves | 7e-06 |  |
| [[ASF1B]] | +0.76 | +0.64 / +0.80 | both halves | 7e-06 |  |
| [[CHAF1A]] | +0.76 | +0.77 / +0.78 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 3, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers HAUS8's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.9% of all compounds | 0.020 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[MAP2K1]] | B | MAP2K1 activity raises HAUS8's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 2.2% of all compounds | 0.037 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[CDC25A]] | B | CDC25A activity raises HAUS8's level | lines that do not express CDC25A (5) vs lines expressing it (45) | 1.98× lower at baseline in the lines without CDC25A | 0.060 | ⚠ within organs, on part of the lines; also absent: ZNF367, E2F1, ALDH1B1; maybe low, not absent |
| [[DSCC1]] | C | DSCC1 activity raises HAUS8's level | lines that do not express DSCC1 (4) vs lines expressing it (46) | 1.91× lower at baseline in the lines without DSCC1 | 0.025 | ⚠ few lines (4 vs 46); across organs; also absent: NDC80, ADGRL1, MYBL2; maybe low, not absent |
| [[ZNF367]] | C | ZNF367 activity raises HAUS8's level | lines that do not express ZNF367 (4) vs lines expressing it (46) | 2.04× lower at baseline in the lines without ZNF367 | 0.079 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CDC25A; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 071]] — Metabolism of non-coding RNA; 70 genes; every member is in the + arm (projection on the module's main direction 0.836). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-35.8, -48.5); signed map (-41.7, -43.6). **Vector** length 105, 24.9% of its response variance represented; |z| ≥ 3 in 1,060 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *IP3 and IP4 transport between cytosol and nucleus* (reactome, mean cos +0.50 to 4); *IP6 and IP7 transport between cytosol and nucleus* (reactome, mean cos +0.50 to 4); *IPs transport between nucleus and cytosol* (reactome, mean cos +0.50 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.2 | +21.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +4.1 | +8.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.9 | +9.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~88% of this change | +3.0 | +5.3 |
|  | [[Trifluridine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~73% of this change | +2.7 | +4.3 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | +1.7 | +3.1 |
|  | [[Cytarabine (drug)]] 0.05 µM |  | +1.6 | +1.5 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +1.6 | +2.8 |
|  | [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | +1.5 | +1.8 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | -8.2 | -7.5 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~50% of this change | -6.6 | -8.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -4.2 | -7.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.2 | -3.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -4.0 | -4.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.9 | -1.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -2.6 | -3.7 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -2.5 | -3.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.5 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | HAUS augmin like complex subunit 8 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.11 — chr19:17,049,729-17,075,625 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC20533, NY-SAR-48; previously HICE1 |
| Gene groups (HGNC) | HAUS augmin like complex |
| Reactome | 17 pathways, smallest: Loss of Nlp from mitotic centrosomes; Loss of proteins required for interphase microtubule organization from the centrosome; AURKA Activation by TPX2 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BT25](https://www.uniprot.org/uniprotkb/Q9BT25) (HAUS augmin-like complex subunit 8):

> Contributes to mitotic spindle assembly, maintenance of centrosome integrity and completion of cytokinesis as part of the HAUS augmin-like complex.

**Summary**, from NCBI Gene [93323](https://www.ncbi.nlm.nih.gov/gene/93323):

> HAUS8 is 1 of 8 subunits of the 390-kD human augmin complex, or HAUS complex. The augmin complex was first identified in Drosophila, and its name comes from the Latin verb 'augmentare,' meaning 'to increase.' The augmin complex is a microtubule-binding complex involved in microtubule generation within the mitotic spindle and is vital to mitotic spindle assembly (Goshima et al., 2008 [PubMed 18443220]; Uehara et al., 2009 [PubMed 19369198]).[supplied by OMIM, Jun 2010]

**Accessions** — [HGNC:30532](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30532) · Entrez [93323](https://www.ncbi.nlm.nih.gov/gene/93323) · UniProt [Q9BT25](https://www.uniprot.org/uniprotkb/Q9BT25) · Ensembl [ENSG00000131351](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000131351)

## Data

Gene col 5193: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5193); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5193, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5193]; `tensor/DDL_lfc|DDL_z.npy` [5193]; `embed/gene_vectors.npy` [5193]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5193 or target_col == 5193). Every well: [[HAUS8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HAUS8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
