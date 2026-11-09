---
symbol: "UBFD1"
type: "gene"
col: 2358
ensembl_id: "ENSG00000103353"
name: "ubiquitin family domain containing 1"
location: "16p12.2"
module: 25
arm: "+"
pooled_cpm: 37.44
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 9
n_dd_up_clean: 6
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/025"]
generated_by: "tahoemap"
---

# UBFD1

*ubiquitin family domain containing 1* — 16p12.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (4 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 2.15× (z +14.3, q 1e-43, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.760× (z -7.2, q 3e-10, down in 30 of 47 measured lines) ⚠ cell-cycle shift, explains ~22% of this change. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 0.814× (z -5.4, q 2e-05, down in 27 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BABAM1]] (+0.70, fdr 7e-06), [[AHSA1]] (+0.67, fdr 7e-06), [[GPN1]] (+0.65, fdr 7e-06); moves opposite to [[EID2]] (-0.58, fdr 7e-06), [[METTL23]] (-0.58, fdr 9e-06), [[PPP1R35]] (-0.57, fdr 2e-05, ⚠ PPP1R35 in the vector space only through flagged drug-doses), [[TGIF2]] (-0.56, fdr 1e-05).
> It sits in the **+** arm of [[Module 025]] (oxidative phosphorylation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[PSMB5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 6 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2358.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.15×** | +14.3 | 1e-43 | 46/48 (NCI-H1573, PANC-1, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.98×** | +12.8 | 6e-35 | 46/48 (NCI-H1573, PANC-1, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.90×** | +11.3 | 2e-27 | 45/48 (PANC-1, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~7% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.57×** | +8.4 | 7e-15 | 37/48 (HT-29, C32, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.46×** | +6.8 | 1e-09 | 23/39 (PANC-1, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.36×** | +5.8 | 7e-07 | 26/46 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.46×** | +5.1 | 3e-05 | 25/48 (NCI-H1792, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.31×** | +5.1 | 3e-05 | 26/48 (SW480, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.65×** | +4.9 | 5e-05 | 25/44 (PANC-1, SW480, …) | all doses, flat | cell-cycle shift (explains ~8% here); noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.23×** | +3.6 | 0.022 | 20/44 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | 1.14× | +3.5 | 0.028 | 14/48 (J82, HT-29, …) | top dose only | low cells (technical?) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +3.0 | 0.11 | 13/48 (SW480, PANC-1, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 7 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2358.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **0.760×** | -7.2 | 3e-10 | 30/47 (HS-578T, RKO, …) | inconsistent across doses | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.814×** | -5.4 | 2e-05 | 27/48 (KATO III, SW1417, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.759×** | -5.1 | 5e-05 | 26/48 (NCI-H2347, HS-578T, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.769×** | -4.9 | 1e-04 | 22/48 (NCI-H460, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **0.766×** | -4.8 | 2e-04 | 23/48 (RKO, SNU-423, …) | top dose only | composition shift |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.802×** | -4.1 | 0.004 | 21/48 (AsPC-1, HOP62, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~14% of this change | **0.818×** | -3.7 | 0.015 | 18/48 (SW480, A549, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~13% of this change | 0.837× | -3.3 | 0.066 | 10/48 (NCI-H2347, A-427, …) | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.951× | -3.3 | 0.068 | 1/48 (NCI-H23) | inconsistent across doses |  |
| [[venetoclax (drug)]] 5 µM |  | **0.718×** | -3.2 | 0.069 | 16/47 (HT-29, SK-MEL-2, …) | top dose only | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.5 µM |  | **0.789×** | -3.1 | 0.083 | 11/48 (SK-MEL-2, C-33 A, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | 0.845× | -3.1 | 0.083 | 16/48 (SW 900, H4, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2358. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 42.7 | 3 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.47× (z +11.0) | — |
| [[SW480 (line)]] | alt | 37.7 | 3 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.49× (z +10.5) | — |
| [[C32 (line)]] | wt | 24.2 | 2 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.30× (z +8.9) | — |
| [[NCI-H1573 (line)]] | alt | 37.4 | 2 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.11× (z +11.9) | — |
| [[C-33 A (line)]] | alt | 45.4 | 0 | 1 (1 ⚠) | — | [[Simotinib (drug)]] 5 µM 0.294× (z -8.8) ⚠ toxic |
| [[COLO 205 (line)]] | alt | 24.3 | 0 | 1 | — | [[Vilanterol (drug)]] 0.5 µM 0.170× (z -10.2) |
| [[HEC-1-A (line)]] | alt | 36.4 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.63× (z +8.8) | — |
| [[HS-578T (line)]] | alt | 41.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.389× (z -11.5) ⚠ cell-cycle shift, explains ~22% of this change |
| [[HT-29 (line)]] | alt | 24.9 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.42× (z +9.2) | — |
| [[LoVo (line)]] | wt | 32.5 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.42× (z +8.6) | — |
| [[LOX-IMVI (line)]] | wt | 36.6 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.07× (z +10.2) | — |
| [[RKO (line)]] | wt | 41.5 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.349× (z -8.6) ⚠ cell-cycle shift, explains ~22% of this change |
| [[SNU-1 (line)]] | wt | 46.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.109× (z -13.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW48 (line)]] | wt | 35.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.196× (z -9.1) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 53.8 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 37.4 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 59.2 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 47.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 39.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 33.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 32.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 41.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 50.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 56.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 55.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 55.9 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 33.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 36.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 43.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 31.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 35.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 27.3 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 35.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 36.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 43.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 37.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 29.6 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 30.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 34.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 34.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 40.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 36.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 37.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 52.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 29.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 30.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 31.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2358), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BABAM1]] | +0.70 | +0.76 / +0.60 | both halves | 7e-06 |  |
| [[AHSA1]] | +0.67 | +0.69 / +0.61 | both halves | 7e-06 |  |
| [[GPN1]] | +0.65 | +0.63 / +0.63 | both halves | 7e-06 |  |
| [[GDAP2]] | +0.64 | +0.72 / +0.60 | both halves | 7e-06 |  |
| [[TIMM10B]] | +0.63 | +0.65 / +0.59 | both halves | 7e-06 |  |
| [[SERPINH1]] | +0.63 | +0.63 / +0.60 | both halves | 7e-06 |  |
| [[SUDS3]] | +0.62 | +0.61 / +0.67 | both halves | 7e-06 |  |
| [[UFD1]] | +0.62 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[USP5]] | +0.62 | +0.64 / +0.60 | both halves | 7e-06 |  |
| [[NAXD]] | +0.62 | +0.59 / +0.62 | both halves | 7e-06 |  |
| [[CLNS1A]] | +0.62 | +0.49 / +0.58 | both halves | 1e-05 |  |
| [[NUCB1]] | +0.61 | +0.54 / +0.66 | both halves | 1e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EID2]] | -0.58 | -0.60 / -0.62 | both halves | 7e-06 |  |
| [[METTL23]] | -0.58 | -0.57 / -0.60 | both halves | 9e-06 |  |
| [[PPP1R35]] ⚠ | -0.57 | -0.47 / -0.58 | both halves | 2e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[TGIF2]] | -0.56 | -0.64 / -0.51 | both halves | 1e-05 |  |
| [[PRPF38B]] | -0.56 | -0.53 / -0.57 | both halves | 1e-05 |  |
| [[FOXA2]] | -0.55 | -0.44 / -0.62 | both halves | 3e-05 |  |
| [[PPP4R2]] | -0.55 | -0.40 / -0.56 | both halves | 5e-05 |  |
| [[PFN1]] | -0.54 | -0.57 / -0.42 | both halves | 4e-05 |  |
| [[POGZ]] | -0.54 | -0.54 / -0.46 | both halves | 3e-05 |  |
| [[ANKRD12]] | -0.54 | -0.55 / -0.48 | both halves | 2e-05 |  |
| [[NBPF19]] | -0.53 | -0.51 / -0.49 | both halves | 1e-05 |  |
| [[PHACTR4]] | -0.53 | -0.47 / -0.59 | both halves | 2e-05 |  |
| [[NBPF14]] | -0.53 | -0.47 / -0.49 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSMB5]] | B | PSMB5 activity lowers UBFD1's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[TXNIP]] | B | TXNIP activity lowers UBFD1's level | lines that do not express TXNIP (11) vs lines expressing it (39) | 1.10× higher at baseline in the lines without TXNIP | 0.071 | ⚠ within organs, on part of the lines; also absent: FAM3B, CADPS2, PLAC4; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 025]] — oxidative phosphorylation; 171 genes; this gene is in the **+** arm (projection on the module's main direction 0.461). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-22.3, -13.0); signed map (-28.9, -28.7). **Vector** length 102, 23.7% of its response variance represented; |z| ≥ 3 in 864 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM |  | +8.7 | +14.3 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +8.4 | +11.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +7.8 | +12.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.6 | +8.4 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | +4.2 | +4.9 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +3.2 | +5.1 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +2.0 | +2.9 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | +1.7 | +1.6 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | -5.8 | -4.8 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | -5.5 | -7.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.4 | -5.4 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -3.5 | +1.3 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.4 | -1.3 |
|  | [[EX229 (drug)]] 5 µM |  | -3.0 | -2.7 |
|  | [[venetoclax (drug)]] 5 µM |  | -2.8 | -3.2 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.6 | -2.3 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -2.3 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | ubiquitin family domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p12.2 — chr16:23,557,721-23,574,389 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ42145, FLJ38870, UBPH |
| Matched by | ensembl_id |

**Function**, from UniProt [O14562](https://www.uniprot.org/uniprotkb/O14562) (Ubiquitin domain-containing protein UBFD1):

> May play a role as NF-kappa-B regulator.

**Summary**, from NCBI Gene [56061](https://www.ncbi.nlm.nih.gov/gene/56061):

> Enables RNA binding activity and cadherin binding activity. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:30565](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30565) · Entrez [56061](https://www.ncbi.nlm.nih.gov/gene/56061) · UniProt [O14562](https://www.uniprot.org/uniprotkb/O14562) · Ensembl [ENSG00000103353](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000103353)

## Data

Gene col 2358: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2358); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2358, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2358]; `tensor/DDL_lfc|DDL_z.npy` [2358]; `embed/gene_vectors.npy` [2358]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2358 or target_col == 2358). Every well: [[UBFD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UBFD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
