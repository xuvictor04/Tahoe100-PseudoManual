---
symbol: "GBP1"
type: "gene"
col: 3886
ensembl_id: "ENSG00000117228"
name: "guanylate binding protein 1"
location: "1p22.2"
module: 70
arm: "+"
pooled_cpm: 28.62
n_lines_expressing: 34
n_dd_up: 42
n_dd_down: 32
n_dd_up_clean: 40
n_dd_down_clean: 29
in_vector_space: true
direction_upstream: 70
direction_downstream: 111
tags: ["gene", "module/070"]
generated_by: "tahoemap"
---

# GBP1

*guanylate binding protein 1* — 1p22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 42 drug-doses (2 with an alert ⚠); the strongest is [[Cobimetinib (drug)]] 5 µM: 3.35× (z +10.8, q 3e-24, up in 30 of 31 measured lines).
> Pooled over the cell lines (median), lowered significantly by 32 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.224× (z -13.8, q 8e-41, down in 30 of 32 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EPSTI1]] (+0.87, fdr 7e-06), [[SAMD9L]] (+0.86, fdr 7e-06), [[PARP14]] (+0.86, fdr 7e-06).
> It is in [[Module 070]], a single-armed module (interferon gamma response).
> Probable direction (from the cell lines, not proof of direct regulation): 70 arrows point to it, the strongest [[CASP10]] → it (grade B ⚠); 111 go from it, the strongest it → [[NLRC5]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 42 in all, 2 with an alert ⚠; shown: the 15 strongest. 42 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3886.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 5 µM |  | **3.35×** | +10.8 | 3e-24 | 30/31 (NCI-H460, A549, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **3.09×** | +10.4 | 4e-23 | 28/32 (HS-578T, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Trametinib (drug)]] 5 µM |  | **2.61×** | +9.8 | 2e-20 | 31/32 (AsPC-1, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **2.68×** | +9.7 | 4e-20 | 30/32 (CFPAC-1, AsPC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **2.35×** | +9.5 | 3e-19 | 30/32 (AsPC-1, CFPAC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **2.86×** | +9.3 | 1e-18 | 29/32 (AsPC-1, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.68×** | +9.1 | 7e-18 | 25/32 (CFPAC-1, HS-578T, …) | inconsistent across doses | cell-cycle shift (explains ~3% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **2.38×** | +8.0 | 7e-14 | 29/32 (AsPC-1, A549, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.97×** | +7.7 | 1e-12 | 28/32 (CFPAC-1, AsPC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **2.14×** | +7.0 | 1e-10 | 28/31 (NCI-H460, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | **1.73×** | +7.0 | 2e-10 | 26/32 (AsPC-1, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.65×** | +6.3 | 2e-08 | 26/32 (AsPC-1, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.89×** | +5.9 | 2e-07 | 23/32 (CFPAC-1, NCI-H2347, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **2.00×** | +5.9 | 2e-07 | 25/32 (CFPAC-1, AsPC-1, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.81×** | +5.3 | 5e-06 | 19/32 (CFPAC-1, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 3 with an alert ⚠; shown: the 15 strongest. 32 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3886.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.224×** | -13.8 | 8e-41 | 30/32 (A498, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.260×** | -12.5 | 4e-33 | 29/32 (A498, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.283×** | -11.7 | 3e-29 | 28/32 (A-172, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tofacitinib (drug)]] 5 µM |  | **0.425×** | -11.2 | 6e-27 | 24/32 (CFPAC-1, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | **0.474×** | -9.8 | 2e-20 | 24/32 (CFPAC-1, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.364×** | -9.4 | 8e-19 | 29/32 (AsPC-1, LoVo, …) | top dose only |  |
| [[Tofacitinib (drug)]] 0.5 µM |  | **0.365×** | -9.3 | 9e-19 | 25/32 (NCI-H2347, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **0.371×** | -9.2 | 3e-18 | 26/32 (NCI-H2347, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.380×** | -8.9 | 2e-17 | 28/32 (NCI-H2347, LoVo, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.477×** | -6.9 | 4e-10 | 22/32 (BT-474, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.534×** | -5.3 | 6e-06 | 22/32 (A549, RPMI-7951, …) | all doses, flat | cell-cycle shift (explains ~7% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.570×** | -5.2 | 9e-06 | 23/32 (A549, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.692×** | -4.8 | 6e-05 | 16/32 (A549, BT-474, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~14% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.612×** | -4.5 | 2e-04 | 21/32 (A549, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **0.606×** | -4.5 | 3e-04 | 19/31 (SK-MEL-2, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~2% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, +0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3886. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CFPAC-1 (line)]] | alt | 121 | 6 (1 ⚠) | 6 | [[Homoharringtonine (drug)]] 5 µM 4.90× (z +16.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 7.42× (z +14.5) | [[Tofacitinib (drug)]] 5 µM 0.199× (z -16.7) |
| [[NCI-H2347 (line)]] | alt | 57.4 | 2 | 10 (1 ⚠) | [[Harringtonine (drug)]] 0.5 µM 6.36× (z +11.9) | [[Tofacitinib (drug)]] 5 µM 0.199× (z -14.8) |
| [[A549 (line)]] | wt | 26.8 | 0 | 10 | — | [[Panobinostat (drug)]] 5 µM 0.0744× (z -12.4) |
| [[AsPC-1 (line)]] | alt | 35.6 | 7 | 3 | [[Trametinib (drug)]] 0.5 µM 5.11× (z +10.3) | [[Auranofin (drug)]] 5 µM 0.0671× (z -14.2) |
| [[LoVo (line)]] | wt | 23.3 | 0 | 9 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0726× (z -14.4) |
| [[MIA PaCa-2 (line)]] | alt | 16.7 | 3 (1 ⚠) | 6 (1 ⚠) | [[Adagrasib (drug)]] 0.05 µM 2.02× (z +9.4) ⚠ position not correctable · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 10.1× (z +8.6) | [[Belinostat (drug)]] 5 µM 0.0444× (z -11.7) |
| [[A-172 (line)]] | wt | 25.6 | 3 | 5 | [[Homoharringtonine (drug)]] 0.5 µM 15.0× (z +13.6) | [[Belinostat (drug)]] 5 µM 0.0696× (z -13.5) |
| [[A498 (line)]] | wt | 118 | 1 | 7 | [[Homoharringtonine (drug)]] 0.5 µM 3.25× (z +8.9) | [[Panobinostat (drug)]] 5 µM 0.0981× (z -17.6) |
| [[BT-474 (line)]] | alt | 18.0 | 0 | 8 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0320× (z -12.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[TAK-901 (drug)]] 0.05 µM 0.0307× (z -11.5) |
| [[J82 (line)]] | alt | 44.3 | 6 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 12.5× (z +12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~21% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 9.39× (z +10.9) | — |
| [[Panc 03.27 (line)]] | alt | 27.2 | 4 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 0.5 µM 14.5× (z +13.1) | [[Auranofin (drug)]] 5 µM 0.105× (z -11.1) |
| [[SNU-423 (line)]] | alt | 84.4 | 1 | 4 | [[Homoharringtonine (drug)]] 0.5 µM 4.78× (z +8.7) | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM 0.140× (z -11.0) |
| [[Hs 766T (line)]] | wt | 49.7 | 1 (1 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 3.04× (z +8.6) ⚠ cell-cycle shift, explains ~0% of this change | [[Tofacitinib (citrate) (drug)]] 0.5 µM 0.143× (z -10.7) |
| [[HS-578T (line)]] | alt | 101 | 3 | 1 | [[Harringtonine (drug)]] 0.5 µM 13.2× (z +15.2) | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM 0.197× (z -9.6) |
| [[RPMI-7951 (line)]] | alt | 103 | 1 | 3 | [[Harringtonine (drug)]] 0.5 µM 5.51× (z +10.6) | [[Panobinostat (drug)]] 0.5 µM 0.126× (z -12.9) |
| [[COLO 205 (line)]] | alt | 46.9 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.0397× (z -13.0) |
| [[HEC-1-A (line)]] | alt | 22.2 | 1 | 2 | [[Harringtonine (drug)]] 0.5 µM 5.57× (z +10.7) | [[Panobinostat (drug)]] 0.5 µM 0.212× (z -9.7) |
| [[hTERT-HPNE (line)]] | wt | 27.9 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.58× (z +13.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 18.1× (z +13.0) | — |
| [[NCI-H1792 (line)]] | alt | 54.5 | 1 | 2 | [[Harringtonine (drug)]] 0.5 µM 4.25× (z +9.1) | [[Tofacitinib (drug)]] 0.5 µM 0.251× (z -8.8) |
| [[NCI-H460 (line)]] | wt | 9.91 | 2 | 1 | [[Cobimetinib (drug)]] 5 µM 6.71× (z +9.2) | [[Panobinostat (drug)]] 5 µM 0.170× (z -9.0) |
| [[H4 (line)]] | wt | 22.1 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.0507× (z -11.4) |
| [[C32 (line)]] | wt | 24.3 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.179× (z -9.1) |
| [[CHP-212 (line)]] | wt | 25.8 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.0366× (z -9.6) |
| [[HT-29 (line)]] | alt | 13.1 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.135× (z -8.6) |
| [[KATO III (line)]] | alt | 15.9 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.109× (z -8.9) |
| [[SK-MEL-2 (line)]] | alt | 14.0 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.108× (z -9.0) |
| [[SW 900 (line)]] | alt | 16.3 | 1 | 0 | [[Harringtonine (drug)]] 0.5 µM 8.93× (z +9.1) | — |
| [[A-427 (line)]] | wt | 1.48 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 3.35 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.96 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 2.36 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 6.97 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 5.63 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.36 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 9.30 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.25 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.20 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 3.36 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 4.92 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 2.72 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.73 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 86.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.75 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.29 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.74 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3886), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EPSTI1]] | +0.87 | +0.80 / +0.87 | both halves | 7e-06 | STRING 780 |
| [[SAMD9L]] | +0.86 | +0.81 / +0.88 | both halves | 7e-06 | STRING 773 |
| [[PARP14]] | +0.86 | +0.80 / +0.86 | both halves | 7e-06 | STRING 622 |
| [[TRANK1]] | +0.85 | +0.83 / +0.83 | both halves | 7e-06 |  |
| [[IFI35]] | +0.84 | +0.78 / +0.85 | both halves | 7e-06 | pathway: Interferon Signaling; STRING 738 |
| [[GBP4]] | +0.84 | +0.81 / +0.83 | both halves | 7e-06 | same gene group; pathway: Antimicrobial mechanism of IFN-stimulated genes; STRING 905 |
| [[CFB]] | +0.84 | +0.78 / +0.84 | both halves | 7e-06 | **novel candidate** |
| [[NMI]] | +0.83 | +0.76 / +0.85 | both halves | 7e-06 | STRING 531 |
| [[IFIH1]] | +0.83 | +0.74 / +0.86 | both halves | 7e-06 | pathway: Interferon Signaling; STRING 870 |
| [[ADAR]] | +0.83 | +0.76 / +0.82 | both halves | 7e-06 | pathway: Antimicrobial mechanism of IFN-stimulated genes |
| [[PARP9]] | +0.83 | +0.75 / +0.84 | both halves | 7e-06 | STRING 814 |
| [[SLC15A3]] | +0.83 | +0.72 / +0.86 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*70 arrows, 70 of them with an alert ⚠; grade A 0, B 48, C 22. Shown: the 12 strongest; 58 more arrows (58 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CASP10]] | B | CASP10 activity raises GBP1's level | lines that do not express CASP10 (19) vs lines expressing it (31) | 3.24× lower at baseline in the lines without CASP10 | 6e-04 | ⚠ within organs, on part of the lines; also absent: RARRES1, TRIM22, ACSL5 |
| [[OAS1]] | B | OAS1 activity raises GBP1's level | lines that do not express OAS1 (13) vs lines expressing it (37) | 3.37× lower at baseline in the lines without OAS1 | 0.003 | ⚠ within organs, on part of the lines; also absent: OAS2, TRIM22, IFI27; maybe low, not absent |
| [[MX1]] | B | MX1 activity raises GBP1's level | lines that do not express MX1 (19) vs lines expressing it (31) | 2.89× lower at baseline in the lines without MX1 | 0.004 | ⚠ within organs, on part of the lines; also absent: OAS2, SRMS, EPSTI1 |
| [[OASL]] | B | OASL activity raises GBP1's level | lines that do not express OASL (10) vs lines expressing it (40) | 3.85× lower at baseline in the lines without OASL | 0.004 | ⚠ within organs, on part of the lines; also absent: TMEM92-AS1, GBP2, TENT5A; maybe low, not absent |
| [[IFI16]] | B | IFI16 activity raises GBP1's level | lines that do not express IFI16 (18) vs lines expressing it (32) | 3.80× lower at baseline in the lines without IFI16 | 0.005 | ⚠ within organs, on part of the lines; also absent: MMP14, IL1A, MAF |
| [[TNFSF10]] | B | TNFSF10 activity raises GBP1's level | lines that do not express TNFSF10 (24) vs lines expressing it (26) | 3.27× lower at baseline in the lines without TNFSF10 | 0.006 | ⚠ within organs, on part of the lines; also absent: PLAAT4, TMEM92, LY75 |
| [[EPSTI1]] | B | EPSTI1 activity raises GBP1's level | lines that do not express EPSTI1 (25) vs lines expressing it (25) | 3.60× lower at baseline in the lines without EPSTI1 | 0.006 | ⚠ within organs, on part of the lines; also absent: UGT1A6, PKP1, ENSG00000271933 |
| [[RARRES1]] | B | RARRES1 activity raises GBP1's level | lines that do not express RARRES1 (22) vs lines expressing it (28) | 2.26× lower at baseline in the lines without RARRES1 | 0.007 | ⚠ within organs, on part of the lines; also absent: CASP10, POU5F1, ENSG00000284644; maybe low, not absent |
| [[MMP13]] | B | MMP13 activity raises GBP1's level | lines that do not express MMP13 (30) vs lines expressing it (20) | 2.59× lower at baseline in the lines without MMP13 | 0.008 | ⚠ within organs, on part of the lines; also absent: SOX11, AGT, STEAP4 |
| [[RASGRP3]] | B | RASGRP3 activity raises GBP1's level | lines that do not express RASGRP3 (16) vs lines expressing it (34) | 3.39× lower at baseline in the lines without RASGRP3 | 0.010 | ⚠ within organs, on part of the lines; also absent: IFI6, SLC15A3, GBP4; maybe low, not absent |
| [[NLRC5]] | B | NLRC5 activity raises GBP1's level | lines that do not express NLRC5 (5) vs lines expressing it (45) | 4.65× lower at baseline in the lines without NLRC5 | 0.014 | ⚠ within organs, on part of the lines; also absent: NDRG1, APOL6, S100A13; maybe low, not absent |
| [[SLC15A3]] | B | SLC15A3 activity raises GBP1's level | lines that do not express SLC15A3 (16) vs lines expressing it (34) | 4.24× lower at baseline in the lines without SLC15A3 | 0.016 | ⚠ within organs, on part of the lines; also absent: XAF1, MX2, GBP4 |

### Downstream of this gene

*111 arrows, 111 of them with an alert ⚠; grade A 0, B 92, C 19. Shown: the 12 strongest; 99 more arrows (99 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NLRC5]] | B | GBP1 activity raises NLRC5's level | lines that do not express GBP1 (16) vs lines expressing it (34) | 2.33× lower at baseline in the lines without GBP1 | 4e-04 | ⚠ within organs, on part of the lines; also absent: GBP4, GBP2, SAMD9 |
| [[PSMB10]] | B | GBP1 activity raises PSMB10's level | lines that do not express GBP1 (16) vs lines expressing it (34) | 1.68× lower at baseline in the lines without GBP1 | 6e-04 | ⚠ within organs, on part of the lines; also absent: GBP4, GBP2, SAMD9 |
| [[OAS1]] | B | GBP1 activity raises OAS1's level | lines that do not express GBP1 (16) vs lines expressing it (34) | 3.13× lower at baseline in the lines without GBP1 | 0.001 | ⚠ within organs, on part of the lines; also absent: GBP4, GBP2, SAMD9 |
| [[IRF1]] | B | GBP1 activity raises IRF1's level | lines that do not express GBP1 (16) vs lines expressing it (34) | 1.79× lower at baseline in the lines without GBP1 | 0.001 | ⚠ within organs, on part of the lines; also absent: GBP4, GBP2, SAMD9 |
| [[SP100]] | B | GBP1 activity raises SP100's level | lines that do not express GBP1 (16) vs lines expressing it (34) | 2.50× lower at baseline in the lines without GBP1 | 0.002 | ⚠ within organs, on part of the lines; also absent: GBP4, GBP2, SAMD9 |
| [[APOL6]] | B | GBP1 activity raises APOL6's level | lines that do not express GBP1 (16) vs lines expressing it (34) | 2.59× lower at baseline in the lines without GBP1 | 0.002 | ⚠ within organs, on part of the lines; also absent: GBP4, GBP2, SAMD9 |
| [[CASP10]] | B | GBP1 activity raises CASP10's level | lines that do not express GBP1 (16) vs lines expressing it (34) | 2.57× lower at baseline in the lines without GBP1 | 0.004 | ⚠ within organs, on part of the lines; also absent: GBP4, GBP2, SAMD9 |
| [[CXCL2]] | B | GBP1 activity raises CXCL2's level | lines that do not express GBP1 (16) vs lines expressing it (34) | 2.51× lower at baseline in the lines without GBP1 | 0.005 | ⚠ within organs, on part of the lines; also absent: GBP4, GBP2, SAMD9 |
| [[B2M]] | B | GBP1 activity raises B2M's level | lines that do not express GBP1 (16) vs lines expressing it (34) | 2.28× lower at baseline in the lines without GBP1 | 0.005 | ⚠ within organs, on part of the lines; also absent: GBP4, GBP2, SAMD9 |
| [[TRIM34]] | B | GBP1 activity raises TRIM34's level | lines that do not express GBP1 (16) vs lines expressing it (34) | 2.18× lower at baseline in the lines without GBP1 | 0.005 | ⚠ within organs, on part of the lines; also absent: GBP4, GBP2, SAMD9 |
| [[PSMB8]] | B | GBP1 activity raises PSMB8's level | lines that do not express GBP1 (16) vs lines expressing it (34) | 2.57× lower at baseline in the lines without GBP1 | 0.006 | ⚠ within organs, on part of the lines; also absent: GBP4, GBP2, SAMD9 |
| [[DDX60]] | B | GBP1 activity raises DDX60's level | lines that do not express GBP1 (16) vs lines expressing it (34) | 2.97× lower at baseline in the lines without GBP1 | 0.006 | ⚠ within organs, on part of the lines; also absent: GBP4, GBP2, SAMD9 |

## Where it sits

- **Module**: [[Module 070]] — interferon gamma response; 70 genes; every member is in the + arm (projection on the module's main direction 0.882). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (46.5, 52.3); signed map (62.5, 30.3). **Vector** length 158, 54.9% of its response variance represented; |z| ≥ 3 in 1,350 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *interferon gamma response* (hallmark, mean cos +0.63 to 25); *interferon alpha response* (hallmark, mean cos +0.62 to 19); *Antigen processing-Cross presentation* (reactome, mean cos +0.64 to 14).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +9.2 | +10.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +8.3 | +10.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +8.2 | +9.5 |
|  | [[Binimetinib (drug)]] 5 µM |  | +8.2 | +9.7 |
|  | [[Trametinib (drug)]] 5 µM |  | +7.5 | +9.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +7.5 | +9.3 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +7.0 | +7.7 |
| fall | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -8.0 | -8.9 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -7.7 | -11.2 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -7.0 | -9.8 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -6.8 | -9.2 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -6.1 | -9.3 |

## What is on record

|  |  |
|---|---|
| Name | guanylate binding protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p22.2 — chr1:89,051,882-89,065,360 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Guanylate binding proteins |
| Reactome | 15 pathways, smallest: Regulation of GBP-mediated host defense; CASP4 inflammasome assembly; Enterobacterial factors antagonize host defense |
| Matched by | ensembl_id |

**Function**, from UniProt [P32455](https://www.uniprot.org/uniprotkb/P32455) (Guanylate-binding protein 1):

> Interferon (IFN)-inducible GTPase that plays important roles in innate immunity against a diverse range of bacterial, viral and protozoan pathogens. Hydrolyzes GTP to GMP in two consecutive cleavage reactions: GTP is first hydrolyzed to GDP and then to GMP in a processive manner. Following infection, recruited to the pathogen-containing vacuoles or vacuole-escaped bacteria and promotes both inflammasome assembly and autophagy. Acts as a positive regulator of inflammasome assembly by …

**Summary**, from NCBI Gene [2633](https://www.ncbi.nlm.nih.gov/gene/2633):

> Guanylate binding protein expression is induced by interferon. Guanylate binding proteins are characterized by their ability to specifically bind guanine nucleotides (GMP, GDP, and GTP) and are distinguished from the GTP-binding proteins by the presence of 2 binding motifs rather than 3. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:4182](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4182) · Entrez [2633](https://www.ncbi.nlm.nih.gov/gene/2633) · UniProt [P32455](https://www.uniprot.org/uniprotkb/P32455) · Ensembl [ENSG00000117228](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000117228)

## Data

Gene col 3886: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3886); `tables/drug_effects.parquet` (74 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3886, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3886]; `tensor/DDL_lfc|DDL_z.npy` [3886]; `embed/gene_vectors.npy` [3886]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3886 or target_col == 3886). Every well: [[GBP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GBP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
