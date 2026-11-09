---
symbol: "EXOSC6"
type: "gene"
col: 13342
ensembl_id: "ENSG00000223496"
name: "exosome component 6"
location: "16q22.1"
module: 88
arm: "+"
pooled_cpm: 12.7
n_lines_expressing: 50
n_dd_up: 27
n_dd_down: 2
n_dd_up_clean: 18
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/088"]
generated_by: "tahoemap"
---

# EXOSC6

*exosome component 6* — 16q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (9 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 2.41× (z +11.1, q 9e-26, up in 43 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Verteporfin (drug)]] 5 µM: 0.655× (z -5.1, q 2e-04, down in 23 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (A-427 0.0993×); [[Orlistat (drug)]] 0.05 µM in 1 line (SNU-423 0.0781×); [[Imiquimod (hydrochloride) (drug)]] 5 µM in 1 line (SNU-423 0.115×; ⚠ toxic); [[Cobimetinib (drug)]] 5 µM in 1 line (SNU-1 0.0772×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FEM1A]] (+0.73, fdr 7e-06), [[AVEN]] (+0.71, fdr 9e-06), [[ITPRIPL2]] (+0.69, fdr 1e-05); moves opposite to [[ECI2]] (-0.68, fdr 2e-05), [[PPP1R2]] (-0.67, fdr 7e-06), [[ARL3]] (-0.64, fdr 1e-05).
> It sits in the **+** arm of [[Module 088]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[SLC16A1-AS1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 9 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13342.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **2.41×** | +11.1 | 9e-26 | 43/47 (A-172, BT-474, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.99×** | +8.7 | 1e-15 | 25/39 (NCI-H1792, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.91×** | +7.8 | 9e-13 | 15/24 (A549, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.55×** | +7.8 | 1e-12 | 28/46 (Hs 766T, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.88×** | +7.7 | 2e-12 | 31/41 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.81×** | +7.5 | 5e-12 | 30/46 (HOP62, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.80×** | +7.4 | 9e-12 | 27/38 (LS 180, SW480, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~11% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.54×** | +5.4 | 4e-06 | 26/47 (SW480, HOP62, …) | two highest doses | cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.55×** | +5.1 | 2e-05 | 14/29 (KATO III, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.46×** | +4.8 | 1e-04 | 18/48 (MIA PaCa-2, A549, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.41×** | +4.1 | 0.002 | 20/44 (SW1417, SNU-423, …) | inconsistent across doses | cell-cycle shift (explains ~16% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.39×** | +4.1 | 0.002 | 11/47 (NCI-H1792, SW480, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.40×** | +4.1 | 0.002 | 21/47 (A498, NCI-H1792, …) | two highest doses | cell-cycle shift (explains ~21% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.23×** | +3.7 | 0.010 | 12/48 (A549, PANC-1, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.34×** | +3.7 | 0.010 | 14/47 (LoVo, HEC-1-A, …) | top dose only | position effect removed |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **1.32×** | +3.5 | 0.019 | 13/45 (SHP-77, AsPC-1, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.31×** | +3.4 | 0.020 | 11/47 (KATO III, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.45×** | +3.3 | 0.026 | 7/42 (SHP-77, C-33 A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.29×** | +3.3 | 0.033 | 8/48 (A-427, J82, …) | rises with dose |  |
| [[Abiraterone acetate (drug)]] 0.05 µM |  | **1.29×** | +3.2 | 0.038 | 12/47 (hTERT-HPNE, A498, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.30×** | +3.2 | 0.042 | 15/47 (NCI-H1792, LS 180, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.29×** | +3.1 | 0.049 | 15/46 (A-172, SW480, …) | top dose only | cell-cycle shift (explains ~8% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13342.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (A-427 0.0993×); [[Orlistat (drug)]] 0.05 µM in 1 line (SNU-423 0.0781×); [[Imiquimod (hydrochloride) (drug)]] 5 µM in 1 line (SNU-423 0.115×; ⚠ toxic); [[Cobimetinib (drug)]] 5 µM in 1 line (SNU-1 0.0772×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Verteporfin (drug)]] 5 µM |  | **0.655×** | -5.1 | 2e-04 | 23/47 (A-427, NCI-H2030, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.806×** | -3.9 | 0.033 | 21/48 (KATO III, LS 180, …) | inconsistent across doses | position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | 0.768× | -3.3 | 0.16 | 12/48 (MIA PaCa-2, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.07 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13342. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 20.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.0993× (z -15.2) |
| [[BT-474 (line)]] | alt | 17.3 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 5.05× (z +8.7) | [[Niclosamide (olamine) (drug)]] 5 µM 0.195× (z -8.5) ⚠ toxic |
| [[SNU-423 (line)]] | alt | 7.82 | 0 | 2 (1 ⚠) | — | [[Orlistat (drug)]] 0.05 µM 0.0781× (z -10.1) |
| [[A-172 (line)]] | wt | 15.8 | 1 | 0 | [[Auranofin (drug)]] 5 µM 4.29× (z +9.5) | — |
| [[HOP62 (line)]] | alt | 12.5 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.30× (z +9.5) | — |
| [[Hs 766T (line)]] | wt | 10.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.43× (z +8.6) | — |
| [[SNU-1 (line)]] | wt | 9.90 | 0 | 1 | — | [[Cobimetinib (drug)]] 5 µM 0.0772× (z -9.0) |
| [[A498 (line)]] | wt | 15.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.32 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 7.84 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.68 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 20.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.67 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 14.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 13.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 8.15 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.39 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 17.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 8.71 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 9.98 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.84 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.80 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 9.10 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.07 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 8.57 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.91 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.21 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 9.16 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 16.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 9.28 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 30.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.59 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 15.7 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 26.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13342), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FEM1A]] | +0.73 | +0.74 / +0.64 | both halves | 7e-06 |  |
| [[AVEN]] | +0.71 | +0.69 / +0.57 | both halves | 9e-06 |  |
| [[ITPRIPL2]] | +0.69 | +0.70 / +0.55 | both halves | 1e-05 |  |
| [[ZSCAN29]] | +0.69 | +0.67 / +0.61 | both halves | 7e-06 |  |
| [[ST7L]] | +0.68 | +0.72 / +0.56 | both halves | 1e-05 |  |
| [[PCBD2]] | +0.67 | +0.65 / +0.55 | both halves | 1e-05 |  |
| [[AFG3L1P]] | +0.66 | +0.64 / +0.60 | both halves | 7e-06 |  |
| [[ZC3H4]] | +0.66 | +0.61 / +0.62 | both halves | 7e-06 | pathway: Nuclear RNA decay |
| [[BRD1]] | +0.65 | +0.61 / +0.48 | both halves | 2e-05 |  |
| [[SRCAP]] | +0.64 | +0.65 / +0.53 | both halves | 1e-05 |  |
| [[MBD3]] | +0.64 | +0.64 / +0.55 | both halves | 1e-05 |  |
| [[ITPA]] | +0.64 | +0.66 / +0.47 | both halves | 2e-05 | STRING 449 |

## Genes that move opposite

*19 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ECI2]] | -0.68 | -0.71 / -0.48 | both halves | 2e-05 |  |
| [[PPP1R2]] | -0.67 | -0.63 / -0.59 | both halves | 7e-06 |  |
| [[ARL3]] | -0.64 | -0.57 / -0.52 | both halves | 1e-05 |  |
| [[PGAP1]] | -0.61 | -0.59 / -0.48 | both halves | 2e-05 |  |
| [[RAB8B]] | -0.59 | -0.62 / -0.48 | both halves | 2e-05 |  |
| [[GMCL1]] | -0.59 | -0.65 / -0.40 | both halves | 5e-05 |  |
| [[CRY2]] | -0.59 | -0.54 / -0.57 | both halves | 1e-05 |  |
| [[HDAC3]] | -0.59 | -0.61 / -0.47 | both halves | 2e-05 |  |
| [[IDH2]] | -0.58 | -0.56 / -0.46 | both halves | 3e-05 |  |
| [[TMEM256]] | -0.58 | -0.64 / -0.33 | both halves | 1e-04 |  |
| [[SCPEP1]] | -0.57 | -0.49 / -0.47 | both halves | 2e-05 |  |
| [[GPR160]] | -0.57 | -0.58 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC16A1-AS1]] | B | SLC16A1-AS1 activity raises EXOSC6's level | lines that do not express SLC16A1-AS1 (5) vs lines expressing it (45) | 1.51× lower at baseline in the lines without SLC16A1-AS1 | 0.088 | ⚠ within organs, on part of the lines; also absent: P3H4, SLC16A1, DUSP19 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 088]]; 51 genes; this gene is in the **+** arm (projection on the module's main direction 0.687). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.46).
- **Nodal map** (x, y) = (7.2, -9.1); signed map (21.9, -27.4). **Vector** length 73.9, 12.5% of its response variance represented; |z| ≥ 3 in 913 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +6.3 | +11.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.9 | +7.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.9 | +4.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.8 | +7.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.5 | +4.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.0 | +3.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.8 | +3.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.6 | +2.9 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -3.6 | -3.9 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -3.5 | -3.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.5 | -0.8 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.6 | -2.8 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.6 | -1.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.2 | -1.4 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.5 | -2.0 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM |  | -1.4 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | exosome component 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q22.1 — chr16:70,246,778-70,251,940 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MTR3, hMtr3p, Mtr3p, EAP4, p11 |
| Gene groups (HGNC) | Exosome complex |
| Reactome | 20 pathways, smallest: mRNA decay by 3' to 5' exoribonuclease; Butyrate Response Factor 1 (BRF1) binds and destabilizes mRNA; KSRP (KHSRP) binds and destabilizes mRNA |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5RKV6](https://www.uniprot.org/uniprotkb/Q5RKV6) (Exosome complex component MTR3):

> Non-catalytic component of the RNA exosome complex which has 3'->5' exoribonuclease activity and participates in a multitude of cellular RNA processing and degradation events. In the nucleus, the RNA exosome complex is involved in proper maturation of stable RNA species such as rRNA, snRNA and snoRNA, in the elimination of RNA processing by-products and non-coding 'pervasive' transcripts, such as antisense RNA species and promoter-upstream transcripts (PROMPTs), and of mRNAs with processing …

**Summary**, from NCBI Gene [118460](https://www.ncbi.nlm.nih.gov/gene/118460):

> This gene product constitutes one of the subunits of the multisubunit particle called exosome, which mediates mRNA degradation. The composition of human exosome is similar to its yeast counterpart. This protein is homologous to the yeast Mtr3 protein. Its exact function is not known, however, it has been shown using a cell-free RNA decay system that the exosome is required for rapid degradation of unstable mRNAs containing AU-rich elements (AREs), but not for poly(A) shortening. The exosome …

**Accessions** — [HGNC:19055](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19055) · Entrez [118460](https://www.ncbi.nlm.nih.gov/gene/118460) · UniProt [Q5RKV6](https://www.uniprot.org/uniprotkb/Q5RKV6) · Ensembl [ENSG00000223496](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000223496)

## Data

Gene col 13342: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13342); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13342, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13342]; `tensor/DDL_lfc|DDL_z.npy` [13342]; `embed/gene_vectors.npy` [13342]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13342 or target_col == 13342). Every well: [[EXOSC6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EXOSC6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
