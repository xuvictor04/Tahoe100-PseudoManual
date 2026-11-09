---
symbol: "POLR2G"
type: "gene"
col: 9577
ensembl_id: "ENSG00000168002"
name: "RNA polymerase II subunit G"
location: "11q12.3"
module: 58
arm: "+"
pooled_cpm: 14.52
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 0
n_dd_up_clean: 0
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/058", "evidence-flagged-only"]
generated_by: "tahoemap"
---

# POLR2G

*RNA polymerase II subunit G* — 11q12.3

## At a glance

> [!summary] In this data
> ⚠ It is in the vector space only through drug-doses that carry an alert for it (its significant pooled drug-doses and per-line responses; `embed/genes.parquet` evidence_flagged_only): its vector, partners and module rest on changes that may come from what those drug-doses did to the cells rather than from its own regulation.
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.75× (z +11.6, q 1e-28, up in 38 of 39 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 8 lines (NCI-H1573 12.0×, HEC-1-A 7.04×, SW480 4.15×, NCI-H460 5.51×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change); [[Panobinostat (drug)]] 5 µM in 1 line (SW480 3.74×; ⚠ cell-cycle shift, explains ~46% of this change).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (A-427 0.202×).
> Its strongest partners by |cos| (93 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 14 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PSENEN]] (+0.63, fdr 1e-05), [[ATF7]] (+0.62, fdr 4e-05), [[TMED1]] (+0.62, fdr 1e-05); moves opposite to [[LINC00592]] (-0.50, fdr 1e-04), [[KCND3]] (-0.48, fdr 2e-04), [[BCL2]] (-0.48, fdr 4e-04).
> It is in [[Module 058]], a single-armed module (oxidative phosphorylation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 11 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9577.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 8 lines (NCI-H1573 12.0×, HEC-1-A 7.04×, SW480 4.15×, NCI-H460 5.51×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change); [[Panobinostat (drug)]] 5 µM in 1 line (SW480 3.74×; ⚠ cell-cycle shift, explains ~46% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **3.75×** | +11.6 | 1e-28 | 38/39 (NCI-H1573, HEC-1-A, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **3.37×** | +9.2 | 8e-18 | 24/25 (KATO III, SW480, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **2.37×** | +7.0 | 4e-10 | 26/32 (HOP62, LOX-IMVI, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **2.10×** | +6.5 | 9e-09 | 41/48 (SW480, KATO III, …) | rises with dose | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **2.06×** | +6.4 | 2e-08 | 39/48 (SW480, KATO III, …) | rises with dose | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~48% of this change | **1.66×** | +4.4 | 8e-04 | 27/43 (RPMI-7951, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.68×** | +3.9 | 0.007 | 23/42 (HT-29, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~78% of this change | **1.55×** | +3.8 | 0.009 | 23/46 (SW480, KATO III, …) | top dose only | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~78% of this change | **1.54×** | +3.8 | 0.011 | 24/47 (SW480, KATO III, …) | top dose only |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **1.31×** | +3.3 | 0.052 | 22/48 (SW480, A-172, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.43×** | +3.1 | 0.095 | 14/46 (LS 180, NCI-H1573, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9577.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (A-427 0.202×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Hydroxyurea (drug)]] 5 µM |  | 0.658× | -3.2 | 0.43 | 14/47 (H4, PANC-1, …) | rises with dose | position effect removed |
| [[TAK-901 (drug)]] 0.05 µM |  | 0.686× | -3.2 | 0.43 | 20/47 (NCI-H2347, C32, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.47 per unit of S-phase module lfc, +0.35 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9577. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 19.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.15× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[A-427 (line)]] | wt | 23.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.202× (z -13.3) |
| [[A498 (line)]] | wt | 10.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.66× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[A549 (line)]] | wt | 14.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.79× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[HEC-1-A (line)]] | alt | 12.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.04× (z +10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[HT-29 (line)]] | alt | 17.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.37× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[NCI-H1573 (line)]] | alt | 10.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 12.0× (z +11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[NCI-H460 (line)]] | wt | 10.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.51× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[PANC-1 (line)]] | alt | 22.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.80× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[A-172 (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 9.70 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 8.30 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 13.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 9.49 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 12.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 8.83 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 15.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 13.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 6.91 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 9.68 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.38 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 19.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.81 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.28 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 12.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9577), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 14 of them with an alert (⚠; 7 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PSENEN]] | +0.63 | +0.63 / +0.57 | both halves | 1e-05 |  |
| [[ATF7]] | +0.62 | +0.54 / +0.41 | both halves | 4e-05 |  |
| [[TMED1]] | +0.62 | +0.63 / +0.57 | both halves | 1e-05 |  |
| [[DDT]] | +0.61 | +0.44 / +0.59 | both halves | 3e-05 |  |
| [[AKR7A2]] | +0.61 | +0.41 / +0.61 | both halves | 4e-05 |  |
| [[NDUFS7]] | +0.58 | +0.37 / +0.59 | both halves | 8e-05 |  |
| [[C19orf53]] | +0.57 | +0.37 / +0.60 | both halves | 8e-05 |  |
| [[NDUFA3]] | +0.57 | +0.30 / +0.65 | both halves | 2e-04 |  |
| [[NUDT16L1]] | +0.56 | +0.35 / +0.66 | both halves | 1e-04 |  |
| [[POLR2J]] ⚠ | +0.55 | +0.34 / +0.61 | both halves | 1e-04 | same gene group; pathway: HALLMARK_DNA_REPAIR; STRING 999; ⚠ in the vector space only through flagged drug-doses |
| [[COPS9]] | +0.55 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[SNAP29]] | +0.54 | +0.50 / +0.47 | both halves | 2e-05 |  |
| [[ETFB]] | +0.54 | +0.29 / +0.61 | both halves | 2e-04 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC00592]] | -0.50 | -0.39 / -0.33 | both halves | 1e-04 |  |
| [[KCND3]] | -0.48 | -0.41 / -0.30 | both halves | 2e-04 |  |
| [[BCL2]] | -0.48 | -0.38 / -0.26 | both halves | 4e-04 | pathway: ESR-mediated signaling |
| [[FSCN2]] | -0.48 | -0.35 / -0.39 | both halves | 1e-04 |  |
| [[LINC01355]] | -0.47 | -0.28 / -0.41 | both halves | 3e-04 |  |
| [[KCNQ4]] | -0.47 | -0.46 / -0.25 | both halves | 4e-04 |  |
| [[DGUOK-AS1]] | -0.46 | -0.33 / -0.24 | both halves | 5e-04 |  |
| [[BTBD16]] | -0.46 | -0.36 / -0.24 | both halves | 4e-04 |  |
| [[OTUD4]] | -0.46 | -0.42 / -0.24 | both halves | 4e-04 |  |
| [[CFAP161]] | -0.46 | -0.37 / -0.30 | both halves | 2e-04 |  |
| [[BEND3]] | -0.45 | -0.40 / -0.32 | both halves | 2e-04 |  |
| [[ELF4]] | -0.45 | -0.38 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 058]] — oxidative phosphorylation; 80 genes; every member is in the + arm (projection on the module's main direction 0.557). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- ⚠ **In the space only through flagged drug-doses**: its significant pooled drug-doses and per-line responses all carry an alert (`embed/genes.parquet` evidence_flagged_only), so its module and partners may reflect what those drug-doses did to the cells.
- **Nodal map** (x, y) = (-50.5, -21.9); signed map (-38.2, 10.7). **Vector** length 49.7, 9.13% of its response variance represented; |z| ≥ 3 in 532 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | +3.1 | +6.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.9 | +1.7 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | +2.8 | +6.5 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~78% of this change | +2.5 | +3.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.5 | +1.4 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.5 | +2.0 |
|  | [[Arbutin (drug)]] 5 µM |  | +1.2 | +2.5 |
|  | [[Artesunate (drug)]] 0.5 µM |  | +1.0 | -0.5 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +1.0 | +1.0 |
|  | [[Sinomenine (drug)]] 0.5 µM |  | +0.9 | +0.7 |
| fall | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.6 | -1.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.6 | -1.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.5 | +0.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -2.4 | -2.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.2 | +1.6 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -1.5 | -0.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.4 | -1.4 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.4 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | RNA polymerase II subunit G |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q12.3 — chr11:62,761,565-62,766,710 (+) |
| Ensembl biotype | protein_coding |
| Also known as | hRPB19, hsRPB7, RPB7 |
| Gene groups (HGNC) | RNA polymerase subunits |
| Hallmark sets | DNA_REPAIR |
| Reactome | 75 pathways, smallest: Signaling by FGFR2 IIIa TM; PIWI-interacting RNA (piRNA) biogenesis; Abortive elongation of HIV-1 transcript in the absence of Tat |
| Matched by | ensembl_id |

**Function**, from UniProt [P62487](https://www.uniprot.org/uniprotkb/P62487) (DNA-directed RNA polymerase II subunit RPB7):

> Core component of RNA polymerase II (Pol II), a DNA-dependent RNA polymerase which synthesizes mRNA precursors and many functional non-coding RNAs using the four ribonucleoside triphosphates as substrates. Pol II is the central component of the basal RNA polymerase II transcription machinery. It is composed of mobile elements that move relative to each other. POLR2G/RPB7 is part of a subcomplex with POLR2D/RPB4 that binds to a pocket formed by POLR2A/RPB1, POLR2B/RPB2 and POLR2F/RPABC2 at the …

**Summary**, from NCBI Gene [5436](https://www.ncbi.nlm.nih.gov/gene/5436):

> This gene encodes the seventh largest subunit of RNA polymerase II, the polymerase responsible for synthesizing messenger RNA in eukaryotes. The protein functions in transcription initiation, and is also thought to help stabilize transcribing polyermase molecules during elongation. [provided by RefSeq, Jan 2009]

**Accessions** — [HGNC:9194](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9194) · Entrez [5436](https://www.ncbi.nlm.nih.gov/gene/5436) · UniProt [P62487](https://www.uniprot.org/uniprotkb/P62487) · Ensembl [ENSG00000168002](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000168002)

## Data

Gene col 9577: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9577); `tables/drug_effects.parquet` (13 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9577, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9577]; `tensor/DDL_lfc|DDL_z.npy` [9577]; `embed/gene_vectors.npy` [9577]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9577 or target_col == 9577). Every well: [[POLR2G — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/POLR2G.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
