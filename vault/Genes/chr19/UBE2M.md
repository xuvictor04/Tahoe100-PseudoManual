---
symbol: "UBE2M"
type: "gene"
col: 5108
ensembl_id: "ENSG00000130725"
name: "ubiquitin conjugating enzyme E2 M"
location: "19q13.43"
module: 72
arm: "+"
pooled_cpm: 42.41
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 3
n_dd_up_clean: 3
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/072"]
generated_by: "tahoemap"
---

# UBE2M

*ubiquitin conjugating enzyme E2 M* — 19q13.43

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.00× (z +10.7, q 9e-24, up in 44 of 45 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 0.5 µM: 1.57× (z +4.4, q 0.001, up in 34 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.628× (z -6.4, q 8e-08, down in 39 of 47 measured lines).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RAB5IF]] (+0.73, fdr 7e-06), [[PSMB3]] (+0.62, fdr 2e-05), [[NEDD8]] (+0.61, fdr 1e-05); moves opposite to [[CYP2U1]] (-0.59, fdr 1e-05), [[YWHAE]] (-0.57, fdr 2e-05), [[MBLAC2]] (-0.56, fdr 2e-05).
> It is in [[Module 072]], a single-armed module (Degradation of DVL).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 7 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5108.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **3.00×** | +10.7 | 9e-24 | 44/45 (A549, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **2.81×** | +9.7 | 1e-19 | 37/39 (SW480, HEC-1-A, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~30% of this change | **1.87×** | +6.1 | 2e-07 | 44/47 (J82, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **1.70×** | +5.1 | 4e-05 | 38/47 (PANC-1, NCI-H2030, …) | rises with dose | position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **1.89×** | +4.9 | 9e-05 | 29/42 (SW480, A549, …) | all doses, stronger at high dose | composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.57×** | +4.4 | 0.001 | 34/48 (PANC-1, HT-29, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.58×** | +4.3 | 0.002 | 33/46 (RKO, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~6% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.51×** | +4.0 | 0.004 | 33/48 (PANC-1, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.46×** | +3.7 | 0.015 | 32/48 (C32, A-427, …) | top dose only | position effect removed |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | 1.26× | +3.1 | 0.10 | 26/48 (LOX-IMVI, SHP-77, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5108.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.628×** | -6.4 | 8e-08 | 39/47 (RKO, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.647×** | -4.3 | 0.006 | 32/47 (HS-578T, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.765×** | -3.7 | 0.041 | 27/48 (KATO III, SW 900, …) | rises with dose |  |
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.712× | -3.3 | 0.13 | 27/48 (SW 900, A498, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | 0.463× | -3.0 | 0.26 | 26/48 (SW 900, LoVo, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.26 per unit of S-phase module lfc, +0.31 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5108. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 33.0 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.49× (z +11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | [[Homoharringtonine (drug)]] 5 µM 0.408× (z -9.5) |
| [[A549 (line)]] | wt | 39.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.47× (z +11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[HEC-1-A (line)]] | alt | 50.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.85× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[HOP62 (line)]] | alt | 22.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.84× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[HS-578T (line)]] | alt | 46.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.58× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[PANC-1 (line)]] | alt | 58.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.22× (z +11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[SW480 (line)]] | alt | 48.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.95× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[C32 (line)]] | wt | 23.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.87× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[J82 (line)]] | alt | 30.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.30× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[KATO III (line)]] | alt | 52.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.71× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[LOX-IMVI (line)]] | wt | 34.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.71× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[NCI-H2030 (line)]] | alt | 59.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.389× (z -9.6) |
| [[NCI-H23 (line)]] | alt | 38.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.92× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[RKO (line)]] | wt | 43.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.294× (z -11.1) |
| [[A-172 (line)]] | wt | 50.8 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 53.8 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 75.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 33.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 36.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 68.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 31.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 56.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 44.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 23.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 31.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 65.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 46.5 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 40.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 45.5 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 36.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 37.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 33.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 32.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 37.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 28.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 34.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 55.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 43.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 38.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 23.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 46.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 49.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 60.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 42.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5108), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*71 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RAB5IF]] | +0.73 | +0.71 / +0.65 | both halves | 7e-06 |  |
| [[PSMB3]] | +0.62 | +0.67 / +0.46 | both halves | 2e-05 | pathway: Antigen processing: Ubiquitination & Proteasome degradation |
| [[NEDD8]] | +0.61 | +0.61 / +0.50 | both halves | 1e-05 | pathway: Neddylation; STRING 999 |
| [[TUSC2]] | +0.60 | +0.64 / +0.55 | both halves | 1e-05 |  |
| [[MBOAT7]] | +0.59 | +0.68 / +0.47 | both halves | 2e-05 |  |
| [[TMEM259]] | +0.58 | +0.61 / +0.41 | both halves | 4e-05 |  |
| [[UFD1]] | +0.57 | +0.66 / +0.43 | both halves | 4e-05 | pathway: Neddylation |
| [[MED31]] | +0.56 | +0.54 / +0.48 | both halves | 2e-05 |  |
| [[BABAM1]] | +0.56 | +0.58 / +0.50 | both halves | 1e-05 |  |
| [[RAD9A]] | +0.55 | +0.51 / +0.45 | both halves | 3e-05 |  |
| [[TANGO2]] | +0.55 | +0.51 / +0.56 | both halves | 1e-05 |  |
| [[FBXW11]] | +0.55 | +0.64 / +0.46 | both halves | 2e-05 | pathway: Antigen processing: Ubiquitination & Proteasome degradation; STRING 650 |

## Genes that move opposite

*29 of its nearest partners move opposite, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CYP2U1]] | -0.59 | -0.60 / -0.56 | both halves | 1e-05 |  |
| [[YWHAE]] | -0.57 | -0.48 / -0.54 | both halves | 2e-05 |  |
| [[MBLAC2]] | -0.56 | -0.55 / -0.47 | both halves | 2e-05 |  |
| [[CEP63]] | -0.55 | -0.62 / -0.40 | both halves | 5e-05 |  |
| [[SLC35A5]] | -0.54 | -0.52 / -0.40 | both halves | 5e-05 |  |
| [[ZBED9]] | -0.53 | -0.55 / -0.36 | both halves | 1e-04 |  |
| [[BHLHE41]] | -0.53 | -0.52 / -0.42 | both halves | 4e-05 |  |
| [[SRSF3]] | -0.53 | -0.52 / -0.41 | both halves | 4e-05 |  |
| [[COQ5]] | -0.52 | -0.60 / -0.26 | both halves | 3e-04 |  |
| [[F8]] | -0.52 | -0.61 / -0.28 | both halves | 3e-04 |  |
| [[ZNF620]] | -0.51 | -0.54 / -0.38 | both halves | 6e-05 |  |
| [[CGGBP1]] | -0.51 | -0.61 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 072]] — Degradation of DVL; 69 genes; every member is in the + arm (projection on the module's main direction 0.547). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-14.2, -7.7); signed map (-40.8, 6.2). **Vector** length 58.7, 15.0% of its response variance represented; |z| ≥ 3 in 620 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM |  | +4.3 | +4.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.0 | +4.4 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +3.6 | +2.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.5 | +3.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.4 | +2.7 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.4 | +0.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.1 | +3.7 |
|  | [[Belinostat (drug)]] 0.05 µM |  | +1.1 | +1.1 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.0 | +0.9 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -5.2 | -6.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.4 | -4.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.8 | -3.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | -2.4 | +4.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.3 | -2.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.8 | +0.6 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.5 | -0.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.4 | -3.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.0 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | ubiquitin conjugating enzyme E2 M |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.43 — chr19:58,555,712-58,558,954 (-) |
| Ensembl biotype | protein_coding |
| Also known as | hUbc12, UBC12 |
| Gene groups (HGNC) | Ubiquitin conjugating enzymes E2 |
| Reactome | 14 pathways, smallest: NIK-->noncanonical NF-kB signaling; Dectin-1 mediated noncanonical NF-kB signaling; TGF-beta receptor signaling activates SMADs |
| Matched by | ensembl_id |

**Function**, from UniProt [P61081](https://www.uniprot.org/uniprotkb/P61081) (NEDD8-conjugating enzyme Ubc12):

> Accepts the ubiquitin-like protein NEDD8 from the UBA3-NAE1 E1 complex and catalyzes its covalent attachment to other proteins. The specific interaction with the E3 ubiquitin ligase RBX1, but not RBX2, suggests that the RBX1-UBE2M complex neddylates specific target proteins, such as CUL1, CUL2, CUL3 and CUL4. Involved in cell proliferation.

**Summary**, from NCBI Gene [9040](https://www.ncbi.nlm.nih.gov/gene/9040):

> The modification of proteins with ubiquitin is an important cellular mechanism for targeting abnormal or short-lived proteins for degradation. Ubiquitination involves at least three classes of enzymes: ubiquitin-activating enzymes, or E1s, ubiquitin-conjugating enzymes, or E2s, and ubiquitin-protein ligases, or E3s. This gene encodes a member of the E2 ubiquitin-conjugating enzyme family. The encoded protein is linked with a ubiquitin-like protein, NEDD8, which can be conjugated to cellular …

**Accessions** — [HGNC:12491](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12491) · Entrez [9040](https://www.ncbi.nlm.nih.gov/gene/9040) · UniProt [P61081](https://www.uniprot.org/uniprotkb/P61081) · Ensembl [ENSG00000130725](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000130725)

## Data

Gene col 5108: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5108); `tables/drug_effects.parquet` (15 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5108, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5108]; `tensor/DDL_lfc|DDL_z.npy` [5108]; `embed/gene_vectors.npy` [5108]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5108 or target_col == 5108). Every well: [[UBE2M — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UBE2M.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
