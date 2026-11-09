---
symbol: "OSTC"
type: "gene"
col: 12710
ensembl_id: "ENSG00000198856"
name: "oligosaccharyltransferase complex non-catalytic subunit"
location: "4q25"
module: 49
arm: "+"
pooled_cpm: 66.18
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 18
n_dd_up_clean: 1
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/049"]
generated_by: "tahoemap"
---

# OSTC

*oligosaccharyltransferase complex non-catalytic subunit* — 4q25

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.46× (z +5.6, q 1e-05, up in 27 of 42 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Betamethasone dipropionate (drug)]] 5 µM: 1.25× (z +3.4, q 0.082, up in 21 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 1 line (J82 3.15×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 1 line (A-427 2.88×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.527× (z -11.7, q 8e-29, down in 43 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMEM39A]] (+0.82, fdr 7e-06), [[SLC33A1]] (+0.82, fdr 7e-06), [[SEC61A1]] (+0.77, fdr 7e-06).
> It is in [[Module 049]], a single-armed module (XBP1(S) activates chaperone genes).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 4 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12710.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 1 line (J82 3.15×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 1 line (A-427 2.88×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.46×** | +5.6 | 1e-05 | 27/42 (J82, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.56×** | +5.4 | 2e-05 | 29/48 (A-427, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.31×** | +4.0 | 0.011 | 25/47 (HepG2/C3A, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.31×** | +3.8 | 0.018 | 23/45 (J82, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **1.25×** | +3.4 | 0.082 | 21/48 (HOP62, H4, …) | top dose only | position effect removed |
| [[Fluvoxamine (maleate) (drug)]] 0.5 µM |  | 1.22× | +3.1 | 0.17 | 19/48 (NCI-H460, NCI-H2347, …) | two highest doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 7 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12710.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.527×** | -11.7 | 8e-29 | 43/48 (A498, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **0.577×** | -8.2 | 9e-14 | 39/48 (A498, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.656×** | -6.5 | 2e-08 | 31/48 (A498, H4, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.704×** | -5.4 | 9e-06 | 30/48 (A498, KATO III, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.708×** | -5.3 | 1e-05 | 30/48 (A498, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[DTP3 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.731×** | -4.8 | 1e-04 | 40/48 (SW480, A498, …) | inconsistent across doses | position effect removed |
| [[Drospirenone (drug)]] 5 µM |  | **0.762×** | -4.2 | 0.002 | 32/48 (SW480, NCI-H1792, …) | top dose only | position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.774×** | -3.9 | 0.005 | 24/48 (A498, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.774×** | -3.9 | 0.005 | 27/48 (A498, CFPAC-1, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.811×** | -3.9 | 0.006 | 26/48 (HS-578T, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.816×** | -3.7 | 0.010 | 20/48 (CHP-212, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.784×** | -3.5 | 0.019 | 22/47 (A-172, HOP62, …) | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | **0.657×** | -3.4 | 0.031 | 19/49 (A498, HOP62, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.798×** | -3.3 | 0.033 | 22/48 (H4, Hs 766T, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.831×** | -3.3 | 0.035 | 18/49 (NCI-H1573, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | **0.820×** | -3.0 | 0.078 | 17/48 (LoVo, HEC-1-A, …) | inconsistent across doses |  |
| [[Fumaric acid (drug)]] 0.5 µM |  | **0.778×** | -3.0 | 0.085 | 12/48 (SW480, AN3 CA, …) | rises with dose | noisy plate (z scaled); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.22 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12710. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 74.8 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.317× (z -15.1) |
| [[A498 (line)]] | wt | 127 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.275× (z -21.4) |
| [[SW 1088 (line)]] | alt | 143 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.0970× (z -12.4) |
| [[HS-578T (line)]] | alt | 81.6 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.342× (z -11.2) |
| [[NCI-H2347 (line)]] | alt | 89.3 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.356× (z -15.8) |
| [[J82 (line)]] | alt | 48.8 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.15× (z +11.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.437× (z -9.9) |
| [[A-427 (line)]] | wt | 58.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.88× (z +8.6) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 55.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.428× (z -9.6) |
| [[AN3 CA (line)]] | alt | 49.8 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.124× (z -10.0) |
| [[AsPC-1 (line)]] | alt | 48.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.420× (z -9.6) |
| [[CFPAC-1 (line)]] | alt | 75.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.304× (z -13.7) |
| [[H4 (line)]] | wt | 126 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.286× (z -12.7) |
| [[HOP62 (line)]] | alt | 92.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.321× (z -16.0) |
| [[Hs 766T (line)]] | wt | 79.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.402× (z -9.8) |
| [[hTERT-HPNE (line)]] | wt | 95.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.342× (z -11.6) |
| [[LoVo (line)]] | wt | 82.3 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.392× (z -8.6) |
| [[MIA PaCa-2 (line)]] | alt | 43.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.209× (z -9.8) |
| [[NCI-H1573 (line)]] | alt | 116 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.501× (z -8.5) ⚠ cell-cycle shift, explains ~29% of this change |
| [[NCI-H1792 (line)]] | alt | 81.4 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 5 µM 0.0709× (z -12.7) ⚠ toxic; cell-cycle shift, explains ~19% of this change |
| [[SW 900 (line)]] | alt | 63.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.418× (z -9.6) |
| [[BT-474 (line)]] | alt | 40.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 52.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 39.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 75.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 68.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 70.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 61.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 63.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 73.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 90.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 34.6 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 92.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 54.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 58.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 47.5 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 59.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 69.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 51.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 51.9 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 40.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 66.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 84.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 36.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 53.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 55.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 30.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 40.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 44.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 66.3 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 40.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12710), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM39A]] | +0.82 | +0.83 / +0.79 | both halves | 7e-06 | **novel candidate** |
| [[SLC33A1]] | +0.82 | +0.74 / +0.84 | both halves | 7e-06 | **novel candidate** |
| [[SEC61A1]] | +0.77 | +0.82 / +0.72 | both halves | 7e-06 | pathway: Cotranslational targeting of proteins to the endoplasmic reticulum; STRING 934 |
| [[COG3]] | +0.77 | +0.80 / +0.74 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation |
| [[NFXL1]] | +0.76 | +0.78 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[COG6]] | +0.76 | +0.80 / +0.71 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation |
| [[SEC23A]] | +0.76 | +0.74 / +0.74 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation |
| [[PDIA5]] | +0.76 | +0.82 / +0.70 | both halves | 7e-06 |  |
| [[KDELR2]] | +0.75 | +0.80 / +0.71 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation |
| [[GOLT1B]] | +0.75 | +0.85 / +0.66 | both halves | 7e-06 |  |
| [[DNAJC25]] | +0.75 | +0.73 / +0.72 | both halves | 7e-06 |  |
| [[MCEE]] | +0.74 | +0.73 / +0.71 | both halves | 7e-06 | pathway: HALLMARK_FATTY_ACID_METABOLISM |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 049]] — XBP1(S) activates chaperone genes; 93 genes; every member is in the + arm (projection on the module's main direction 0.829). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.12; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (13.8, -34.7); signed map (-52.9, 10.9). **Vector** length 116, 35.5% of its response variance represented; |z| ≥ 3 in 764 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *XBP1(S) activates chaperone genes* (reactome, mean cos +0.57 to 8); *IRE1alpha activates chaperones* (reactome, mean cos +0.57 to 8); *Unfolded Protein Response (UPR)* (reactome, mean cos +0.57 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.7 | +4.0 |
|  | [[Terfenadine (drug)]] 5 µM |  | +2.7 | +2.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.7 | +5.6 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.7 | +2.3 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +2.5 | +2.7 |
|  | [[Pasireotide (acetate) (drug)]] 5 µM |  | +2.3 | +2.3 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.3 | +0.3 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -4.8 | -8.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -3.6 | -11.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.6 | -2.3 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.5 | -1.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.5 | -2.5 |
|  | [[Busulfan (drug)]] 0.05 µM |  | -3.1 | -2.3 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -3.1 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | oligosaccharyltransferase complex non-catalytic subunit |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q25 — chr4:108,650,585-108,667,820 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DC2 |
| Gene groups (HGNC) | Oligosaccharyltransferase complex subunits |
| Hallmark sets | FATTY_ACID_METABOLISM |
| Reactome | 26 pathways, smallest: PD-L1(CD274) glycosylation and translocation to plasma membrane; Regulation of CDH1 posttranslational processing and trafficking to plasma membrane; Maturation of spike protein_9694548 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NRP0](https://www.uniprot.org/uniprotkb/Q9NRP0) (Oligosaccharyltransferase complex subunit OSTC):

> Subunit of STT3A-containing oligosaccharyl transferase (OST-A) complex that catalyzes the initial transfer of a defined glycan (Glc(3)Man(9)GlcNAc(2) in eukaryotes) from the lipid carrier dolichol-pyrophosphate to an asparagine residue within an Asn-Xaa-Ser/Thr consensus motif in nascent polypeptide chains, the first step in protein N-glycosylation. N-glycosylation occurs cotranslationally and the complex associates with the Sec61 complex at the channel-forming translocon complex that mediates …

**Summary**, from NCBI Gene [58505](https://www.ncbi.nlm.nih.gov/gene/58505):

> Enables protein-macromolecule adaptor activity. Involved in protein N-linked glycosylation. Located in endoplasmic reticulum membrane. Part of oligosaccharyltransferase complex A. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:24448](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24448) · Entrez [58505](https://www.ncbi.nlm.nih.gov/gene/58505) · UniProt [Q9NRP0](https://www.uniprot.org/uniprotkb/Q9NRP0) · Ensembl [ENSG00000198856](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198856)

## Data

Gene col 12710: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12710); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12710, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12710]; `tensor/DDL_lfc|DDL_z.npy` [12710]; `embed/gene_vectors.npy` [12710]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12710 or target_col == 12710). Every well: [[OSTC — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/OSTC.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
