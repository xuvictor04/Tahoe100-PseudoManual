---
symbol: "DNPEP"
type: "gene"
col: 4470
ensembl_id: "ENSG00000123992"
name: "aspartyl aminopeptidase"
location: "2q35"
module: 32
arm: "+"
pooled_cpm: 33.78
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 4
n_dd_up_clean: 10
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/032"]
generated_by: "tahoemap"
---

# DNPEP

*aspartyl aminopeptidase* — 2q35

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.58× (z +7.8, q 3e-12, up in 23 of 35 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 1.50× (z +7.1, q 3e-10, up in 29 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.654× (z -10.6, q 1e-23, down in 32 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DGLUCY]] (+0.57, fdr 4e-05), [[APOL2]] (+0.52, fdr 2e-05), [[NMI]] (+0.52, fdr 2e-05); moves opposite to [[GTF2IP7]] (-0.43, fdr 1e-04), [[POGLUT2]] (-0.42, fdr 5e-05), [[CCN2]] (-0.41, fdr 1e-04).
> It is in [[Module 032]], a single-armed module (interferon alpha response).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[SLC2A6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 4 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4470.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.58×** | +7.8 | 3e-12 | 23/35 (LoVo, PANC-1, …) | rises with dose | cell-cycle shift (explains ~6% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.50×** | +7.1 | 3e-10 | 29/48 (PANC-1, HS-578T, …) | inconsistent across doses | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.43×** | +6.3 | 4e-08 | 25/47 (PANC-1, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~3% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.43×** | +6.3 | 4e-08 | 32/48 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.38×** | +5.8 | 9e-07 | 31/48 (MIA PaCa-2, A-172, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.37×** | +5.6 | 2e-06 | 26/46 (KATO III, SW480, …) | rises with dose | cell-cycle shift (explains ~10% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.25×** | +5.6 | 2e-06 | 25/48 (NCI-H460, A549, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.28×** | +4.4 | 8e-04 | 20/48 (NCI-H460, HOP62, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.33×** | +4.4 | 8e-04 | 22/48 (NCI-H460, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.27×** | +4.2 | 0.001 | 22/46 (NCI-H460, BT-474, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.52×** | +4.1 | 0.002 | 14/48 (PANC-1, LOX-IMVI, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~12% of this change | **1.22×** | +3.5 | 0.022 | 17/48 (NCI-H460, BT-474, …) | top dose only | composition shift |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.41×** | +3.4 | 0.028 | 9/46 (SNU-1, NCI-H460, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.38×** | +3.2 | 0.062 | 11/47 (MIA PaCa-2, Hs 766T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4470.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.654×** | -10.6 | 1e-23 | 32/47 (SW480, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.487×** | -6.7 | 7e-09 | 32/48 (C32, A498, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.797×** | -5.7 | 2e-06 | 26/48 (MIA PaCa-2, RKO, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.726×** | -5.7 | 2e-06 | 32/48 (HCT15, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, +0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4470. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 34.4 | 3 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.98× (z +10.8) ⚠ cell-cycle shift, explains ~12% of this change | — |
| [[C-33 A (line)]] | alt | 35.3 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.271× (z -9.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.416× (z -9.3) |
| [[NCI-H23 (line)]] | alt | 42.9 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.184× (z -13.3) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.380× (z -10.7) |
| [[SW480 (line)]] | alt | 33.0 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.20× (z +8.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.410× (z -13.7) |
| [[A-172 (line)]] | wt | 59.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.391× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[BT-474 (line)]] | alt | 28.0 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.234× (z -9.2) ⚠ toxic; cell-cycle shift, explains ~36% of this change |
| [[C32 (line)]] | wt | 46.2 | 0 | 1 | — | [[TAK-901 (drug)]] 5 µM 0.138× (z -8.6) |
| [[CHP-212 (line)]] | wt | 47.8 | 0 | 1 | — | [[Tucatinib (drug)]] 0.05 µM 0.109× (z -8.5) |
| [[COLO 205 (line)]] | alt | 22.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.263× (z -9.7) |
| [[HCT15 (line)]] | alt | 44.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.280× (z -9.1) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 48.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.417× (z -11.3) |
| [[HT-29 (line)]] | alt | 34.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.471× (z -9.4) |
| [[hTERT-HPNE (line)]] | wt | 30.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.346× (z -9.6) |
| [[KATO III (line)]] | alt | 23.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.33× (z +10.1) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 34.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.93× (z +9.2) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 26.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.380× (z -11.1) |
| [[LS 180 (line)]] | wt | 30.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.15× (z +8.6) ⚠ toxic; transcription drop | — |
| [[SNU-1 (line)]] | wt | 42.6 | 0 | 1 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.378× (z -8.9) |
| [[SW1417 (line)]] | alt | 43.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.484× (z -9.5) |
| [[SW48 (line)]] | wt | 30.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.298× (z -8.6) |
| [[A-427 (line)]] | wt | 26.1 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 39.7 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 31.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 37.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 28.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 49.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 34.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 32.9 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 33.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 27.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 43.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 31.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 34.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 30.2 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 30.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 40.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 53.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 42.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 47.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 47.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 28.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 25.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4470), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DGLUCY]] | +0.57 | +0.42 / +0.66 | both halves | 4e-05 |  |
| [[APOL2]] | +0.52 | +0.48 / +0.51 | both halves | 2e-05 |  |
| [[NMI]] | +0.52 | +0.47 / +0.59 | both halves | 2e-05 |  |
| [[IFI35]] | +0.52 | +0.48 / +0.53 | both halves | 2e-05 |  |
| [[UBE2Z]] | +0.52 | +0.50 / +0.46 | both halves | 3e-05 |  |
| [[PSMB10]] | +0.51 | +0.39 / +0.63 | both halves | 6e-05 |  |
| [[ZFYVE26]] | +0.50 | +0.46 / +0.50 | both halves | 3e-05 |  |
| [[OGFR]] | +0.50 | +0.49 / +0.51 | both halves | 1e-05 |  |
| [[PARP14]] | +0.49 | +0.45 / +0.54 | both halves | 3e-05 |  |
| [[IFI16]] | +0.49 | +0.41 / +0.52 | both halves | 4e-05 |  |
| [[RNF213]] | +0.48 | +0.46 / +0.51 | both halves | 2e-05 |  |
| [[SAMD9L]] | +0.48 | +0.43 / +0.51 | both halves | 3e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GTF2IP7]] | -0.43 | -0.42 / -0.35 | both halves | 1e-04 |  |
| [[POGLUT2]] | -0.42 | -0.44 / -0.39 | both halves | 5e-05 |  |
| [[CCN2]] | -0.41 | -0.35 / -0.36 | both halves | 1e-04 |  |
| [[GOLIM4]] | -0.41 | -0.33 / -0.44 | both halves | 1e-04 |  |
| [[ANKRD44]] | -0.40 | -0.22 / -0.51 | both halves | 6e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC2A6]] | B | SLC2A6 activity raises DNPEP's level | lines that do not express SLC2A6 (6) vs lines expressing it (44) | 1.13× lower at baseline in the lines without SLC2A6 | 0.075 | ⚠ within organs, on part of the lines; also absent: GFOD1, SOAT1, RGS9; maybe low, not absent |
| [[GTF2IP7]] | B | GTF2IP7 activity lowers DNPEP's level | lines that do not express GTF2IP7 (18) vs lines expressing it (32) | 1.12× higher at baseline in the lines without GTF2IP7 | 0.079 | ⚠ within organs, on part of the lines; also absent: ENSG00000290729, FRMD4B, TMEM92 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 032]] — interferon alpha response; 139 genes; every member is in the + arm (projection on the module's main direction 0.458). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (44.0, 54.3); signed map (60.3, 33.3). **Vector** length 91.9, 20.7% of its response variance represented; |z| ≥ 3 in 766 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM |  | +5.8 | +6.3 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +5.3 | +7.1 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +4.9 | +4.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.5 | +4.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.4 | +5.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.4 | +2.4 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | +2.4 | +4.1 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.2 | +1.4 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -4.1 | -5.7 |
|  | [[TAK-901 (drug)]] 5 µM |  | -4.0 | -6.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -3.4 | -5.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -2.8 | -10.6 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -2.3 | -1.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.0 | -2.6 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.6 | -1.7 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -1.6 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | aspartyl aminopeptidase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q35 — chr2:219,372,043-219,400,022 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DAP, ASPEP |
| Gene groups (HGNC) | Aminopeptidases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9ULA0](https://www.uniprot.org/uniprotkb/Q9ULA0) (Aspartyl aminopeptidase):

> Aminopeptidase with specificity towards an acidic amino acid at the N-terminus. Likely to play an important role in intracellular protein and peptide metabolism.

**Summary**, from NCBI Gene [23549](https://www.ncbi.nlm.nih.gov/gene/23549):

> The protein encoded by this gene is an aminopeptidase which prefers acidic amino acids, and specifically favors aspartic acid over glutamic acid. It is thought to be a cytosolic protein involved in general metabolism of intracellular proteins. Several transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Jan 2016]

**Accessions** — [HGNC:2981](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2981) · Entrez [23549](https://www.ncbi.nlm.nih.gov/gene/23549) · UniProt [Q9ULA0](https://www.uniprot.org/uniprotkb/Q9ULA0) · Ensembl [ENSG00000123992](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000123992)

## Data

Gene col 4470: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4470); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4470, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4470]; `tensor/DDL_lfc|DDL_z.npy` [4470]; `embed/gene_vectors.npy` [4470]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4470 or target_col == 4470). Every well: [[DNPEP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DNPEP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
