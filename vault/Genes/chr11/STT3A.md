---
symbol: "STT3A"
type: "gene"
col: 5627
ensembl_id: "ENSG00000134910"
name: "STT3 oligosaccharyltransferase complex catalytic subunit A"
location: "11q24.2"
module: 42
arm: "+"
pooled_cpm: 66.53
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 16
n_dd_up_clean: 2
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/042"]
generated_by: "tahoemap"
---

# STT3A

*STT3 oligosaccharyltransferase complex catalytic subunit A* — 11q24.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (2 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 4.60× (z +10.6, q 2e-23, up in 48 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[TAK-901 (drug)]] 5 µM in 3 lines (PANC-1 6.77×, SW480 5.24×, HEC-1-A 5.34×); [[Dinaciclib (drug)]] 5 µM in 3 lines (SNU-423 3.22×, HS-578T 2.75×, J82 2.74×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (NCI-H23 3.73×, SNU-423 3.22×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.566× (z -10.7, q 7e-24, down in 41 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RPN1]] (+0.80, fdr 7e-06), [[NOMO2]] (+0.79, fdr 7e-06), [[DDOST]] (+0.78, fdr 7e-06); moves opposite to [[ERVK3-1]] (-0.66, fdr 7e-06), [[TOPORS]] (-0.62, fdr 7e-06), [[JMJD1C]] (-0.62, fdr 2e-05).
> It is in [[Module 042]], a single-armed module (UPR ER).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 2 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5627.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[TAK-901 (drug)]] 5 µM in 3 lines (PANC-1 6.77×, SW480 5.24×, HEC-1-A 5.34×); [[Dinaciclib (drug)]] 5 µM in 3 lines (SNU-423 3.22×, HS-578T 2.75×, J82 2.74×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (NCI-H23 3.73×, SNU-423 3.22×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **4.60×** | +10.6 | 2e-23 | 48/49 (PANC-1, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **3.43×** | +8.5 | 5e-15 | 42/48 (HS-578T, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.73×** | +7.0 | 5e-10 | 30/39 (SNU-423, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.51×** | +5.5 | 7e-06 | 35/49 (NCI-H23, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Goserelin (acetate) (drug)]] 5 µM |  | 1.19× | +3.2 | 0.14 | 15/48 (HEC-1-A, A498, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 8 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5627.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.566×** | -10.7 | 7e-24 | 41/48 (RKO, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.513×** | -8.5 | 5e-15 | 38/48 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.683×** | -5.1 | 7e-05 | 29/48 (A-427, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.713×** | -4.5 | 1e-03 | 27/48 (A498, H4, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.735×** | -4.1 | 0.005 | 27/48 (HS-578T, A-172, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~11% of this change | **0.812×** | -3.9 | 0.008 | 26/48 (AsPC-1, A-427, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.748×** | -3.9 | 0.009 | 27/48 (A498, KATO III, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.733×** | -3.8 | 0.009 | 29/47 (AN3 CA, BT-474, …) | all doses, stronger at high dose | low cells (technical?); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **0.821×** | -3.7 | 0.012 | 21/48 (HEC-1-A, A498, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.764×** | -3.6 | 0.019 | 26/48 (A498, H4, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~15% of this change | **0.782×** | -3.3 | 0.054 | 23/48 (A-172, NCI-H2347, …) | all doses, stronger at high dose | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.777×** | -3.2 | 0.059 | 25/47 (SNU-1, SW 900, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~14% of this change | **0.786×** | -3.2 | 0.059 | 26/48 (A498, H4, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.850× | -3.1 | 0.087 | 18/48 (SW1417, SW 900, …) | top dose only |  |
| [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | **0.796×** | -3.0 | 0.088 | 21/48 (RKO, Panc 03.27, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.800×** | -3.0 | 0.098 | 20/48 (HCT15, Hs 766T, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.12 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5627. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 38.9 | 0 | 3 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.328× (z -9.7) ⚠ cell-cycle shift, explains ~15% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.337× (z -9.1) |
| [[A-427 (line)]] | wt | 31.7 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.236× (z -17.0) |
| [[HS-578T (line)]] | alt | 105 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 2.75× (z +9.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.342× (z -14.6) |
| [[PANC-1 (line)]] | alt | 81.8 | 1 | 2 | [[TAK-901 (drug)]] 5 µM 6.77× (z +9.8) | [[Homoharringtonine (drug)]] 5 µM 0.414× (z -12.2) |
| [[A498 (line)]] | wt | 61.8 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.394× (z -10.0) |
| [[AsPC-1 (line)]] | alt | 64.2 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.258× (z -17.7) |
| [[hTERT-HPNE (line)]] | wt | 77.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.227× (z -15.2) |
| [[NCI-H2347 (line)]] | alt | 78.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.328× (z -16.7) |
| [[SNU-423 (line)]] | alt | 44.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.22× (z +9.8) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 59.2 | 0 | 1 | — | [[Harringtonine (drug)]] 0.05 µM 0.0613× (z -13.0) |
| [[CFPAC-1 (line)]] | alt | 77.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.386× (z -13.2) |
| [[H4 (line)]] | wt | 102 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.466× (z -8.5) |
| [[HEC-1-A (line)]] | alt | 67.9 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 5.34× (z +8.6) | — |
| [[HT-29 (line)]] | alt | 91.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.399× (z -10.8) |
| [[J82 (line)]] | alt | 55.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.74× (z +9.0) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 45.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.433× (z -10.1) |
| [[MIA PaCa-2 (line)]] | alt | 58.3 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.285× (z -9.2) |
| [[NCI-H23 (line)]] | alt | 37.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.73× (z +10.4) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 59.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.217× (z -18.4) |
| [[SHP-77 (line)]] | alt | 57.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0823× (z -19.3) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 61.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0602× (z -10.3) |
| [[SW 900 (line)]] | alt | 93.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.438× (z -9.8) |
| [[SW1417 (line)]] | alt | 84.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.482× (z -9.2) |
| [[SW480 (line)]] | alt | 68.9 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 5.24× (z +9.3) | — |
| [[A549 (line)]] | wt | 45.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 31.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 37.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 22.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 61.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 64.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 96.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 54.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 84.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 79.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 131 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 59.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 73.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 117 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 64.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 64.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 51.5 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 42.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 64.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 59.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 54.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 89.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 67.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 87.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 71.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5627), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPN1]] | +0.80 | +0.76 / +0.86 | both halves | 7e-06 | same gene group; pathway: Adherens junctions interactions; STRING 999 |
| [[NOMO2]] | +0.79 | +0.80 / +0.80 | both halves | 7e-06 | pathway: Cotranslational targeting of proteins to the endoplasmic reticulum |
| [[DDOST]] | +0.78 | +0.78 / +0.78 | both halves | 7e-06 | same gene group; pathway: Adherens junctions interactions; STRING 999 |
| [[TSN]] | +0.76 | +0.76 / +0.74 | both halves | 7e-06 |  |
| [[TXNDC5]] | +0.76 | +0.70 / +0.81 | both halves | 7e-06 | STRING 405 |
| [[TMED2]] | +0.76 | +0.74 / +0.75 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation |
| [[PRPF8]] | +0.75 | +0.67 / +0.78 | both halves | 7e-06 |  |
| [[COPG1]] | +0.74 | +0.76 / +0.73 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation; STRING 519 |
| [[SEC61A1]] | +0.74 | +0.81 / +0.68 | both halves | 7e-06 | pathway: Cotranslational targeting of proteins to the endoplasmic reticulum; STRING 993 |
| [[TMED7]] | +0.73 | +0.69 / +0.76 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation |
| [[SSR1]] | +0.72 | +0.71 / +0.66 | both halves | 7e-06 | pathway: Cotranslational targeting of proteins to the endoplasmic reticulum; STRING 940 |
| [[DNAJB11]] | +0.72 | +0.73 / +0.70 | both halves | 7e-06 | pathway: Dengue Virus Genome Translation and Replication; STRING 443 |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ERVK3-1]] | -0.66 | -0.60 / -0.68 | both halves | 7e-06 |  |
| [[TOPORS]] | -0.62 | -0.60 / -0.62 | both halves | 7e-06 |  |
| [[JMJD1C]] | -0.62 | -0.52 / -0.48 | both halves | 2e-05 |  |
| [[EIF1B]] | -0.60 | -0.56 / -0.58 | both halves | 1e-05 |  |
| [[CROCCP2-1]] | -0.60 | -0.58 / -0.64 | both halves | 8e-06 |  |
| [[IER5]] | -0.58 | -0.58 / -0.54 | both halves | 1e-05 |  |
| [[MSX1]] | -0.57 | -0.52 / -0.65 | both halves | 1e-05 |  |
| [[ZNF503]] | -0.56 | -0.52 / -0.62 | both halves | 1e-05 |  |
| [[TUBB4B]] | -0.56 | -0.52 / -0.57 | both halves | 1e-05 | pathway: Asparagine N-linked glycosylation |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 042]] — UPR ER; 103 genes; every member is in the + arm (projection on the module's main direction 0.780). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-23.9, -22.7); signed map (-55.8, 7.0). **Vector** length 133, 41.5% of its response variance represented; |z| ≥ 3 in 863 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *UPR ER* (control, mean cos +0.56 to 11); *ER to Golgi Anterograde Transport* (reactome, mean cos +0.52 to 13); *Transport to the Golgi and subsequent modification* (reactome, mean cos +0.52 to 13).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +9.7 | +7.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +8.8 | +5.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +8.7 | +2.7 |
|  | [[TAK-901 (drug)]] 5 µM |  | +8.7 | +10.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +7.5 | +8.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.5 | +0.3 |
|  | [[Budesonide (drug)]] 5 µM |  | +2.6 | +2.0 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | +2.5 | +2.9 |
|  | [[Goserelin (acetate) (drug)]] 5 µM |  | +2.4 | +3.2 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -6.6 | -10.7 |
|  | [[Harringtonine (drug)]] 5 µM |  | -6.2 | -8.5 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | -5.9 | -3.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.4 | -1.3 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~15% of this change | -3.8 | -3.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.5 | -4.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.8 | -3.8 |
|  | [[Rapamycin (drug)]] 5 µM |  | -2.8 | -2.3 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -2.7 | -2.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.5 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | STT3 oligosaccharyltransferase complex catalytic subunit A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q24.2 — chr11:125,591,712-125,625,215 (+) |
| Ensembl biotype | protein_coding |
| Also known as | TMC, MGC9042, STT3-A; previously ITM1 |
| Gene groups (HGNC) | STT3 oligosaccharyltransferase catalytic subunits; Oligosaccharyltransferase complex subunits |
| Reactome | 26 pathways, smallest: PD-L1(CD274) glycosylation and translocation to plasma membrane; Regulation of CDH1 posttranslational processing and trafficking to plasma membrane; Maturation of spike protein_9694548 |
| Matched by | ensembl_id |

**Function**, from UniProt [P46977](https://www.uniprot.org/uniprotkb/P46977) (Dolichyl-diphosphooligosaccharide--protein glycosyltransferase subunit STT3A):

> Catalytic subunit of the oligosaccharyl transferase (OST) complex that catalyzes the initial transfer of a defined glycan (Glc(3)Man(9)GlcNAc(2) in eukaryotes) from the lipid carrier dolichol-pyrophosphate to an asparagine residue within an Asn-Xaa-Ser/Thr consensus motif in nascent polypeptide chains, the first step in protein N-glycosylation. N-glycosylation occurs cotranslationally and the complex associates with the Sec61 complex at the channel-forming translocon complex that mediates …

**Summary**, from NCBI Gene [3703](https://www.ncbi.nlm.nih.gov/gene/3703):

> The protein encoded by this gene is a catalytic subunit of the N-oligosaccharyltransferase (OST) complex, which functions in the endoplasmic reticulum to transfer glycan chains to asparagine residues of target proteins. A separate complex containing a similar catalytic subunit with an overlapping function also exists. Multiple transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Aug 2015]

**Accessions** — [HGNC:6172](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6172) · Entrez [3703](https://www.ncbi.nlm.nih.gov/gene/3703) · UniProt [P46977](https://www.uniprot.org/uniprotkb/P46977) · Ensembl [ENSG00000134910](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000134910)

## Data

Gene col 5627: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5627); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5627, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5627]; `tensor/DDL_lfc|DDL_z.npy` [5627]; `embed/gene_vectors.npy` [5627]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5627 or target_col == 5627). Every well: [[STT3A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/STT3A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
