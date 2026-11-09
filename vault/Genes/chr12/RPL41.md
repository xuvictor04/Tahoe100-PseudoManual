---
symbol: "RPL41"
type: "gene"
col: 13691
ensembl_id: "ENSG00000229117"
name: "ribosomal protein L41"
location: "12q13"
module: 21
arm: "+"
pooled_cpm: 41.15
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 1
n_dd_up_clean: 5
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/021"]
generated_by: "tahoemap"
---

# RPL41

*ribosomal protein L41* — 12q13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.77× (z +12.7, q 4e-34, up in 43 of 45 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 3.57× (z +6.4, q 3e-08, up in 47 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Carbidopa (monohydrate) (drug)]] 0.05 µM: 0.513× (z -6.4, q 1e-07, down in 44 of 48 measured lines) ⚠ unreliable plate only; position not correctable.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (A-427 0.365×; ⚠ cell-cycle shift, would explain all of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 9 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMA7]] (+0.70, fdr 1e-05), [[RPL23A]] (+0.67, fdr 7e-06), [[RPL22]] (+0.67, fdr 7e-06); moves opposite to [[HAUS7]] (-0.59, fdr 3e-05), [[NUP62]] (-0.53, fdr 1e-05), [[THUMPD1]] (-0.52, fdr 5e-05).
> It is in [[Module 021]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 7 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13691.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.77×** | +12.7 | 4e-34 | 43/45 (NCI-H1573, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.97×** | +10.0 | 4e-21 | 38/42 (NCI-H1573, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.59×** | +8.4 | 7e-15 | 41/45 (LoVo, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift; position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **3.57×** | +6.4 | 3e-08 | 47/49 (SW480, LS 180, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.90×** | +6.1 | 9e-08 | 43/46 (RPMI-7951, SW 900, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~17% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.55×** | +5.8 | 7e-07 | 33/48 (NCI-H2347, AsPC-1, …) | top dose only | cell-cycle shift (explains ~6% here); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.86×** | +5.7 | 8e-07 | 37/47 (LoVo, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~16% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.82×** | +5.5 | 3e-06 | 33/46 (MIA PaCa-2, HepG2/C3A, …) | inconsistent across doses | cell-cycle shift (explains ~3% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **1.69×** | +5.0 | 3e-05 | 38/47 (NCI-H460, LoVo, …) | rises with dose |  |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.80×** | +4.0 | 0.004 | 34/48 (Panc 03.27, A-427, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.73×** | +3.7 | 0.010 | 35/46 (LoVo, NCI-H2347, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.45×** | +3.4 | 0.030 | 24/48 (RKO, A-172, …) | top dose only | cell-cycle shift (explains ~17% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 2 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13691.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (A-427 0.365×; ⚠ cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.513×** | -6.4 | 1e-07 | 44/48 (PANC-1, LoVo, …) | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.848× | -5.5 | 1e-05 | 20/49 (CFPAC-1, MIA PaCa-2, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 0.05 µM |  | 0.696× | -3.3 | 0.20 | 27/48 (AsPC-1, HT-29, …) | inconsistent across doses | position effect removed |
| [[Balsalazide (sodium hydrate) (drug)]] 5 µM |  | 0.784× | -3.2 | 0.20 | 23/48 (SNU-1, CFPAC-1, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.15 per unit of S-phase module lfc, +0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13691. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 34.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.01× (z +10.4) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 67.2 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.43× (z +11.7) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 52.2 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.31× (z +10.6) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 60.5 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.89× (z +10.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.365× (z -10.2) ⚠ cell-cycle shift, would explain all of this change |
| [[AsPC-1 (line)]] | alt | 46.9 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.55× (z +9.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.31× (z +8.5) | — |
| [[KATO III (line)]] | alt | 29.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.33× (z +10.8) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 45.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.96× (z +9.4) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 43.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.92× (z +11.8) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 35.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.89× (z +10.9) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 56.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.68× (z +10.9) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 20.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.73× (z +8.9) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 50.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.64× (z +9.7) ⚠ toxic; transcription drop | — |
| [[C32 (line)]] | wt | 30.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.18× (z +8.6) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 34.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.57× (z +8.6) ⚠ toxic; transcription drop | — |
| [[H4 (line)]] | wt | 30.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.56× (z +8.6) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 26.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.60× (z +9.1) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 32.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.07× (z +8.8) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 34.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.12× (z +9.1) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 38.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.57× (z +8.5) | — |
| [[Panc 03.27 (line)]] | alt | 51.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.23× (z +9.8) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 56.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.12× (z +9.2) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 34.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 35.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 29.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 52.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 49.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 42.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 68.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 19.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 37.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 26.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 61.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 64.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 39.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 60.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 49.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 47.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 33.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 31.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 39.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 34.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 26.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 30.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 41.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 35.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 46.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13691), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 9 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMA7]] | +0.70 | +0.57 / +0.69 | both halves | 1e-05 | STRING 408 |
| [[RPL23A]] | +0.67 | +0.73 / +0.67 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 704 |
| [[RPL22]] | +0.67 | +0.63 / +0.66 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 597 |
| [[RPL13A]] | +0.66 | +0.69 / +0.66 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 931 |
| [[RPS3A]] | +0.65 | +0.64 / +0.57 | both halves | 9e-06 | pathway: Cap-dependent Translation Initiation; STRING 832 |
| [[C12orf73]] | +0.64 | +0.50 / +0.64 | both halves | 1e-05 |  |
| [[TICAM2-AS1]] | +0.64 | +0.58 / +0.58 | both halves | 7e-06 |  |
| [[RPL21]] ⚠ | +0.64 | +0.66 / +0.64 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 732; ⚠ in the vector space only through flagged drug-doses |
| [[ZBTB47-AS1]] | +0.62 | +0.51 / +0.66 | both halves | 1e-05 |  |
| [[RPS18]] | +0.62 | +0.58 / +0.60 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 743 |
| [[RPS15A]] | +0.61 | +0.65 / +0.66 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 672 |
| [[TNS2-AS1]] | +0.60 | +0.51 / +0.58 | both halves | 1e-05 |  |
| [[RPL29]] | +0.60 | +0.56 / +0.62 | both halves | 1e-05 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 871 |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HAUS7]] | -0.59 | -0.45 / -0.62 | both halves | 3e-05 |  |
| [[NUP62]] | -0.53 | -0.50 / -0.60 | both halves | 1e-05 | pathway: Influenza Infection |
| [[THUMPD1]] | -0.52 | -0.40 / -0.59 | both halves | 5e-05 | pathway: rRNA processing |
| [[THAP5]] | -0.51 | -0.52 / -0.48 | both halves | 2e-05 |  |
| [[SETX]] | -0.51 | -0.36 / -0.55 | both halves | 9e-05 |  |
| [[CIAO1]] | -0.51 | -0.51 / -0.45 | both halves | 3e-05 |  |
| [[UTP11]] | -0.51 | -0.43 / -0.52 | both halves | 3e-05 | pathway: Major pathway of rRNA processing in the nucleolus and cytosol |
| [[ZNF770]] | -0.50 | -0.43 / -0.57 | both halves | 3e-05 |  |
| [[WDR82]] | -0.50 | -0.53 / -0.54 | both halves | 1e-05 |  |
| [[CDKN2AIP]] | -0.49 | -0.37 / -0.48 | both halves | 7e-05 |  |
| [[ASF1A]] | -0.49 | -0.40 / -0.50 | both halves | 4e-05 |  |
| [[UBC]] | -0.49 | -0.43 / -0.43 | both halves | 4e-05 | pathway: Protein localization |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 021]]; 188 genes; every member is in the + arm (projection on the module's main direction 0.516). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-44.6, -30.4); signed map (-62.5, -7.0). **Vector** length 70.0, 16.8% of its response variance represented; |z| ≥ 3 in 629 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +3.6 | +6.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.8 | +3.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.7 | +1.5 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.7 | +2.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.6 | +5.8 |
|  | [[Bimiralisib (drug)]] 0.05 µM |  | +2.0 | +0.4 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.8 | +0.9 |
| fall | [[Auranofin (drug)]] 5 µM |  | -4.0 | +0.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.7 | +0.6 |
|  | [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.5 | -0.9 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -2.4 | -0.6 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.4 | +1.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.2 | +1.0 |
|  | [[Palmatine (chloride) (drug)]] 0.05 µM |  | -1.9 | +0.2 |
|  | [[Thymol (drug)]] 5 µM |  | -1.8 | +2.3 |

## What is on record

|  |  |
|---|---|
| Name | ribosomal protein L41 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q13 — chr12:56,116,590-56,117,967 (+) |
| Ensembl biotype | protein_coding |
| Also known as | L41, eL41 |
| Gene groups (HGNC) | L ribosomal proteins |
| Reactome | 37 pathways, smallest: Peptide chain elongation; PELO:HBS1L and ABCE1 dissociate a ribosome on a non-stop mRNA; Viral mRNA Translation |
| Matched by | ensembl_id |

**Function**, from UniProt [P62945](https://www.uniprot.org/uniprotkb/P62945) (Small ribosomal subunit protein eS32):

> Component of the small ribosomal subunit (Probable). The ribosome is a large ribonucleoprotein complex responsible for the synthesis of proteins in the cell. Interacts with the beta subunit of protein kinase CKII and stimulates phosphorylation of DNA topoisomerase II alpha by CKII.

**Summary**, from NCBI Gene [6171](https://www.ncbi.nlm.nih.gov/gene/6171):

> Enables mRNA 3'-UTR binding activity and mRNA 5'-UTR binding activity. Involved in cytoplasmic translation. Located in endoplasmic reticulum. Part of cytosolic large ribosomal subunit. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:10354](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10354) · Entrez [6171](https://www.ncbi.nlm.nih.gov/gene/6171) · UniProt [P62945](https://www.uniprot.org/uniprotkb/P62945) · Ensembl [ENSG00000229117](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000229117)

## Data

Gene col 13691: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13691); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13691, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13691]; `tensor/DDL_lfc|DDL_z.npy` [13691]; `embed/gene_vectors.npy` [13691]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13691 or target_col == 13691). Every well: [[RPL41 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RPL41.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
