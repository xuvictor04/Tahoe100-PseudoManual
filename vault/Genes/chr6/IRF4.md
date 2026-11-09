---
symbol: "IRF4"
type: "gene"
col: 5991
ensembl_id: "ENSG00000137265"
name: "interferon regulatory factor 4"
location: "6p25.3"
module: 61
arm: "+"
pooled_cpm: 3.26
n_lines_expressing: 16
n_dd_up: 23
n_dd_down: 0
n_dd_up_clean: 11
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 3
direction_downstream: 3
tags: ["gene", "module/061"]
generated_by: "tahoemap"
---

# IRF4

*interferon regulatory factor 4* — 6p25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (12 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 6.27× (z +16.5, q 0e+00, up in 5 of 10 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 4 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 2 lines (C32 0.0973×, NCI-H1792 0.191×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (NCI-H1792 0.0988×, C32 0.244×; ⚠ toxic; transcription drop); [[Belinostat (drug)]] 5 µM in 1 line (NCI-H1792 0.0575×; ⚠ cell-cycle shift, would explain all of this change); [[Harringtonine (drug)]] 5 µM in 1 line (NCI-H1792 0.124×); [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM in 1 line (NCI-H1573 0.0304×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H1792 0.357×).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CRTAC1]] (+0.59, fdr 1e-05), [[LINC01579]] (+0.53, fdr 8e-05), [[MIR4300HG]] (+0.51, fdr 7e-05); moves opposite to [[POFUT1]] (-0.39, fdr 2e-04).
> It is in [[Module 061]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[ADGRA2]] → it (grade B ⚠); 3 go from it, the strongest it → [[IGSF11]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 12 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5991.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **6.27×** | +16.5 | 0e+00 | 5/10 (NCI-H460, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **3.38×** | +10.9 | 3e-25 | 4/10 (C32, HOP62, …) | rises with dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.45×** | +10.3 | 9e-23 | 0/2 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.98×** | +8.8 | 3e-16 | 0/4 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.52×** | +7.4 | 2e-11 | 0/2 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.38×** | +5.3 | 1e-05 | 0/6 | top dose only | cell-cycle shift (explains ~0% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **3.18×** | +5.2 | 1e-05 | 0/4 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.02×** | +4.3 | 0.001 | 0/4 | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.96×** | +4.2 | 0.001 | 0/5 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.95×** | +4.2 | 0.001 | 4/9 (C32, HOP62, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.75×** | +3.5 | 0.020 | 1/6 (C32) | inconsistent across doses | low cells (technical?) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.79×** | +3.5 | 0.020 | 1/10 (C32) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.48×** | +3.5 | 0.020 | 4/10 (NCI-H1573, HOP62, …) | rises with dose |  |
| [[Fingolimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.73×** | +3.4 | 0.023 | 0/9 | top dose only | position effect removed |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.76×** | +3.4 | 0.030 | 0/2 | top dose only | noisy plate (z scaled) |
| [[Doxycycline (monohydrate) (drug)]] 0.5 µM |  | **1.69×** | +3.3 | 0.036 | 0/9 | inconsistent across doses | position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.44×** | +3.2 | 0.043 | 2/10 (C32, SK-MEL-2) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Temsirolimus (drug)]] 0.5 µM |  | **1.63×** | +3.1 | 0.062 | 1/5 (NCI-H1573) | inconsistent across doses |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.94×** | +3.0 | 0.079 | 0/4 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Pimozide (drug)]] 0.05 µM |  | **1.60×** | +3.0 | 0.081 | 0/6 | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5991.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 4 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 2 lines (C32 0.0973×, NCI-H1792 0.191×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (NCI-H1792 0.0988×, C32 0.244×; ⚠ toxic; transcription drop); [[Belinostat (drug)]] 5 µM in 1 line (NCI-H1792 0.0575×; ⚠ cell-cycle shift, would explain all of this change); [[Harringtonine (drug)]] 5 µM in 1 line (NCI-H1792 0.124×); [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM in 1 line (NCI-H1573 0.0304×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H1792 0.357×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Rutin (trihydrate) (drug)]] 0.05 µM |  | 0.581× | -3.2 | 0.35 | 0/11 | inconsistent across doses |  |
| [[(S)-Crizotinib (drug)]] 0.05 µM |  | 0.582× | -3.2 | 0.35 | 2/10 (A549, NCI-H2030) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, +0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5991. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1792 (line)]] | alt | 36.7 | 0 | 6 (4 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0575× (z -16.7) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.124× (z -11.8) |
| [[C32 (line)]] | wt | 96.1 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.11× (z +17.8) | [[Dinaciclib (drug)]] 0.05 µM 0.0973× (z -15.1) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 4.52 | 0 | 1 | — | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM 0.0304× (z -10.1) |
| [[A-172 (line)]] | wt | 0.417 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.435 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.436 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.13 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.905 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.326 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.294 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.458 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.75 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.368 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 2.66 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.469 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.333 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.451 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.519 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.953 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.327 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.391 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.405 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.448 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.368 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.354 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.335 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.515 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.274 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.276 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.891 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.76 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.773 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.267 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.931 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.20 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.988 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.257 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.299 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.373 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.644 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.337 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.839 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.809 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.13 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.717 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.578 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.308 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.601 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.316 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5991), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CRTAC1]] | +0.59 | +0.54 / +0.61 | both halves | 1e-05 |  |
| [[LINC01579]] | +0.53 | +0.37 / +0.45 | both halves | 8e-05 |  |
| [[MIR4300HG]] | +0.51 | +0.38 / +0.47 | both halves | 7e-05 |  |
| [[RORB]] | +0.50 | +0.39 / +0.50 | both halves | 5e-05 |  |
| [[KCNIP1]] | +0.50 | +0.35 / +0.48 | both halves | 1e-04 |  |
| [[C2CD6]] | +0.49 | +0.40 / +0.51 | both halves | 5e-05 |  |
| [[SGCD]] | +0.49 | +0.41 / +0.49 | both halves | 4e-05 |  |
| [[DNAH2]] | +0.48 | +0.43 / +0.46 | both halves | 3e-05 |  |
| [[CFAP20DC-DT]] | +0.48 | +0.39 / +0.41 | both halves | 6e-05 |  |
| [[PKNOX2]] | +0.48 | +0.36 / +0.47 | both halves | 9e-05 |  |
| [[FAM13C]] | +0.48 | +0.40 / +0.45 | both halves | 4e-05 |  |
| [[HS6ST3]] | +0.48 | +0.32 / +0.44 | both halves | 1e-04 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POFUT1]] | -0.39 | -0.31 / -0.36 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 1, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ADGRA2]] | B | ADGRA2 activity lowers IRF4's level | lines that do not express ADGRA2 (11) vs lines expressing it (39) | 1.22× higher at baseline in the lines without ADGRA2 | 0.061 | ⚠ within organs, on part of the lines; also absent: CERCAM, SPEG, STARD9; maybe low, not absent |
| [[FYB1]] | C | FYB1 activity raises IRF4's level | lines that do not express FYB1 (32) vs lines expressing it (18) | 2.26× lower at baseline in the lines without FYB1 | 0.042 | ⚠ within organs, on part of the lines; also absent: AMPH, IRAG2, ENSG00000266450; co-absent with the target |
| [[DCT]] | C | DCT activity raises IRF4's level | lines that do not express DCT (42) vs lines expressing it (8) | 3.10× lower at baseline in the lines without DCT | 0.060 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: LHFPL3-AS1, TYR, GTF2I-AS1; co-absent with the target |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IGSF11]] | B | IRF4 activity raises IGSF11's level | lines that do not express IRF4 (34) vs lines expressing it (16) | 1.99× lower at baseline in the lines without IRF4 | 0.039 | ⚠ within organs, on part of the lines; also absent: CHL1, CPS1, UPK1B |
| [[PRKCA-AS1]] | B | IRF4 activity raises PRKCA-AS1's level | lines that do not express IRF4 (34) vs lines expressing it (16) | 1.12× lower at baseline in the lines without IRF4 | 0.065 | ⚠ within organs, on part of the lines; also absent: CHL1, CPS1, UPK1B |
| [[MAF]] | C | IRF4 activity raises MAF's level | lines that do not express IRF4 (34) vs lines expressing it (16) | 2.72× lower at baseline in the lines without IRF4 | 0.067 | ⚠ within organs, on part of the lines; also absent: CHL1, CPS1, UPK1B; co-absent with the target |

## Where it sits

- **Module**: [[Module 061]] — Neuronal System; 78 genes; every member is in the + arm (projection on the module's main direction 0.402). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.25; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (23.0, 31.9); signed map (30.7, 14.8). **Vector** length 33.5, 9.85% of its response variance represented; |z| ≥ 3 in 289 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.6 | +16.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.5 | +10.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.5 | +8.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.2 | +7.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +2.1 | +10.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.7 | +2.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.7 | +3.5 |
|  | [[Entrectinib (drug)]] 5 µM |  | +0.8 | +2.6 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +0.8 | +3.0 |
|  | [[Cepharanthine (drug)]] 5 µM |  | +0.8 | +1.8 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -0.9 | -0.7 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -0.9 | +1.9 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -0.9 | -1.1 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -0.9 | -1.2 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -0.7 | +0.0 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -0.6 | -2.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -0.6 | -2.0 |
|  | [[Neratinib (drug)]] 5 µM |  | -0.5 | +0.2 |

## What is on record

|  |  |
|---|---|
| Name | interferon regulatory factor 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p25.3 — chr6:391,739-411,443 (+) |
| Ensembl biotype | protein_coding |
| Also known as | LSIRF; previously MUM1 |
| Gene groups (HGNC) | Interferon regulatory factors |
| Hallmark sets | ALLOGRAFT_REJECTION, IL2_STAT5_SIGNALING, INTERFERON_GAMMA_RESPONSE |
| Reactome | 18 pathways, smallest: Nuclear events stimulated by ALK signaling in cancer; Regulation of MITF-M-dependent genes involved in pigmentation; Interferon alpha/beta signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15306](https://www.uniprot.org/uniprotkb/Q15306) (Interferon regulatory factor 4):

> Transcriptional activator. Binds to the interferon-stimulated response element (ISRE) of the MHC class I promoter. Binds the immunoglobulin lambda light chain enhancer, together with PU.1. Probably plays a role in ISRE-targeted signal transduction mechanisms specific to lymphoid cells. Involved in CD8(+) dendritic cell differentiation by forming a complex with the BATF-JUNB heterodimer in immune cells, leading to recognition of AICE sequence (5'-TGAnTCA/GAAA-3'), an immune-specific regulatory …

**Summary**, from NCBI Gene [3662](https://www.ncbi.nlm.nih.gov/gene/3662):

> The protein encoded by this gene belongs to the IRF (interferon regulatory factor) family of transcription factors, characterized by an unique tryptophan pentad repeat DNA-binding domain. The IRFs are important in the regulation of interferons in response to infection by virus, and in the regulation of interferon-inducible genes. This family member is lymphocyte specific and negatively regulates Toll-like-receptor (TLR) signaling that is central to the activation of innate and adaptive immune …

**Accessions** — [HGNC:6119](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6119) · Entrez [3662](https://www.ncbi.nlm.nih.gov/gene/3662) · UniProt [Q15306](https://www.uniprot.org/uniprotkb/Q15306) · Ensembl [ENSG00000137265](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000137265)

## Data

Gene col 5991: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5991); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5991, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5991]; `tensor/DDL_lfc|DDL_z.npy` [5991]; `embed/gene_vectors.npy` [5991]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5991 or target_col == 5991). Every well: [[IRF4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IRF4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
