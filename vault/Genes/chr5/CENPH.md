---
symbol: "CENPH"
type: "gene"
col: 7682
ensembl_id: "ENSG00000153044"
name: "centromere protein H"
location: "5q13.2"
module: 6
arm: "+"
pooled_cpm: 16.38
n_lines_expressing: 50
n_dd_up: 24
n_dd_down: 7
n_dd_up_clean: 4
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 10
direction_downstream: 0
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# CENPH

*centromere protein H* — 5q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (20 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.38× (z +20.4, q 0e+00, up in 40 of 40 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change. The strongest without an alert is [[Retinoic acid (drug)]] 0.05 µM: 1.37× (z +4.4, q 6e-04, up in 19 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (4 with an alert ⚠); the strongest is [[Neratinib (maleate) (drug)]] 5 µM: 0.765× (z -5.1, q 1e-04, down in 20 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KNTC1]] (+0.86, fdr 7e-06), [[MYBL2]] (+0.86, fdr 7e-06), [[FANCD2]] (+0.84, fdr 7e-06).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[E2F2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 21 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 20 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7682.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | **4.38×** | +20.4 | 0e+00 | 40/40 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | **3.63×** | +17.2 | 0e+00 | 22/25 (PANC-1, A549, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **2.96×** | +13.9 | 1e-41 | 30/35 (PANC-1, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.89×** | +12.2 | 4e-32 | 37/46 (NCI-H2347, CFPAC-1, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **1.66×** | +6.7 | 2e-09 | 27/48 (SW480, MIA PaCa-2, …) | top dose only | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~51% of this change | **1.58×** | +6.4 | 2e-08 | 23/40 (PANC-1, LoVo, …) | inconsistent across doses | low cells (technical?) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.57×** | +6.3 | 3e-08 | 24/48 (LoVo, A549, …) | rises with dose | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~50% of this change | **1.50×** | +5.4 | 4e-06 | 22/42 (MIA PaCa-2, SW480, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~82% of this change | **1.48×** | +5.2 | 1e-05 | 22/47 (A-172, MIA PaCa-2, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.41×** | +4.7 | 1e-04 | 19/48 (A549, LoVo, …) | rises with dose | position effect removed |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~84% of this change | **1.26×** | +4.4 | 5e-04 | 15/48 (HS-578T, PANC-1, …) | top dose only |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.37×** | +4.4 | 6e-04 | 19/48 (LoVo, A498, …) | inconsistent across doses |  |
| [[Raltitrexed (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~72% of this change | **1.25×** | +4.3 | 6e-04 | 14/48 (LoVo, SW480, …) | rises with dose | position effect removed |
| [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~74% of this change | **1.35×** | +4.1 | 0.001 | 13/48 (LoVo, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Trifluridine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~75% of this change | **1.33×** | +4.0 | 0.002 | 12/48 (SW480, NCI-H460, …) | rises with dose |  |
| [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | **1.28×** | +3.4 | 0.015 | 11/48 (A498, PANC-1, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.19× | +3.4 | 0.015 | 16/48 (SW480, J82, …) | top dose only |  |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | **1.28×** | +3.4 | 0.015 | 14/48 (A-172, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.27×** | +3.2 | 0.034 | 16/47 (LoVo, C32, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 4 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7682.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.765×** | -5.1 | 1e-04 | 20/48 (HCT15, Hs 766T, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~97% of this change | **0.767×** | -5.1 | 1e-04 | 21/48 (A-172, HT-29, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~62% of this change | **0.695×** | -4.7 | 4e-04 | 21/47 (PANC-1, A-172, …) | inconsistent across doses |  |
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~78% of this change | **0.648×** | -4.3 | 0.003 | 11/48 (HT-29, SW480, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.754×** | -3.9 | 0.011 | 18/48 (NCI-H460, A-427, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.778×** | -3.5 | 0.051 | 19/46 (A-427, Hs 766T, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Temsirolimus (drug)]] 0.5 µM |  | **0.783×** | -3.4 | 0.061 | 20/45 (HOP62, Hs 766T, …) | two highest doses |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 0.800× | -3.1 | 0.14 | 12/47 (NCI-H2030, RKO, …) | two highest doses | low cells (technical?) |
| [[Terfenadine (drug)]] 5 µM |  | 0.849× | -3.1 | 0.14 | 7/48 (SW 1088, MIA PaCa-2, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.80 per unit of S-phase module lfc, +0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7682. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 11.9 | 3 (3 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 6.24× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | [[Selinexor (drug)]] 5 µM 0.297× (z -9.1) ⚠ cell-cycle shift, explains ~97% of this change |
| [[PANC-1 (line)]] | alt | 27.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.38× (z +15.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | — |
| [[A-427 (line)]] | wt | 40.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0919× (z -17.9) |
| [[A498 (line)]] | wt | 16.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.90× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | — |
| [[A549 (line)]] | wt | 11.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.96× (z +10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | — |
| [[LoVo (line)]] | wt | 12.0 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.21× (z +9.6) ⚠ cell-cycle shift, would explain all of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 19.7 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.99× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | [[Homoharringtonine (drug)]] 5 µM 0.202× (z -12.0) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H2347 (line)]] | alt | 16.0 | 2 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.42× (z +12.0) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[NCI-H460 (line)]] | wt | 15.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.08× (z +10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | — |
| [[SNU-423 (line)]] | alt | 12.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.57× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | — |
| [[SW480 (line)]] | alt | 26.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.33× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | — |
| [[A-172 (line)]] | wt | 22.3 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.297× (z -9.6) ⚠ cell-cycle shift, explains ~97% of this change |
| [[AsPC-1 (line)]] | alt | 4.63 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.55× (z +8.8) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[CFPAC-1 (line)]] | alt | 9.23 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.19× (z +9.5) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[HCT15 (line)]] | alt | 21.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0620× (z -12.9) |
| [[HEC-1-A (line)]] | alt | 23.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.54× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | — |
| [[Hs 766T (line)]] | wt | 10.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0391× (z -13.7) |
| [[KATO III (line)]] | alt | 14.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.15× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | — |
| [[NCI-H2030 (line)]] | alt | 16.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.37× (z +10.9) ⚠ cell-cycle shift, would explain all of this change | — |
| [[Panc 03.27 (line)]] | alt | 11.3 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.12× (z +9.1) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[AN3 CA (line)]] | alt | 33.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 36.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 9.33 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 9.82 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 14.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.45 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 7.59 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 9.61 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.11 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 14.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 7.64 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.71 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.85 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 19.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 30.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.23 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 13.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7682), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KNTC1]] | +0.86 | +0.83 / +0.85 | both halves | 7e-06 | pathway: Amplification  of signal from unattached  kinetochores via a MAD2  inhibitory signal; STRING 587 |
| [[MYBL2]] | +0.86 | +0.82 / +0.87 | both halves | 7e-06 |  |
| [[FANCD2]] | +0.84 | +0.84 / +0.83 | both halves | 7e-06 |  |
| [[MCM4]] | +0.84 | +0.82 / +0.83 | both halves | 7e-06 | pathway: Cell Cycle Checkpoints; STRING 420 |
| [[HELLS]] | +0.83 | +0.81 / +0.82 | both halves | 7e-06 | STRING 415 |
| [[TIMELESS]] | +0.83 | +0.81 / +0.82 | both halves | 7e-06 | **novel candidate** |
| [[CENPU]] | +0.83 | +0.85 / +0.84 | both halves | 7e-06 | same gene group; pathway: Amplification  of signal from unattached  kinetochores via a MAD2  inhibitory signal; STRING 999 |
| [[XRCC2]] | +0.83 | +0.78 / +0.84 | both halves | 7e-06 |  |
| [[ESCO2]] | +0.83 | +0.82 / +0.81 | both halves | 7e-06 | STRING 443 |
| [[ZWINT]] | +0.83 | +0.82 / +0.82 | both halves | 7e-06 | pathway: Amplification  of signal from unattached  kinetochores via a MAD2  inhibitory signal; STRING 613 |
| [[RAD51AP1]] | +0.82 | +0.75 / +0.86 | both halves | 7e-06 | STRING 705 |
| [[TRIP13]] | +0.81 | +0.78 / +0.77 | both halves | 7e-06 | STRING 511 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 4, C 6.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[E2F2]] | B | E2F2 activity raises CENPH's level | lines that do not express E2F2 (13) vs lines expressing it (37) | 1.85× lower at baseline in the lines without E2F2 | 0.020 | ⚠ within organs, on part of the lines; also absent: ENSG00000260498, ABHD11, BRSK2; maybe low, not absent |
| [[TCF19]] | B | TCF19 activity raises CENPH's level | lines that do not express TCF19 (5) vs lines expressing it (45) | 2.22× lower at baseline in the lines without TCF19 | 0.031 | ⚠ within organs, on part of the lines; also absent: CLSPN, AURKB, SMARCD3; maybe low, not absent |
| [[E2F8]] | B | E2F8 activity raises CENPH's level | lines that do not express E2F8 (5) vs lines expressing it (45) | 2.04× lower at baseline in the lines without E2F8 | 0.043 | ⚠ across organs; also absent: CYB561, NMRAL1, RRM2; maybe low, not absent |
| [[MYBL1]] | B | MYBL1 activity raises CENPH's level | lines that do not express MYBL1 (8) vs lines expressing it (42) | 1.73× lower at baseline in the lines without MYBL1 | 0.060 | ⚠ within organs, on part of the lines; also absent: NCS1, KCNC4, JAZF1; maybe low, not absent |
| [[DSCC1]] | C | DSCC1 activity raises CENPH's level | lines that do not express DSCC1 (4) vs lines expressing it (46) | 2.26× lower at baseline in the lines without DSCC1 | 0.018 | ⚠ few lines (4 vs 46); across organs; also absent: NDC80, ADGRL1, MYBL2; maybe low, not absent |
| [[C21orf58]], [[CDC45]], [[CENPM]], [[SKA3]] | C | C21orf58, CDC45, CENPM, SKA3 activity raises CENPH's level | lines that do not express C21orf58, CDC45, CENPM, SKA3 (3) vs lines expressing them (47) | 2.70× lower at baseline in the lines without C21orf58, CDC45, CENPM (+1 more) | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: CLSPN, SLC44A2, AURKB; maybe low, not absent; its own permutation p; co-absent genes |
| [[MCM2]] | C | MCM2 activity raises CENPH's level | lines that do not express MCM2 (3) vs lines expressing it (47) | 2.16× lower at baseline in the lines without MCM2 | 0.066 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: LRRC20, SEMA3F, CDC45; maybe low, not absent |
| [[PBK]] | C | PBK activity raises CENPH's level | lines that do not express PBK (4) vs lines expressing it (46) | 2.19× lower at baseline in the lines without PBK | 0.078 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SPDL1, SMARCD3, NCS1; maybe low, not absent |
| [[MYBL2]] | C | MYBL2 activity raises CENPH's level | lines that do not express MYBL2 (4) vs lines expressing it (46) | 2.37× lower at baseline in the lines without MYBL2 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SMARCD3, DNMT3B, DSCC1; maybe low, not absent; its own permutation p |
| [[CLSPN]] | C | CLSPN activity raises CENPH's level | lines that do not express CLSPN (4) vs lines expressing it (46) | 2.29× lower at baseline in the lines without CLSPN | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TCF19, CDC45, RRM2; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.860). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-37.4, -45.0); signed map (-39.0, -47.2). **Vector** length 98.3, 24.0% of its response variance represented; |z| ≥ 3 in 954 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *E2F targets* (hallmark, mean cos +0.66 to 65); *DNA strand elongation* (reactome, mean cos +0.67 to 28); *DNA Replication* (reactome, mean cos +0.66 to 40).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | +7.2 | +20.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | +7.1 | +17.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | +6.1 | +13.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | +4.7 | +12.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | +3.5 | +6.7 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +2.3 | +4.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.2 | +3.4 |
|  | [[Irinotecan (drug)]] 0.5 µM |  | +1.9 | +0.9 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | +1.7 | +3.4 |
|  | [[Raltitrexed (drug)]] 0.5 µM |  | +1.7 | +2.7 |
| fall | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | -4.1 | -3.9 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~62% of this change | -3.8 | -4.7 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~97% of this change | -3.6 | -5.1 |
|  | [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.5 | -2.1 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -2.4 | -5.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.1 | -2.2 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.0 | -0.2 |
|  | [[Temsirolimus (drug)]] 5 µM |  | -2.0 | -2.5 |
|  | [[palbociclib (drug)]] 5 µM |  | -2.0 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | centromere protein H |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q13.2 — chr5:69,189,574-69,210,357 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Constitutive centromere associated network |
| Reactome | 20 pathways, smallest: Deposition of new CENPA-containing nucleosomes at the centromere; Nucleosome assembly; Amplification  of signal from unattached  kinetochores via a MAD2  inhibitory signal |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H3R5](https://www.uniprot.org/uniprotkb/Q9H3R5) (Centromere protein H):

> Component of the CENPA-NAC (nucleosome-associated) complex, a complex that plays a central role in assembly of kinetochore proteins, mitotic progression and chromosome segregation. The CENPA-NAC complex recruits the CENPA-CAD (nucleosome distal) complex and may be involved in incorporation of newly synthesized CENPA into centromeres. Required for chromosome congression and efficiently align the chromosomes on a metaphase plate.

**Summary**, from NCBI Gene [64946](https://www.ncbi.nlm.nih.gov/gene/64946):

> Centromere and kinetochore proteins play a critical role in centromere structure, kinetochore formation, and sister chromatid separation. The protein encoded by this gene colocalizes with inner kinetochore plate proteins CENP-A and CENP-C in both interphase and metaphase. It localizes outside of centromeric heterochromatin, where CENP-B is localized, and inside the kinetochore corona, where CENP-E is localized during prometaphase. It is thought that this protein can bind to itself, as well as …

**Accessions** — [HGNC:17268](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17268) · Entrez [64946](https://www.ncbi.nlm.nih.gov/gene/64946) · UniProt [Q9H3R5](https://www.uniprot.org/uniprotkb/Q9H3R5) · Ensembl [ENSG00000153044](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000153044)

## Data

Gene col 7682: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7682); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7682, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7682]; `tensor/DDL_lfc|DDL_z.npy` [7682]; `embed/gene_vectors.npy` [7682]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7682 or target_col == 7682). Every well: [[CENPH — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CENPH.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
