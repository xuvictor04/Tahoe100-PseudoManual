---
symbol: "GBP3"
type: "gene"
col: 3885
ensembl_id: "ENSG00000117226"
name: "guanylate binding protein 3"
location: "1p22.2"
module: 32
arm: "+"
pooled_cpm: 33.53
n_lines_expressing: 39
n_dd_up: 15
n_dd_down: 46
n_dd_up_clean: 15
n_dd_down_clean: 42
in_vector_space: true
direction_upstream: 57
direction_downstream: 47
tags: ["gene", "module/032"]
generated_by: "tahoemap"
---

# GBP3

*guanylate binding protein 3* — 1p22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (none with an alert); the strongest is [[Harringtonine (drug)]] 0.5 µM: 1.86× (z +9.9, q 3e-20, up in 29 of 37 measured lines).
> Pooled over the cell lines (median), lowered significantly by 46 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.232× (z -23.2, q 0e+00, down in 35 of 37 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GBP1]] (+0.81, fdr 7e-06, ⚠ same locus), [[GBP4]] (+0.81, fdr 7e-06), [[NMI]] (+0.81, fdr 7e-06), [[PARP14]] (+0.80, fdr 7e-06).
> It is in [[Module 032]], a single-armed module (interferon alpha response).
> Probable direction (from the cell lines, not proof of direct regulation): 57 arrows point to it, the strongest [[MX1]] → it (grade B ⚠); 47 go from it, the strongest it → [[APOL6]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, none with an alert; shown: the 15 strongest. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3885.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **1.86×** | +9.9 | 3e-20 | 29/37 (A-172, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~1% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.59×** | +7.4 | 3e-11 | 30/37 (SNU-423, NCI-H2347, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.53×** | +6.8 | 2e-09 | 24/37 (A-172, HS-578T, …) | inconsistent across doses | cell-cycle shift (explains ~4% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.45×** | +5.9 | 5e-07 | 20/37 (A-172, HS-578T, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.43×** | +5.3 | 1e-05 | 18/35 (HS-578T, AsPC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.41×** | +5.3 | 1e-05 | 19/35 (Hs 766T, SW1417, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.37×** | +5.1 | 3e-05 | 21/37 (NCI-H1792, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.27×** | +4.6 | 3e-04 | 16/37 (AsPC-1, CFPAC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.33×** | +4.5 | 4e-04 | 13/37 (PANC-1, HS-578T, …) | rises with dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.29×** | +4.1 | 0.002 | 16/37 (A498, LS 180, …) | two highest doses |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.29×** | +4.0 | 0.003 | 14/37 (AsPC-1, CFPAC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Cytarabine (hydrochloride) (drug)]] 5 µM |  | **1.27×** | +3.6 | 0.012 | 14/37 (CFPAC-1, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Binimetinib (drug)]] 0.5 µM |  | 1.19× | +3.5 | 0.021 | 13/37 (Hs 766T, CFPAC-1, …) | rises with dose | noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.33×** | +3.3 | 0.039 | 6/36 (CFPAC-1, LoVo, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.24×** | +3.3 | 0.042 | 15/37 (LS 180, SW1417, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 50 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 46 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3885.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.232×** | -23.2 | 0e+00 | 35/37 (NCI-H1573, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.247×** | -22.2 | 0e+00 | 36/37 (NCI-H1573, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.425×** | -19.2 | 0e+00 | 29/37 (NCI-H1573, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.339×** | -17.2 | 0e+00 | 34/37 (HT-29, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.528×** | -10.1 | 4e-22 | 31/37 (BT-474, MIA PaCa-2, …) | top dose only |  |
| [[Tofacitinib (drug)]] 5 µM |  | **0.639×** | -10.1 | 8e-22 | 28/37 (CFPAC-1, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.543×** | -9.7 | 2e-20 | 29/37 (LoVo, A498, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.586×** | -8.5 | 1e-15 | 27/37 (A498, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.616×** | -7.7 | 8e-13 | 24/36 (NCI-H1573, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **0.628×** | -7.4 | 8e-12 | 25/37 (BT-474, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Tofacitinib (drug)]] 0.5 µM |  | **0.659×** | -6.6 | 2e-09 | 23/37 (CFPAC-1, BT-474, …) | all doses, stronger at high dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.453×** | -6.5 | 5e-09 | 25/37 (LoVo, KATO III, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | **0.769×** | -5.9 | 2e-07 | 22/37 (CFPAC-1, A549, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.699×** | -5.5 | 2e-06 | 20/35 (BT-474, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[EX229 (drug)]] 5 µM |  | **0.533×** | -5.1 | 1e-05 | 21/37 (AsPC-1, NCI-H1573, …) | top dose only | noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.536×** | -5.1 | 1e-05 | 23/36 (NCI-H1573, SNU-423, …) | top dose only | noisy plate (z scaled) |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.744×** | -4.7 | 1e-04 | 19/37 (A498, NCI-H1792, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3885. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 57.0 | 0 | 11 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0390× (z -18.4) |
| [[A498 (line)]] | wt | 48.2 | 0 | 9 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.124× (z -20.3) |
| [[A-172 (line)]] | wt | 20.2 | 3 | 4 (1 ⚠) | [[Harringtonine (drug)]] 0.5 µM 7.03× (z +12.4) | [[Panobinostat (drug)]] 0.5 µM 0.130× (z -12.8) |
| [[LoVo (line)]] | wt | 38.7 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.251× (z -16.4) |
| [[NCI-H1573 (line)]] | alt | 65.5 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0453× (z -38.8) |
| [[SNU-423 (line)]] | alt | 66.6 | 1 | 5 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 3.33× (z +9.2) | [[Panobinostat (drug)]] 0.5 µM 0.179× (z -13.2) |
| [[CFPAC-1 (line)]] | alt | 132 | 0 | 5 | — | [[Panobinostat (drug)]] 0.5 µM 0.210× (z -17.3) |
| [[COLO 205 (line)]] | alt | 52.8 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.114× (z -21.4) |
| [[HT-29 (line)]] | alt | 31.0 | 0 | 5 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0898× (z -17.0) |
| [[RKO (line)]] | wt | 36.7 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0559× (z -24.9) |
| [[A549 (line)]] | wt | 22.1 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.0943× (z -14.0) |
| [[HCT15 (line)]] | alt | 45.6 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.132× (z -19.3) |
| [[HEC-1-A (line)]] | alt | 19.3 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.102× (z -15.2) |
| [[KATO III (line)]] | alt | 68.5 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.130× (z -24.0) |
| [[LS 180 (line)]] | wt | 51.0 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.228× (z -13.3) |
| [[RPMI-7951 (line)]] | alt | 51.2 | 1 | 3 | [[Harringtonine (drug)]] 0.5 µM 3.64× (z +9.0) | [[Homoharringtonine (drug)]] 5 µM 0.123× (z -20.7) |
| [[SW1417 (line)]] | alt | 30.6 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.340× (z -11.0) |
| [[AsPC-1 (line)]] | alt | 61.1 | 0 | 3 | — | [[Auranofin (drug)]] 5 µM 0.289× (z -10.1) |
| [[Hs 766T (line)]] | wt | 79.0 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.247× (z -10.0) |
| [[HS-578T (line)]] | alt | 143 | 2 | 1 | [[Harringtonine (drug)]] 0.5 µM 4.33× (z +11.0) | [[Panobinostat (drug)]] 5 µM 0.258× (z -10.1) |
| [[LOX-IMVI (line)]] | wt | 26.3 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.138× (z -14.6) |
| [[MIA PaCa-2 (line)]] | alt | 14.3 | 0 | 3 | — | [[Tofacitinib (drug)]] 5 µM 0.183× (z -10.0) |
| [[NCI-H1792 (line)]] | alt | 61.6 | 1 (1 ⚠) | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.34× (z +10.1) ⚠ cell-cycle shift, explains ~48% of this change | [[Homoharringtonine (drug)]] 5 µM 0.170× (z -21.2) |
| [[NCI-H2347 (line)]] | alt | 36.2 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.174× (z -19.6) |
| [[PANC-1 (line)]] | alt | 16.8 | 2 | 1 | [[Harringtonine (drug)]] 0.5 µM 4.45× (z +11.9) | [[Homoharringtonine (drug)]] 5 µM 0.0998× (z -25.8) |
| [[NCI-H2030 (line)]] | alt | 9.85 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.166× (z -9.3) |
| [[hTERT-HPNE (line)]] | wt | 28.2 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 5.66× (z +9.4) | — |
| [[J82 (line)]] | alt | 30.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.92× (z +11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~5% of this change | — |
| [[Panc 03.27 (line)]] | alt | 16.9 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.87× (z +8.5) | — |
| [[A-427 (line)]] | wt | 3.25 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 5.27 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.97 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 16.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.64 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 20.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.77 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.88 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 5.92 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.24 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 2.71 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.50 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 112 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 10.0 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 4.78 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3885), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GBP1]] | +0.81 | +0.76 / +0.81 | both halves | 7e-06 | same gene group; pathway: Antimicrobial mechanism of IFN-stimulated genes; STRING 936; ⚠ same locus (29.0 kb, same strand: neighbours can correlate without regulation) |
| [[GBP4]] | +0.81 | +0.75 / +0.82 | both halves | 7e-06 | same gene group; pathway: Antimicrobial mechanism of IFN-stimulated genes |
| [[NMI]] | +0.81 | +0.71 / +0.82 | both halves | 7e-06 |  |
| [[PARP14]] | +0.80 | +0.72 / +0.80 | both halves | 7e-06 |  |
| [[TRANK1]] | +0.79 | +0.70 / +0.79 | both halves | 7e-06 |  |
| [[SAMD9L]] | +0.79 | +0.76 / +0.80 | both halves | 7e-06 | STRING 468 |
| [[IFI35]] | +0.77 | +0.74 / +0.76 | both halves | 7e-06 | pathway: Interferon Signaling; STRING 425 |
| [[PHF11]] | +0.77 | +0.62 / +0.79 | both halves | 7e-06 |  |
| [[DDX60L]] | +0.76 | +0.70 / +0.75 | both halves | 7e-06 | STRING 415 |
| [[CTSS]] | +0.76 | +0.68 / +0.77 | both halves | 7e-06 |  |
| [[SAMD9]] | +0.76 | +0.68 / +0.79 | both halves | 7e-06 | STRING 480 |
| [[APOL6]] | +0.75 | +0.64 / +0.76 | both halves | 7e-06 |  |
| [[SLC15A3]] | +0.75 | +0.67 / +0.76 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*57 arrows, 57 of them with an alert ⚠; grade A 0, B 49, C 8. Shown: the 12 strongest; 45 more arrows (45 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MX1]] | B | MX1 activity raises GBP3's level | lines that do not express MX1 (19) vs lines expressing it (31) | 2.95× lower at baseline in the lines without MX1 | 0.001 | ⚠ within organs, on part of the lines; also absent: OAS2, SRMS, EPSTI1 |
| [[IFI16]] | B | IFI16 activity raises GBP3's level | lines that do not express IFI16 (18) vs lines expressing it (32) | 2.68× lower at baseline in the lines without IFI16 | 0.002 | ⚠ within organs, on part of the lines; also absent: MMP14, IL1A, MAF |
| [[CASP10]] | B | CASP10 activity raises GBP3's level | lines that do not express CASP10 (19) vs lines expressing it (31) | 3.12× lower at baseline in the lines without CASP10 | 0.003 | ⚠ within organs, on part of the lines; also absent: RARRES1, TRIM22, ACSL5 |
| [[IFI44]] | B | IFI44 activity raises GBP3's level | lines that do not express IFI44 (12) vs lines expressing it (38) | 3.53× lower at baseline in the lines without IFI44 | 0.005 | ⚠ within organs, on part of the lines; also absent: SAMD9, GBP1, BMP2 |
| [[OASL]] | B | OASL activity raises GBP3's level | lines that do not express OASL (10) vs lines expressing it (40) | 2.72× lower at baseline in the lines without OASL | 0.006 | ⚠ within organs, on part of the lines; also absent: TMEM92-AS1, GBP2, TENT5A; maybe low, not absent |
| [[TRIM22]] | B | TRIM22 activity raises GBP3's level | lines that do not express TRIM22 (18) vs lines expressing it (32) | 3.44× lower at baseline in the lines without TRIM22 | 0.006 | ⚠ within organs, on part of the lines; also absent: CD5L, XAF1, IFITM1 |
| [[IFI44L]] | B | IFI44L activity raises GBP3's level | lines that do not express IFI44L (22) vs lines expressing it (28) | 2.64× lower at baseline in the lines without IFI44L | 0.006 | ⚠ within organs, on part of the lines; also absent: GBP1, EPSTI1, GBP4 |
| [[IFIT2]] | B | IFIT2 activity raises GBP3's level | lines that do not express IFIT2 (8) vs lines expressing it (42) | 4.03× lower at baseline in the lines without IFIT2 | 0.008 | ⚠ within organs, on part of the lines; also absent: IFIT3, ENSG00000235609, TRIM38 |
| [[RSAD2]] | B | RSAD2 activity raises GBP3's level | lines that do not express RSAD2 (14) vs lines expressing it (36) | 2.92× lower at baseline in the lines without RSAD2 | 0.010 | ⚠ within organs, on part of the lines; also absent: SH3TC1, IFI27, SRMS |
| [[PLAAT4]] | B | PLAAT4 activity raises GBP3's level | lines that do not express PLAAT4 (21) vs lines expressing it (29) | 3.04× lower at baseline in the lines without PLAAT4 | 0.012 | ⚠ within organs, on part of the lines; also absent: PTPRB, TNFSF10, EPSTI1 |
| [[MMP13]] | B | MMP13 activity raises GBP3's level | lines that do not express MMP13 (30) vs lines expressing it (20) | 2.55× lower at baseline in the lines without MMP13 | 0.012 | ⚠ within organs, on part of the lines; also absent: SOX11, AGT, STEAP4 |
| [[TRIM38]] | B | TRIM38 activity raises GBP3's level | lines that do not express TRIM38 (6) vs lines expressing it (44) | 5.13× lower at baseline in the lines without TRIM38 | 0.014 | ⚠ within organs, on part of the lines; also absent: SMOX, S100A13, ERAP2 |

### Downstream of this gene

*47 arrows, 47 of them with an alert ⚠; grade A 0, B 42, C 5. Shown: the 12 strongest; 35 more arrows (35 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[APOL6]] | B | GBP3 activity raises APOL6's level | lines that do not express GBP3 (11) vs lines expressing it (39) | 3.05× lower at baseline in the lines without GBP3 | 0.012 | ⚠ within organs, on part of the lines; also absent: PHLDA2, CD44, ITGA3 |
| [[SP100]] | B | GBP3 activity raises SP100's level | lines that do not express GBP3 (11) vs lines expressing it (39) | 2.55× lower at baseline in the lines without GBP3 | 0.012 | ⚠ within organs, on part of the lines; also absent: PHLDA2, CD44, ITGA3 |
| [[IL7]] | B | GBP3 activity raises IL7's level | lines that do not express GBP3 (11) vs lines expressing it (39) | 2.51× lower at baseline in the lines without GBP3 | 0.015 | ⚠ within organs, on part of the lines; also absent: PHLDA2, CD44, ITGA3 |
| [[RNASEL]] | B | GBP3 activity raises RNASEL's level | lines that do not express GBP3 (11) vs lines expressing it (39) | 1.98× lower at baseline in the lines without GBP3 | 0.020 | ⚠ within organs, on part of the lines; also absent: PHLDA2, CD44, ITGA3 |
| [[SAMD9]] | B | GBP3 activity raises SAMD9's level | lines that do not express GBP3 (11) vs lines expressing it (39) | 4.37× lower at baseline in the lines without GBP3 | 0.021 | ⚠ within organs, on part of the lines; also absent: PHLDA2, CD44, ITGA3 |
| [[IL15RA]] | B | GBP3 activity raises IL15RA's level | lines that do not express GBP3 (11) vs lines expressing it (39) | 2.55× lower at baseline in the lines without GBP3 | 0.031 | ⚠ within organs, on part of the lines; also absent: PHLDA2, CD44, ITGA3 |
| [[IRF2]] | B | GBP3 activity raises IRF2's level | lines that do not express GBP3 (11) vs lines expressing it (39) | 1.38× lower at baseline in the lines without GBP3 | 0.031 | ⚠ within organs, on part of the lines; also absent: PHLDA2, CD44, ITGA3 |
| [[DDX60]] | B | GBP3 activity raises DDX60's level | lines that do not express GBP3 (11) vs lines expressing it (39) | 2.93× lower at baseline in the lines without GBP3 | 0.031 | ⚠ within organs, on part of the lines; also absent: PHLDA2, CD44, ITGA3 |
| [[APOL1]] | B | GBP3 activity raises APOL1's level | lines that do not express GBP3 (11) vs lines expressing it (39) | 3.27× lower at baseline in the lines without GBP3 | 0.036 | ⚠ within organs, on part of the lines; also absent: PHLDA2, CD44, ITGA3 |
| [[NLRC5]] | B | GBP3 activity raises NLRC5's level | lines that do not express GBP3 (11) vs lines expressing it (39) | 2.09× lower at baseline in the lines without GBP3 | 0.036 | ⚠ within organs, on part of the lines; also absent: PHLDA2, CD44, ITGA3 |
| [[IFI44]] | B | GBP3 activity raises IFI44's level | lines that do not express GBP3 (11) vs lines expressing it (39) | 3.48× lower at baseline in the lines without GBP3 | 0.036 | ⚠ within organs, on part of the lines; also absent: PHLDA2, CD44, ITGA3 |
| [[PSMB8]] | B | GBP3 activity raises PSMB8's level | lines that do not express GBP3 (11) vs lines expressing it (39) | 3.09× lower at baseline in the lines without GBP3 | 0.038 | ⚠ within organs, on part of the lines; also absent: PHLDA2, CD44, ITGA3 |

## Where it sits

- **Module**: [[Module 032]] — interferon alpha response; 139 genes; every member is in the + arm (projection on the module's main direction 0.791). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (45.6, 53.1); signed map (61.8, 31.2). **Vector** length 133, 40.4% of its response variance represented; |z| ≥ 3 in 1,321 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *interferon alpha response* (hallmark, mean cos +0.64 to 56); *interferon gamma response* (hallmark, mean cos +0.65 to 60); *interferon* (control, mean cos +0.68 to 23).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +7.9 | +9.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +7.0 | +1.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | +6.1 | +5.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | +5.7 | -0.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | +5.6 | +7.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +5.5 | +5.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.5 | +5.9 |
|  | [[Binimetinib (drug)]] 5 µM |  | +4.0 | +4.0 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +3.8 | +3.5 |
| fall | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -6.9 | -10.1 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -6.3 | -10.1 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -5.6 | -7.4 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -5.5 | -5.9 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -5.4 | -6.6 |

## What is on record

|  |  |
|---|---|
| Name | guanylate binding protein 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p22.2 — chr1:89,006,679-89,022,894 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10961 |
| Gene groups (HGNC) | Guanylate binding proteins |
| Reactome | 11 pathways, smallest: CASP4 inflammasome assembly; Enterobacterial factors antagonize host defense; GBP-mediated host defense |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H0R5](https://www.uniprot.org/uniprotkb/Q9H0R5) (Guanylate-binding protein 3):

> Interferon (IFN)-inducible GTPase that plays important roles in innate immunity against a diverse range of bacterial, viral and protozoan pathogens. Hydrolyzes GTP very efficiently; GDP rather than GMP is the major reaction product (By similarity). Following infection, recruited to the pathogen-containing vacuoles or vacuole-escaped bacteria and acts as a positive regulator of inflammasome assembly by promoting the release of inflammasome ligands from bacteria (By similarity). Acts by promoting …

**Summary**, from NCBI Gene [2635](https://www.ncbi.nlm.nih.gov/gene/2635):

> This gene encodes a member of the guanylate-binding protein (GBP) family. GBPs specifically bind guanine nucleotides (GMP, GDP, and GTP) and contain two of the three consensus motifs found in typical GTP-binding proteins. The encoded protein interacts with a member of the germinal center kinase family. Multiple transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Jan 2017]

**Accessions** — [HGNC:4184](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4184) · Entrez [2635](https://www.ncbi.nlm.nih.gov/gene/2635) · UniProt [Q9H0R5](https://www.uniprot.org/uniprotkb/Q9H0R5) · Ensembl [ENSG00000117226](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000117226)

## Data

Gene col 3885: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3885); `tables/drug_effects.parquet` (66 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3885, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3885]; `tensor/DDL_lfc|DDL_z.npy` [3885]; `embed/gene_vectors.npy` [3885]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3885 or target_col == 3885). Every well: [[GBP3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GBP3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
