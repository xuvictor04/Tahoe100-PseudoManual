---
symbol: "TIFA"
type: "gene"
col: 6983
ensembl_id: "ENSG00000145365"
name: "TRAF interacting protein with forkhead associated domain"
location: "4q25"
module: 14
arm: "+"
pooled_cpm: 11.67
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 8
n_dd_up_clean: 7
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/014"]
generated_by: "tahoemap"
---

# TIFA

*TRAF interacting protein with forkhead associated domain* — 4q25

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (9 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 4.36× (z +28.9, q 0e+00, up in 42 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.628× (z -6.4, q 6e-08, down in 25 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ATP23]] (+0.74, fdr 7e-06), [[FAM111A-DT]] (+0.73, fdr 7e-06), [[TNFAIP2]] (+0.66, fdr 7e-06); moves opposite to [[TANGO2]] (-0.59, fdr 1e-05), [[UFD1]] (-0.58, fdr 1e-05), [[CAP1]] (-0.58, fdr 3e-05).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[PDGFRL]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 9 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6983.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **4.36×** | +28.9 | 0e+00 | 42/46 (HEC-1-A, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **4.40×** | +19.8 | 0e+00 | 44/46 (HEC-1-A, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.15×** | +10.6 | 6e-24 | 27/44 (HEC-1-A, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[TAK-901 (drug)]] 5 µM |  | **4.12×** | +10.3 | 1e-22 | 40/47 (HEC-1-A, BT-474, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.63×** | +9.6 | 8e-20 | 32/45 (J82, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~6% here); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.95×** | +9.3 | 2e-18 | 29/46 (HEC-1-A, C32, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **1.72×** | +7.5 | 6e-12 | 26/45 (NCI-H1792, BT-474, …) | rises with dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.60×** | +6.5 | 4e-09 | 23/47 (NCI-H2347, BT-474, …) | inconsistent across doses | composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.40×** | +4.7 | 2e-04 | 19/46 (Panc 03.27, LoVo, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~37% of this change | **1.41×** | +4.6 | 3e-04 | 18/42 (LoVo, RKO, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~50% of this change | **1.35×** | +4.1 | 0.002 | 16/42 (Panc 03.27, CFPAC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.35×** | +4.0 | 0.003 | 13/42 (NCI-H2030, J82, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.64×** | +3.6 | 0.014 | 10/45 (NCI-H460, LoVo, …) | rises with dose | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change | **1.32×** | +3.6 | 0.014 | 10/32 (HOP62, C32, …) | inconsistent across doses | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **1.26×** | +3.3 | 0.043 | 9/46 (BT-474, NCI-H1792, …) | rises with dose | position effect removed |
| [[Radotinib (drug)]] 5 µM |  | 1.18× | +3.2 | 0.043 | 11/47 (Panc 03.27, SHP-77, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 3 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6983.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.628×** | -6.4 | 6e-08 | 25/47 (RKO, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.679×** | -5.4 | 2e-05 | 22/46 (SW48, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.690×** | -5.1 | 5e-05 | 14/36 (A498, NCI-H2347, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.715×** | -4.5 | 0.001 | 13/25 (HEC-1-A, J82, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Temsirolimus (drug)]] 0.05 µM |  | **0.781×** | -3.4 | 0.061 | 13/47 (NCI-H1573, SNU-1, …) | inconsistent across doses |  |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **0.782×** | -3.4 | 0.061 | 12/46 (SNU-1, SW48, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.785×** | -3.4 | 0.063 | 15/46 (SK-MEL-2, H4, …) | rises with dose | low cells (technical?) |
| [[Temsirolimus (drug)]] 0.5 µM |  | **0.787×** | -3.3 | 0.065 | 11/44 (C32, Panc 03.27, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | 0.791× | -3.1 | 0.11 | 7/45 (H4, A-427, …) | rises with dose |  |
| [[Rapamycin (drug)]] 0.5 µM |  | 0.801× | -3.1 | 0.12 | 13/45 (BT-474, NCI-H1792, …) | rises with dose |  |
| [[Almonertinib (hydrochloride) (drug)]] 0.5 µM |  | 0.804× | -3.0 | 0.13 | 10/45 (J82, H4, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.16 per unit of S-phase module lfc, +0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6983. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 24.2 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.00× (z +20.4) | [[Dinaciclib (drug)]] 5 µM 0.112× (z -16.9) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 11.8 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.19× (z +12.2) | [[Dinaciclib (drug)]] 5 µM 0.0955× (z -10.8) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 10.1 | 4 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.29× (z +15.3) | [[Dinaciclib (drug)]] 5 µM 0.126× (z -10.9) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 23.2 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.56× (z +14.1) | [[Dinaciclib (drug)]] 0.5 µM 0.283× (z -10.0) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 12.7 | 3 | 1 | [[Homoharringtonine (drug)]] 5 µM 6.57× (z +13.3) | [[Temsirolimus (drug)]] 0.5 µM 0.179× (z -8.7) |
| [[NCI-H460 (line)]] | wt | 7.87 | 3 | 1 | [[Homoharringtonine (drug)]] 5 µM 4.29× (z +12.1) | [[Isocorydine (drug)]] 0.5 µM 0.233× (z -8.6) |
| [[A549 (line)]] | wt | 7.39 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 17.1× (z +16.9) | — |
| [[hTERT-HPNE (line)]] | wt | 15.1 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.8× (z +14.6) | — |
| [[NCI-H2347 (line)]] | alt | 15.6 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.83× (z +19.1) | — |
| [[PANC-1 (line)]] | alt | 6.53 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.76× (z +16.1) | — |
| [[SNU-1 (line)]] | wt | 20.9 | 1 | 2 | [[Homoharringtonine (drug)]] 0.5 µM 6.44× (z +8.7) | [[Tofacitinib (citrate) (drug)]] 0.5 µM 0.0618× (z -13.0) |
| [[A-172 (line)]] | wt | 9.23 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.20× (z +12.7) | — |
| [[BT-474 (line)]] | alt | 11.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.5× (z +15.7) | — |
| [[HepG2_C3A (line)]] | wt | 10.7 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.28× (z +11.1) | [[Pimozide (drug)]] 0.5 µM 0.109× (z -8.7) ⚠ transcription drop |
| [[HOP62 (line)]] | alt | 6.46 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 19.9× (z +19.0) | — |
| [[Panc 03.27 (line)]] | alt | 12.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.00× (z +14.7) | — |
| [[SW48 (line)]] | wt | 33.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.45× (z +11.6) | — |
| [[CFPAC-1 (line)]] | alt | 9.70 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.36× (z +13.0) | — |
| [[COLO 205 (line)]] | alt | 12.5 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.139× (z -8.9) |
| [[Hs 766T (line)]] | wt | 13.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.18× (z +9.8) | — |
| [[HT-29 (line)]] | alt | 8.57 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.17× (z +11.1) | — |
| [[LoVo (line)]] | wt | 15.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.77× (z +10.1) | — |
| [[MIA PaCa-2 (line)]] | alt | 10.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.10× (z +10.2) | — |
| [[NCI-H2030 (line)]] | alt | 11.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.13× (z +9.0) | — |
| [[NCI-H23 (line)]] | alt | 4.83 | 0 | 1 | — | [[18β-Glycyrrhetinic acid (drug)]] 0.5 µM 0.0797× (z -9.4) |
| [[RKO (line)]] | wt | 24.9 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.253× (z -9.1) |
| [[RPMI-7951 (line)]] | alt | 12.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.94× (z +10.6) | — |
| [[SHP-77 (line)]] | alt | 7.74 | 0 | 1 | — | [[Ixazomib (drug)]] 0.05 µM 0.0956× (z -8.5) |
| [[SK-MEL-2 (line)]] | alt | 13.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.31× (z +9.9) | — |
| [[SNU-423 (line)]] | alt | 7.93 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.66× (z +9.7) | — |
| [[SW 900 (line)]] | alt | 12.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.95× (z +11.9) | — |
| [[SW480 (line)]] | alt | 8.83 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.239× (z -9.8) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 8.13 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.92 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 14.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 9.99 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 8.31 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 7.67 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 8.19 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.69 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.63 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.37 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.91 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.35 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6983), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATP23]] | +0.74 | +0.76 / +0.61 | both halves | 7e-06 |  |
| [[FAM111A-DT]] | +0.73 | +0.69 / +0.64 | both halves | 7e-06 |  |
| [[TNFAIP2]] | +0.66 | +0.60 / +0.66 | both halves | 7e-06 |  |
| [[DENND2B]] | +0.65 | +0.58 / +0.63 | both halves | 7e-06 |  |
| [[IKBKE]] | +0.65 | +0.67 / +0.59 | both halves | 7e-06 | pathway: MyD88-independent TLR4 cascade |
| [[CSF1]] | +0.63 | +0.58 / +0.63 | both halves | 7e-06 |  |
| [[OGFRL1]] | +0.63 | +0.70 / +0.46 | both halves | 3e-05 |  |
| [[STAT5A]] | +0.63 | +0.60 / +0.56 | both halves | 1e-05 |  |
| [[BCOR]] | +0.62 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[STAP2]] | +0.61 | +0.58 / +0.53 | both halves | 1e-05 |  |
| [[SLC16A9]] | +0.61 | +0.57 / +0.45 | both halves | 3e-05 |  |
| [[PATL1]] | +0.61 | +0.57 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TANGO2]] | -0.59 | -0.55 / -0.53 | both halves | 1e-05 |  |
| [[UFD1]] | -0.58 | -0.53 / -0.56 | both halves | 1e-05 |  |
| [[CAP1]] | -0.58 | -0.60 / -0.45 | both halves | 3e-05 |  |
| [[HERC2P3]] | -0.58 | -0.51 / -0.42 | both halves | 4e-05 |  |
| [[PWWP3A]] | -0.57 | -0.52 / -0.48 | both halves | 2e-05 |  |
| [[DIP2A]] | -0.57 | -0.61 / -0.47 | both halves | 2e-05 |  |
| [[CDC42BPB]] | -0.57 | -0.51 / -0.49 | both halves | 1e-05 |  |
| [[BCAP31]] | -0.57 | -0.54 / -0.53 | both halves | 1e-05 |  |
| [[SAMD4B]] | -0.56 | -0.49 / -0.51 | both halves | 1e-05 |  |
| [[KLC1]] | -0.55 | -0.63 / -0.54 | both halves | 1e-05 |  |
| [[HERC2P2]] | -0.55 | -0.53 / -0.36 | both halves | 9e-05 |  |
| [[GALNS]] | -0.55 | -0.55 / -0.36 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PDGFRL]] | B | PDGFRL activity raises TIFA's level | lines that do not express PDGFRL (16) vs lines expressing it (34) | 1.31× lower at baseline in the lines without PDGFRL | 0.007 | ⚠ within organs, on part of the lines; also absent: SLC16A7, ITPR1, TOX2 |
| [[LINC02605]] | B | LINC02605 activity raises TIFA's level | lines that do not express LINC02605 (15) vs lines expressing it (35) | 1.18× lower at baseline in the lines without LINC02605 | 0.063 | ⚠ within organs, on part of the lines; also absent: ENSG00000285744, FAR2, ENSG00000285517 |
| [[CSF1]] | B | CSF1 activity raises TIFA's level | lines that do not express CSF1 (21) vs lines expressing it (29) | 1.26× lower at baseline in the lines without CSF1 | 0.095 | ⚠ within organs, on part of the lines; also absent: SERPINE1, TNFRSF9, ROR1-AS1 |
| [[IKBKE]] | C | IKBKE activity raises TIFA's level | lines that do not express IKBKE (4) vs lines expressing it (46) | 2.01× lower at baseline in the lines without IKBKE | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SP100, NAT1, NDRG1; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction 0.737). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (23.1, 5.4); signed map (43.6, 5.3). **Vector** length 89.5, 18.6% of its response variance represented; |z| ≥ 3 in 990 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +7.5 | +19.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +7.1 | +28.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.6 | +9.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.1 | +10.6 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +3.2 | +1.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.1 | +2.7 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.3 | +3.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.0 | +0.5 |
|  | [[venetoclax (drug)]] 5 µM |  | +1.8 | +2.0 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +1.7 | +1.3 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -4.9 | -5.4 |
|  | [[Panobinostat (drug)]] 5 µM |  | -4.8 | -6.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -4.6 | -1.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.4 | -1.7 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -4.3 | -1.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.8 | -1.9 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -2.2 | -0.8 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.2 | -2.3 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -1.8 | -3.4 |

## What is on record

|  |  |
|---|---|
| Name | TRAF interacting protein with forkhead associated domain |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q25 — chr4:112,272,968-112,285,955 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC20791, T2BP, T6BP, TIFAA |
| Reactome | 23 pathways, smallest: Alpha-protein kinase 1 signaling pathway; TAK1-dependent IKK and NF-kappa-B activation; MyD88 cascade initiated on plasma membrane |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96CG3](https://www.uniprot.org/uniprotkb/Q96CG3) (TRAF-interacting protein with FHA domain-containing protein A):

> Adapter molecule that plays a key role in the activation of pro-inflammatory NF-kappa-B signaling following detection of bacterial pathogen-associated molecular pattern metabolites (PAMPs). Promotes activation of an innate immune response by inducing the oligomerization and polyubiquitination of TRAF6, which leads to the activation of TAK1 and IKK through a proteasome-independent mechanism. TIFA-dependent innate immune response is triggered by ADP-D-glycero-beta-D-manno-heptose (ADP-Heptose), a …

**Summary**, from NCBI Gene [92610](https://www.ncbi.nlm.nih.gov/gene/92610):

> This gene encodes an adapter protein involved in adaptive and innate immunity. This protein includes a forkhead-associated (FHA) domain that specifically binds to phosphorylated serine and threonine residues. In response to bacterial infection, the encoded host cell protein undergoes an intermolecular interaction between the FHA domain and a phosphorylated threonine that leads to protein oligomerization and stimulation of the NF-kappa B and other downstream signaling pathways. This protein …

**Accessions** — [HGNC:19075](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19075) · Entrez [92610](https://www.ncbi.nlm.nih.gov/gene/92610) · UniProt [Q96CG3](https://www.uniprot.org/uniprotkb/Q96CG3) · Ensembl [ENSG00000145365](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000145365)

## Data

Gene col 6983: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6983); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6983, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6983]; `tensor/DDL_lfc|DDL_z.npy` [6983]; `embed/gene_vectors.npy` [6983]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6983 or target_col == 6983). Every well: [[TIFA — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TIFA.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
