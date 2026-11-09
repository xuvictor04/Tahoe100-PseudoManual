---
symbol: "LDAF1"
type: "gene"
col: 248
ensembl_id: "ENSG00000011638"
name: "lipid droplet assembly factor 1"
location: "16p12.3"
module: 24
arm: "+"
pooled_cpm: 37.75
n_lines_expressing: 49
n_dd_up: 13
n_dd_down: 8
n_dd_up_clean: 11
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/024"]
generated_by: "tahoemap"
---

# LDAF1

*lipid droplet assembly factor 1* — 16p12.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (2 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 1.84× (z +7.4, q 9e-11, up in 36 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (2 with an alert ⚠); the strongest is [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM: 0.710× (z -5.9, q 2e-06, down in 33 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CAMLG]] (+0.68, fdr 7e-06), [[SNHG7]] (+0.67, fdr 1e-05), [[EPB41L4A-AS1]] (+0.64, fdr 1e-05); moves opposite to [[SMC1A]] (-0.59, fdr 1e-05), [[SYNCRIP]] (-0.58, fdr 3e-05), [[NUP188]] (-0.57, fdr 3e-05).
> It sits in the **+** arm of [[Module 024]] (Aerobic respiration and respiratory electron transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ATP6V0D2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 3 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 248.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.84×** | +7.4 | 9e-11 | 36/47 (HT-29, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.73×** | +6.6 | 8e-09 | 34/47 (HT-29, LS 180, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.73×** | +6.2 | 8e-08 | 36/47 (HT-29, LS 180, …) | all doses, flat | cell-cycle shift (explains ~3% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.66×** | +6.1 | 1e-07 | 35/47 (C32, A498, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.67×** | +5.9 | 3e-07 | 32/45 (NCI-H2030, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.55×** | +5.3 | 1e-05 | 33/47 (PANC-1, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.35×** | +5.1 | 2e-05 | 32/47 (A-172, MIA PaCa-2, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~6% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.00×** | +4.4 | 8e-04 | 25/41 (HT-29, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.11× | +4.3 | 0.001 | 3/48 (NCI-H2030, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.05 µM |  | **1.40×** | +4.1 | 0.003 | 27/47 (PANC-1, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.25×** | +3.7 | 0.010 | 23/48 (CFPAC-1, KATO III, …) | rises with dose |  |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.35×** | +3.6 | 0.014 | 25/47 (NCI-H460, C-33 A, …) | top dose only |  |
| [[Radotinib (drug)]] 5 µM |  | **1.24×** | +3.6 | 0.014 | 21/47 (AsPC-1, RKO, …) | rises with dose |  |
| [[Mebendazole (drug)]] 5 µM |  | **1.32×** | +3.2 | 0.051 | 20/47 (SNU-423, Hs 766T, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 248.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.710×** | -5.9 | 2e-06 | 33/47 (SW1417, RKO, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.764×** | -4.7 | 6e-04 | 27/46 (LS 180, NCI-H460, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.481×** | -4.7 | 6e-04 | 27/46 (KATO III, NCI-H2347, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.786×** | -4.2 | 0.004 | 23/47 (KATO III, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.707×** | -4.0 | 0.007 | 26/46 (NCI-H2347, Panc 03.27, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.738×** | -3.7 | 0.019 | 23/47 (SW48, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **0.740×** | -3.7 | 0.019 | 25/47 (SW480, A549, …) | rises with dose | composition shift; position effect removed |
| [[PH-797804 (drug)]] 0.05 µM |  | **0.757×** | -3.2 | 0.094 | 15/47 (HS-578T, CFPAC-1, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.29 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 248. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 33.8 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.64× (z +15.4) | [[Dinaciclib (drug)]] 0.05 µM 0.211× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HT-29 (line)]] | alt | 46.0 | 3 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.26× (z +10.5) | — |
| [[SW480 (line)]] | alt | 11.3 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 4.82× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.258× (z -8.7) ⚠ cell-cycle shift, explains ~21% of this change |
| [[A498 (line)]] | wt | 76.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.15× (z +9.9) | — |
| [[CFPAC-1 (line)]] | alt | 73.3 | 1 | 0 | [[Vinblastine (sulfate) (drug)]] 5 µM 2.05× (z +8.8) | — |
| [[HepG2_C3A (line)]] | wt | 11.0 | 0 | 1 | — | [[Ponatinib (drug)]] 5 µM 0.0544× (z -11.6) |
| [[KATO III (line)]] | alt | 39.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.384× (z -10.7) |
| [[LS 180 (line)]] | wt | 52.2 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.467× (z -9.5) ⚠ cell-cycle shift, explains ~25% of this change |
| [[NCI-H460 (line)]] | wt | 24.7 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.450× (z -8.9) ⚠ cell-cycle shift, explains ~25% of this change |
| [[RPMI-7951 (line)]] | alt | 45.3 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.372× (z -8.6) ⚠ cell-cycle shift, explains ~25% of this change |
| [[A-427 (line)]] | wt | 16.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 41.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 51.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 69.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 40.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 14.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 13.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 30.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 21.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 33.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 71.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 35.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 48.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 34.1 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 36.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 6.94 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 9.56 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 117 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 51.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 43.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 46.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 58.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 40.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 41.4 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 45.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 34.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 19.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 50.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 53.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 55.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 50.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 248), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 5 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CAMLG]] | +0.68 | +0.61 / +0.68 | both halves | 7e-06 |  |
| [[SNHG7]] | +0.67 | +0.57 / +0.64 | both halves | 1e-05 |  |
| [[EPB41L4A-AS1]] | +0.64 | +0.57 / +0.60 | both halves | 1e-05 |  |
| [[BEX2]] | +0.63 | +0.52 / +0.66 | both halves | 1e-05 |  |
| [[WDFY1]] | +0.62 | +0.61 / +0.57 | both halves | 1e-05 |  |
| [[NSA2]] | +0.62 | +0.51 / +0.62 | both halves | 1e-05 |  |
| [[OCIAD2]] | +0.61 | +0.50 / +0.63 | both halves | 1e-05 |  |
| [[ATP6V0D2]] | +0.61 | +0.55 / +0.62 | both halves | 1e-05 |  |
| [[UBE2B]] | +0.60 | +0.49 / +0.64 | both halves | 1e-05 |  |
| [[CSTB]] | +0.60 | +0.52 / +0.59 | both halves | 1e-05 |  |
| [[MED10]] | +0.59 | +0.40 / +0.64 | both halves | 5e-05 |  |
| [[RAB11FIP1]] | +0.59 | +0.57 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMC1A]] | -0.59 | -0.56 / -0.57 | both halves | 1e-05 |  |
| [[SYNCRIP]] | -0.58 | -0.43 / -0.64 | both halves | 3e-05 |  |
| [[NUP188]] | -0.57 | -0.45 / -0.61 | both halves | 3e-05 |  |
| [[NCBP1]] | -0.55 | -0.49 / -0.61 | both halves | 1e-05 |  |
| [[PTBP1]] | -0.55 | -0.44 / -0.58 | both halves | 3e-05 |  |
| [[HNRNPAB]] | -0.54 | -0.48 / -0.55 | both halves | 2e-05 |  |
| [[HNRNPL]] | -0.54 | -0.44 / -0.55 | both halves | 3e-05 |  |
| [[HNRNPUL1]] | -0.54 | -0.36 / -0.54 | both halves | 9e-05 |  |
| [[DNMT1]] | -0.53 | -0.53 / -0.56 | both halves | 1e-05 |  |
| [[SNRPB]] | -0.53 | -0.58 / -0.43 | both halves | 3e-05 |  |
| [[CLPTM1L]] | -0.53 | -0.47 / -0.48 | both halves | 2e-05 |  |
| [[MBD3]] | -0.52 | -0.54 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ATP6V0D2]] | B | ATP6V0D2 activity raises LDAF1's level | lines that do not express ATP6V0D2 (18) vs lines expressing it (32) | 1.31× lower at baseline in the lines without ATP6V0D2 | 0.083 | ⚠ within organs, on part of the lines; co-occurs with SETD1B, KMT2D, ARID1A; also absent: GBP5, NALCN, IGFBP7; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 024]] — Aerobic respiration and respiratory electron transport; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.491). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-40.2, -27.8); signed map (-21.1, 14.3). **Vector** length 125, 35.4% of its response variance represented; |z| ≥ 3 in 978 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +8.2 | +5.1 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +7.2 | +6.2 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +7.0 | +5.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +6.8 | +7.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +5.9 | +6.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.1 | +6.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +4.9 | +3.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.4 | +1.3 |
|  | [[Radotinib (drug)]] 5 µM |  | +4.1 | +3.6 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.3 | -2.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | -5.0 | -3.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.9 | -4.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.4 | -5.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.4 | -2.9 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -3.7 | -4.0 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -2.6 | -2.3 |
|  | [[Busulfan (drug)]] 0.05 µM |  | -2.5 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | lipid droplet assembly factor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p12.3 — chr16:21,158,377-21,180,616 (+) |
| Ensembl biotype | protein_coding |
| Also known as | promethin; previously TMEM159 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96B96](https://www.uniprot.org/uniprotkb/Q96B96) (Lipid droplet assembly factor 1):

> Plays an important role in the formation of lipid droplets during the differentiation and maturation of adipocytes. Together with seipin (BSCL2), defines the sites of lipid droplet formation in the endoplasmic reticulum and promotes the aggregation of triacylglycerol molecules to form the core of a lipid droplet (nucleation) in the endoplasmic reticulum and drive budding of lipid droplets into the cytoplasm.

**Summary**, from NCBI Gene [57146](https://www.ncbi.nlm.nih.gov/gene/57146):

> Involved in lipid droplet formation. Located in endoplasmic reticulum membrane and lipid droplet. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:30136](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30136) · Entrez [57146](https://www.ncbi.nlm.nih.gov/gene/57146) · UniProt [Q96B96](https://www.uniprot.org/uniprotkb/Q96B96) · Ensembl [ENSG00000011638](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000011638)

## Data

Gene col 248: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 248); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 248, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 248]; `tensor/DDL_lfc|DDL_z.npy` [248]; `embed/gene_vectors.npy` [248]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 248 or target_col == 248). Every well: [[LDAF1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LDAF1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
