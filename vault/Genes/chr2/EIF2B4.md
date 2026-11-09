---
symbol: "EIF2B4"
type: "gene"
col: 3634
ensembl_id: "ENSG00000115211"
name: "eukaryotic translation initiation factor 2B subunit delta"
location: "2p23.3"
module: 17
arm: "+"
pooled_cpm: 21.9
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 4
n_dd_up_clean: 0
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/017"]
generated_by: "tahoemap"
---

# EIF2B4

*eukaryotic translation initiation factor 2B subunit delta* — 2p23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (3 with an alert ⚠); the strongest is [[Docetaxel (drug)]] 0.05 µM: 1.26× (z +4.6, q 0.002, up in 18 of 44 measured lines) ⚠ transcription drop. None of them is without an alert.
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.917× (z -5.8, q 4e-06, down in 4 of 48 measured lines) ⚠ position not correctable. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.815× (z -5.7, q 4e-06, down in 25 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PWP1]] (+0.67, fdr 7e-06), [[ZYG11B]] (+0.58, fdr 1e-05), [[TSR3]] (+0.58, fdr 1e-05); moves opposite to [[PPP1R15B-AS1]] (-0.56, fdr 2e-05), [[DEPDC4]] (-0.51, fdr 4e-05), [[EPB41L2]] (-0.50, fdr 2e-05).
> It sits in the **+** arm of [[Module 017]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TMTC2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 6 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3634.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.26×** | +4.6 | 0.002 | 18/44 (PANC-1, SK-MEL-2, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~9% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 1.20× | +3.6 | 0.071 | 17/41 (SW480, NCI-H1573, …) | two highest doses | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.20×** | +3.5 | 0.071 | 12/44 (NCI-H2030, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~3% of this change | **1.20×** | +3.5 | 0.071 | 14/46 (MIA PaCa-2, HS-578T, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.13× | +3.3 | 0.085 | 12/48 (A498, LOX-IMVI, …) | top dose only | low cells (technical?) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +3.3 | 0.085 | 10/47 (PANC-1, NCI-H2030, …) | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 3 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3634.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.917× | -5.8 | 4e-06 | 4/48 (CFPAC-1, SK-MEL-2, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.815×** | -5.7 | 4e-06 | 25/47 (SNU-1, RKO, …) | top dose only | cell-cycle shift (explains ~5% here); position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.793×** | -4.6 | 0.001 | 16/48 (CHP-212, CFPAC-1, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.807×** | -4.2 | 0.004 | 18/48 (AsPC-1, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.873× | -3.8 | 0.017 | 21/47 (LOX-IMVI, NCI-H1792, …) | top dose only | composition shift |
| [[Irinotecan (drug)]] 0.5 µM |  | **0.765×** | -3.7 | 0.017 | 5/48 (NCI-H2347, A498, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | 0.875× | -3.7 | 0.018 | 13/48 (SW480, NCI-H1792, …) | two highest doses |  |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 0.837× | -3.5 | 0.037 | 5/47 (SW480, KATO III, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3634. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C-33 A (line)]] | alt | 23.6 | 0 | 2 (1 ⚠) | — | [[Pimozide (drug)]] 0.05 µM 0.148× (z -11.8) |
| [[LOX-IMVI (line)]] | wt | 20.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.426× (z -9.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[RKO (line)]] | wt | 25.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.399× (z -8.5) |
| [[SNU-1 (line)]] | wt | 22.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.164× (z -12.8) |
| [[SW1417 (line)]] | alt | 28.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.286× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 22.9 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 30.3 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 27.8 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 29.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 16.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 17.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 15.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 27.4 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 18.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 23.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 14.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 21.5 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 43.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 20.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 32.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 26.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 30.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 26.9 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 24.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3634), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PWP1]] | +0.67 | +0.64 / +0.61 | both halves | 7e-06 |  |
| [[ZYG11B]] | +0.58 | +0.49 / +0.50 | both halves | 1e-05 |  |
| [[TSR3]] | +0.58 | +0.49 / +0.50 | both halves | 1e-05 |  |
| [[ABCF3]] | +0.57 | +0.54 / +0.53 | both halves | 1e-05 |  |
| [[HARS2]] | +0.57 | +0.48 / +0.59 | both halves | 2e-05 | STRING 400 |
| [[CIAO3]] | +0.56 | +0.47 / +0.56 | both halves | 2e-05 |  |
| [[RNF20]] | +0.55 | +0.49 / +0.46 | both halves | 3e-05 |  |
| [[LRRC47]] | +0.53 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[PLD2]] | +0.53 | +0.46 / +0.49 | both halves | 3e-05 |  |
| [[BRMS1]] | +0.53 | +0.46 / +0.55 | both halves | 2e-05 |  |
| [[SHARPIN]] | +0.53 | +0.45 / +0.50 | both halves | 3e-05 |  |
| [[FIP1L1]] | +0.52 | +0.56 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPP1R15B-AS1]] | -0.56 | -0.55 / -0.46 | both halves | 2e-05 |  |
| [[DEPDC4]] | -0.51 | -0.51 / -0.42 | both halves | 4e-05 |  |
| [[EPB41L2]] | -0.50 | -0.47 / -0.51 | both halves | 2e-05 |  |
| [[MYH15]] | -0.48 | -0.38 / -0.50 | both halves | 6e-05 |  |
| [[TMTC2]] | -0.48 | -0.53 / -0.43 | both halves | 3e-05 |  |
| [[FAM81A]] | -0.48 | -0.52 / -0.40 | both halves | 5e-05 |  |
| [[CA8]] | -0.48 | -0.44 / -0.47 | both halves | 3e-05 |  |
| [[KCNQ1]] | -0.48 | -0.51 / -0.44 | both halves | 3e-05 |  |
| [[ARL5B]] | -0.47 | -0.50 / -0.40 | both halves | 5e-05 |  |
| [[SLIT2]] | -0.47 | -0.42 / -0.42 | both halves | 4e-05 |  |
| [[B4GALT6]] | -0.47 | -0.49 / -0.40 | both halves | 5e-05 |  |
| [[LINC01088]] | -0.47 | -0.44 / -0.37 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TMTC2]] | B | TMTC2 activity lowers EIF2B4's level | lines that do not express TMTC2 (6) vs lines expressing it (44) | 1.23× higher at baseline in the lines without TMTC2 | 0.048 | ⚠ within organs, on part of the lines; also absent: RNF125, GPR19; maybe low, not absent |
| [[STRA6LP]] | B | STRA6LP activity lowers EIF2B4's level | lines that do not express STRA6LP (9) vs lines expressing it (41) | 1.15× higher at baseline in the lines without STRA6LP | 0.074 | ⚠ within organs, on part of the lines; co-absent genes; also absent: CCDC180 |
| [[EPB41L2]] | B | EPB41L2 activity raises EIF2B4's level | lines that do not express EPB41L2 (6) vs lines expressing it (44) | 1.18× lower at baseline in the lines without EPB41L2 | 0.084 | ⚠ within organs, on part of the lines; also absent: SLC26A2, CRTAP, FAM216A; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 017]] — Intraflagellar transport; 202 genes; this gene is in the **+** arm (projection on the module's main direction 0.494). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-32.0, -3.1); signed map (-20.6, -13.4). **Vector** length 70.8, 12.2% of its response variance represented; |z| ≥ 3 in 683 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~3% of this change | +2.3 | +3.5 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +2.0 | +4.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +2.0 | +3.3 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +1.8 | +3.3 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.7 | +2.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.7 | +2.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.7 | +2.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.6 | +2.7 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.4 | +1.3 |
|  | [[Betamethasone dipropionate (drug)]] 0.5 µM |  | +1.3 | +2.4 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -4.6 | -5.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -3.4 | -4.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.1 | -3.7 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -2.7 | -3.8 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -2.6 | -1.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.6 | -2.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.3 | -1.3 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.5 | -1.6 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.4 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | eukaryotic translation initiation factor 2B subunit delta |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p23.3 — chr2:27,364,352-27,370,338 (-) |
| Ensembl biotype | protein_coding |
| Also known as | EIF2Bdelta, EIF-2B, DKFZP586J0119, EIF2B |
| Reactome | 4 pathways, smallest: Recycling of eIF2:GDP; Cap-dependent Translation Initiation; Eukaryotic Translation Initiation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UI10](https://www.uniprot.org/uniprotkb/Q9UI10) (Translation initiation factor eIF2B subunit delta):

> Acts as a component of the translation initiation factor 2B (eIF2B) complex, which catalyzes the exchange of GDP for GTP on eukaryotic initiation factor 2 (eIF2) gamma subunit. Its guanine nucleotide exchange factor activity is repressed when bound to eIF2 complex phosphorylated on the alpha subunit, thereby limiting the amount of methionyl-initiator methionine tRNA available to the ribosome and consequently global translation is repressed.

**Summary**, from NCBI Gene [8890](https://www.ncbi.nlm.nih.gov/gene/8890):

> Eukaryotic initiation factor 2B (EIF2B), which is necessary for protein synthesis, is a GTP exchange factor composed of five different subunits. The protein encoded by this gene is the fourth, or delta, subunit. Defects in this gene are a cause of leukoencephalopathy with vanishing white matter (VWM) and ovarioleukodystrophy. Multiple transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:3260](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3260) · Entrez [8890](https://www.ncbi.nlm.nih.gov/gene/8890) · UniProt [Q9UI10](https://www.uniprot.org/uniprotkb/Q9UI10) · Ensembl [ENSG00000115211](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000115211)

## Data

Gene col 3634: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3634); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3634, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3634]; `tensor/DDL_lfc|DDL_z.npy` [3634]; `embed/gene_vectors.npy` [3634]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3634 or target_col == 3634). Every well: [[EIF2B4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EIF2B4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
