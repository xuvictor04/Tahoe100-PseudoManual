---
symbol: "SNAP25-AS1"
type: "gene"
col: 13613
ensembl_id: "ENSG00000227906"
name: "SNAP25 antisense RNA 1"
location: "20p12.2"
module: 21
arm: "+"
pooled_cpm: 7.4
n_lines_expressing: 50
n_dd_up: 24
n_dd_down: 1
n_dd_up_clean: 13
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/021"]
generated_by: "tahoemap"
---

# SNAP25-AS1

*SNAP25 antisense RNA 1* — 20p12.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.26× (z +15.6, q 0e+00, up in 27 of 29 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.78× (z +15.6, q 0e+00, up in 36 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.908× (z -3.9, q 0.036, down in 14 of 48 measured lines) ⚠ position not correctable. The strongest without an alert is [[Betamethasone dipropionate (drug)]] 0.05 µM: 0.682× (z -3.8, q 0.036, down in 14 of 43 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Fluvoxamine (drug)]] 5 µM in 1 line (HEC-1-A 0.0587×); [[Triamcinolone (drug)]] 0.5 µM in 1 line (hTERT-HPNE 0.0845×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SPATA21]] (+0.76, fdr 7e-06), [[MROH8]] (+0.73, fdr 7e-06), [[KIAA2012]] (+0.72, fdr 7e-06).
> It is in [[Module 021]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[SNAP25]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 11 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13613.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.26×** | +15.6 | 0e+00 | 27/29 (LoVo, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.78×** | +15.6 | 0e+00 | 36/40 (HOP62, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.20×** | +14.9 | 0e+00 | 11/12 (HOP62, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.57×** | +12.7 | 9e-35 | 15/18 (HOP62, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.81×** | +9.1 | 1e-17 | 23/40 (HOP62, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.83×** | +6.3 | 3e-08 | 15/33 (NCI-H460, SNU-423, …) | top dose only | cell-cycle shift (explains ~10% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.65×** | +5.2 | 2e-05 | 12/32 (CFPAC-1, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.59×** | +5.0 | 5e-05 | 17/45 (MIA PaCa-2, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.57×** | +4.8 | 8e-05 | 13/45 (KATO III, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.83×** | +4.6 | 2e-04 | 10/45 (CFPAC-1, KATO III, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.52×** | +4.5 | 3e-04 | 14/45 (HOP62, SW480, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.34×** | +4.5 | 3e-04 | 16/46 (A498, MIA PaCa-2, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.51×** | +4.5 | 3e-04 | 14/45 (HOP62, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.42×** | +3.8 | 0.006 | 14/45 (KATO III, CFPAC-1, …) | rises with dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.94×** | +3.7 | 0.007 | 1/12 (SHP-77) | top dose only | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.26×** | +3.5 | 0.017 | 13/47 (HOP62, NCI-H460, …) | top dose only |  |
| [[Verteporfin (drug)]] 5 µM |  | **1.39×** | +3.4 | 0.022 | 3/43 (KATO III, Hs 766T, …) | top dose only | position effect removed |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.33×** | +3.1 | 0.063 | 6/45 (A-172, PANC-1, …) | inconsistent across doses |  |
| [[Terfenadine (drug)]] 5 µM |  | **1.21×** | +3.0 | 0.075 | 8/46 (AN3 CA, AsPC-1, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13613.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Fluvoxamine (drug)]] 5 µM in 1 line (HEC-1-A 0.0587×); [[Triamcinolone (drug)]] 0.5 µM in 1 line (hTERT-HPNE 0.0845×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.908× | -3.9 | 0.036 | 14/48 (C-33 A, NCI-H1792, …) | inconsistent across doses |  |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **0.682×** | -3.8 | 0.036 | 14/43 (Panc 03.27, LoVo, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 0.05 µM |  | 0.734× | -3.2 | 0.30 | 7/46 (A-427, LS 180, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13613. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 18.4 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 13.6× (z +20.9) | — |
| [[NCI-H460 (line)]] | wt | 7.96 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.34× (z +14.4) | — |
| [[RPMI-7951 (line)]] | alt | 34.4 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 13.8× (z +20.0) | — |
| [[hTERT-HPNE (line)]] | wt | 7.44 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 6.91× (z +9.6) | [[Triamcinolone (drug)]] 0.5 µM 0.0845× (z -8.6) |
| [[HEC-1-A (line)]] | alt | 2.97 | 0 | 1 | — | [[Fluvoxamine (drug)]] 5 µM 0.0587× (z -9.4) |
| [[LoVo (line)]] | wt | 6.02 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 14.6× (z +11.1) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 30.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.22× (z +13.4) | — |
| [[PANC-1 (line)]] | alt | 3.10 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.90× (z +8.6) | — |
| [[SW 900 (line)]] | alt | 6.45 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 15.9× (z +8.7) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 4.20 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.38× (z +9.1) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 4.29 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.64 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 6.93 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.82 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.33 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.62 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.00 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.61 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.71 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 9.44 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.54 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 9.54 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.97 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.08 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.33 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.08 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.90 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.24 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.36 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.63 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.36 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 9.55 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.42 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.07 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.30 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.78 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.15 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 42.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.98 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.27 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.54 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.06 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.88 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.23 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13613), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPATA21]] | +0.76 | +0.64 / +0.72 | both halves | 7e-06 |  |
| [[MROH8]] | +0.73 | +0.66 / +0.72 | both halves | 7e-06 |  |
| [[KIAA2012]] | +0.72 | +0.59 / +0.76 | both halves | 7e-06 |  |
| [[CHMP3-AS1]] | +0.71 | +0.47 / +0.70 | both halves | 2e-05 | same gene group |
| [[SLC27A6]] | +0.71 | +0.52 / +0.72 | both halves | 1e-05 |  |
| [[BTG1-DT]] | +0.71 | +0.55 / +0.76 | both halves | 1e-05 |  |
| [[C2CD5-AS1]] | +0.70 | +0.47 / +0.72 | both halves | 2e-05 | same gene group |
| [[CNTN5]] | +0.70 | +0.58 / +0.72 | both halves | 7e-06 |  |
| [[SEC1P]] | +0.69 | +0.66 / +0.58 | both halves | 7e-06 |  |
| [[GEMIN7-AS1]] | +0.69 | +0.55 / +0.73 | both halves | 1e-05 | same gene group |
| [[HSPA2-AS1]] | +0.69 | +0.56 / +0.67 | both halves | 1e-05 | same gene group |
| [[CTDSPL2-DT]] | +0.69 | +0.60 / +0.62 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SNAP25]] | B | SNAP25 activity raises SNAP25-AS1's level | lines that do not express SNAP25 (26) vs lines expressing it (24) | 2.15× lower at baseline in the lines without SNAP25 | 0.012 | ⚠ within organs, on part of the lines; also absent: EYA4, SPOCK1, DPYSL3 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 021]]; 188 genes; every member is in the + arm (projection on the module's main direction 0.722). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (15.9, 31.0); signed map (37.0, 6.5). **Vector** length 64.8, 10.2% of its response variance represented; |z| ≥ 3 in 855 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +9.2 | +15.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +8.8 | +12.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +8.7 | +15.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +8.2 | +14.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.7 | +9.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.1 | +4.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.7 | +4.5 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.7 | +3.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.4 | +3.5 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.1 | +4.6 |
| fall | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.7 | -0.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.4 | -1.4 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.1 | -2.4 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -2.0 | -0.8 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.9 | -3.9 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.7 | -2.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.7 | -1.2 |
|  | [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | -1.6 | -1.7 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.5 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | SNAP25 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 20p12.2 — chr20:10,006,381-10,368,831 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

**Summary**, from NCBI Gene [100131208](https://www.ncbi.nlm.nih.gov/gene/100131208):

> Predicted to be involved in SRP-dependent cotranslational protein targeting to membrane, signal sequence recognition. Predicted to be part of signal recognition particle, endoplasmic reticulum targeting. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:44312](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:44312) · Entrez [100131208](https://www.ncbi.nlm.nih.gov/gene/100131208) · Ensembl [ENSG00000227906](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000227906)

## Data

Gene col 13613: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13613); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13613, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13613]; `tensor/DDL_lfc|DDL_z.npy` [13613]; `embed/gene_vectors.npy` [13613]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13613 or target_col == 13613). Every well: [[SNAP25-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SNAP25-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
