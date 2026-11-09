---
symbol: "SAMD4A-AS1"
type: "gene"
col: 16148
ensembl_id: "ENSG00000285774"
name: "SAMD4A antisense RNA 1"
location: "14q22.2"
module: 21
arm: "+"
pooled_cpm: 4.23
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 0
n_dd_up_clean: 10
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/021"]
generated_by: "tahoemap"
---

# SAMD4A-AS1

*SAMD4A antisense RNA 1* — 14q22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.50× (z +12.6, q 7e-34, up in 28 of 38 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Drospirenone (drug)]] 0.5 µM in 1 line (J82 0.0726×); [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM in 1 line (NCI-H2030 0.120×); [[Ponatinib (drug)]] 5 µM in 1 line (HepG2/C3A 0.0838×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RBMS3-AS3]] (+0.75, fdr 7e-06), [[MAP3K20-AS1]] (+0.74, fdr 7e-06), [[SPATC1]] (+0.73, fdr 7e-06); moves opposite to [[SKP2]] (-0.63, fdr 1e-05), [[NUDT21]] (-0.60, fdr 2e-05), [[ACTR5]] (-0.60, fdr 5e-05).
> It is in [[Module 021]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[LY6K]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 8 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 16148.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.50×** | +12.6 | 7e-34 | 28/38 (NCI-H460, HOP62, …) | rises with dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.00×** | +9.6 | 3e-19 | 32/38 (LoVo, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.38×** | +8.4 | 6e-15 | 16/25 (HEC-1-A, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.19×** | +7.3 | 3e-11 | 3/9 (J82, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.72×** | +5.3 | 2e-05 | 17/37 (NCI-H460, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.66×** | +4.9 | 8e-05 | 9/28 (NCI-H460, PANC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~25% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.76×** | +4.8 | 1e-04 | 3/11 (HS-578T, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.63×** | +4.8 | 1e-04 | 13/36 (A498, NCI-H460, …) | top dose only | cell-cycle shift (explains ~13% here); position effect removed |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.41×** | +4.7 | 1e-04 | 13/45 (NCI-H1573, MIA PaCa-2, …) | rises with dose | position effect removed |
| [[Peretinoin (drug)]] 5 µM |  | **1.52×** | +4.0 | 0.004 | 13/44 (LS 180, NCI-H23, …) | rises with dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.46×** | +3.7 | 0.013 | 13/47 (LS 180, NCI-H2347, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.42×** | +3.4 | 0.032 | 16/44 (NCI-H23, SW480, …) | top dose only |  |
| [[vincristine (drug)]] 0.5 µM |  | **1.62×** | +3.4 | 0.032 | 6/36 (CFPAC-1, A549, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled); position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.42×** | +3.3 | 0.038 | 11/44 (J82, hTERT-HPNE, …) | rises with dose | composition shift; position effect removed |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.40×** | +3.3 | 0.041 | 6/47 (A498, HT-29, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.39×** | +3.1 | 0.070 | 10/36 (SW480, C32, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.38×** | +3.0 | 0.077 | 8/33 (HS-578T, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 16148.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Drospirenone (drug)]] 0.5 µM in 1 line (J82 0.0726×); [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM in 1 line (NCI-H2030 0.120×); [[Ponatinib (drug)]] 5 µM in 1 line (HepG2/C3A 0.0838×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.879× | -4.6 | 0.002 | 22/48 (A-172, COLO 205, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM |  | 0.706× | -3.4 | 0.18 | 12/46 (C32, A549, …) | two highest doses | cell-cycle shift (explains ~19% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.21 per unit of S-phase module lfc, +0.34 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 16148. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[J82 (line)]] | alt | 4.50 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 5.74× (z +9.3) | [[Drospirenone (drug)]] 0.5 µM 0.0726× (z -9.7) |
| [[HepG2_C3A (line)]] | wt | 9.15 | 0 | 1 | — | [[Ponatinib (drug)]] 5 µM 0.0838× (z -8.6) |
| [[HOP62 (line)]] | alt | 4.38 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.68× (z +9.8) | — |
| [[NCI-H2030 (line)]] | alt | 8.90 | 0 | 1 | — | [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM 0.120× (z -9.1) |
| [[NCI-H460 (line)]] | wt | 5.14 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.36× (z +10.6) | — |
| [[A-172 (line)]] | wt | 3.63 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.54 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.23 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.49 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.37 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.34 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.31 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.15 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.30 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.68 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.03 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.60 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.22 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.37 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.85 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.99 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.65 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.34 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.06 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.75 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.47 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 6.42 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.69 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.76 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.26 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.63 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.24 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.06 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.39 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.65 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.94 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.96 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.59 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.60 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.18 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.33 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.47 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.98 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.13 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.28 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.26 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.02 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.95 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.33 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.50 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 16148), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RBMS3-AS3]] | +0.75 | +0.73 / +0.68 | both halves | 7e-06 | same gene group |
| [[MAP3K20-AS1]] | +0.74 | +0.73 / +0.62 | both halves | 7e-06 | same gene group |
| [[SPATC1]] | +0.73 | +0.78 / +0.61 | both halves | 7e-06 |  |
| [[PPP1R12A-AS2]] | +0.71 | +0.70 / +0.66 | both halves | 7e-06 | same gene group |
| [[ASB14]] | +0.70 | +0.71 / +0.62 | both halves | 7e-06 |  |
| [[SAMD4A]] | +0.70 | +0.68 / +0.65 | both halves | 7e-06 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[STARD13-AS]] | +0.69 | +0.60 / +0.72 | both halves | 7e-06 | same gene group |
| [[TTC36-AS1]] | +0.69 | +0.65 / +0.67 | both halves | 7e-06 | same gene group |
| [[PKD2L2]] | +0.69 | +0.62 / +0.65 | both halves | 7e-06 |  |
| [[MIR4300HG]] | +0.68 | +0.70 / +0.54 | both halves | 1e-05 |  |
| [[EYS]] | +0.68 | +0.75 / +0.53 | both halves | 1e-05 |  |
| [[DLGAP4-AS1]] | +0.67 | +0.63 / +0.58 | both halves | 7e-06 | same gene group |
| [[ARHGAP15]] | +0.67 | +0.68 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SKP2]] | -0.63 | -0.58 / -0.54 | both halves | 1e-05 |  |
| [[NUDT21]] | -0.60 | -0.61 / -0.47 | both halves | 2e-05 |  |
| [[ACTR5]] | -0.60 | -0.65 / -0.40 | both halves | 5e-05 |  |
| [[FBXW2]] | -0.59 | -0.58 / -0.50 | both halves | 1e-05 |  |
| [[PPP5C]] | -0.59 | -0.60 / -0.58 | both halves | 8e-06 |  |
| [[CASP2]] | -0.58 | -0.54 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LY6K]] | B | LY6K activity raises SAMD4A-AS1's level | lines that do not express LY6K (32) vs lines expressing it (18) | 1.27× lower at baseline in the lines without LY6K | 0.041 | ⚠ within organs, on part of the lines; also absent: IL6, STEAP1B-AS1, TNIP3 |
| [[EMP3]] | B | EMP3 activity raises SAMD4A-AS1's level | lines that do not express EMP3 (9) vs lines expressing it (41) | 1.25× lower at baseline in the lines without EMP3 | 0.062 | ⚠ within organs, on part of the lines; also absent: LGALS1, SYDE1, SPAG17 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 021]]; 188 genes; every member is in the + arm (projection on the module's main direction 0.622). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (17.0, 25.6); signed map (30.7, 9.0). **Vector** length 55.2, 7.16% of its response variance represented; |z| ≥ 3 in 947 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +6.8 | +12.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.5 | +9.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.8 | +5.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.9 | +8.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +2.7 | +3.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.6 | +2.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.3 | +4.7 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.1 | +4.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.8 | +3.4 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.7 | +2.8 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -1.7 | -2.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.6 | -2.4 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.5 | -1.0 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.4 | -2.1 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -1.3 | -3.4 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.3 | -1.8 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.2 | -1.4 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -1.2 | -1.7 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -1.1 | -0.1 |

## What is on record

|  |  |
|---|---|
| Name | SAMD4A antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 14q22.2 — chr14:54,684,026-54,729,324 (-) |
| Ensembl biotype | lncRNA |
| Also known as | lnc-GCH1-2:3 |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:54803](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:54803) · Entrez [729451](https://www.ncbi.nlm.nih.gov/gene/729451) · Ensembl [ENSG00000285774](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000285774)

## Data

Gene col 16148: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 16148); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 16148, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 16148]; `tensor/DDL_lfc|DDL_z.npy` [16148]; `embed/gene_vectors.npy` [16148]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 16148 or target_col == 16148). Every well: [[SAMD4A-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SAMD4A-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
