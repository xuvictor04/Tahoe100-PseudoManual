---
symbol: "CATSPERD"
type: "gene"
col: 10538
ensembl_id: "ENSG00000174898"
name: "catsper channel auxiliary subunit delta"
location: "19p13.3"
module: 53
arm: "+"
pooled_cpm: 2.43
n_lines_expressing: 50
n_dd_up: 27
n_dd_down: 3
n_dd_up_clean: 18
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/053"]
generated_by: "tahoemap"
---

# CATSPERD

*catsper channel auxiliary subunit delta* — 19p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (9 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 12.1× (z +26.8, q 0e+00, up in 33 of 34 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Radotinib (drug)]] 5 µM: 0.695× (z -4.0, q 0.041, down in 11 of 41 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AXDND1]] (+0.81, fdr 7e-06), [[EPHA1-AS1]] (+0.79, fdr 7e-06), [[IL12RB2]] (+0.79, fdr 7e-06).
> It is in [[Module 053]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 9 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10538.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **12.1×** | +26.8 | 0e+00 | 33/34 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **7.30×** | +21.3 | 0e+00 | 32/32 (A-172, A498, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **7.94×** | +15.1 | 0e+00 | 0/0 | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **5.47×** | +12.9 | 7e-36 | 27/33 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **4.81×** | +11.9 | 1e-30 | 12/14 (HOP62, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.81×** | +11.0 | 3e-26 | 0/1 | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **3.80×** | +10.1 | 3e-22 | 33/45 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **3.19×** | +8.8 | 1e-16 | 26/39 (NCI-H460, SW480, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **2.23×** | +8.6 | 5e-16 | 16/43 (HEC-1-A, PANC-1, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **2.07×** | +7.8 | 4e-13 | 24/43 (KATO III, SW480, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.85×** | +7.6 | 1e-12 | 13/27 (HEC-1-A, SW480, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **2.58×** | +7.2 | 4e-11 | 24/41 (SW480, PANC-1, …) | all doses, stronger at high dose | position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.52×** | +6.7 | 7e-10 | 19/33 (SW480, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~19% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.16×** | +5.6 | 9e-07 | 15/35 (HS-578T, C32, …) | top dose only | cell-cycle shift (explains ~25% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **3.87×** | +5.4 | 3e-06 | 16/35 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **3.81×** | +5.3 | 4e-06 | 11/27 (PANC-1, NCI-H460, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.72×** | +4.1 | 0.001 | 10/39 (SW480, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[EX229 (drug)]] 5 µM |  | **2.62×** | +3.8 | 0.004 | 5/26 (SW480, A549, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Belzutifan (drug)]] 5 µM |  | **2.53×** | +3.7 | 0.007 | 4/16 (SW480, NCI-H460, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10538.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Radotinib (drug)]] 5 µM |  | **0.695×** | -4.0 | 0.041 | 11/41 (RKO, KATO III, …) | top dose only |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.711×** | -3.7 | 0.059 | 13/44 (SNU-423, SW48, …) | rises with dose |  |
| [[Neratinib (drug)]] 5 µM |  | **0.630×** | -3.6 | 0.072 | 10/43 (SW48, SW480, …) | top dose only | position effect removed |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | 0.749× | -3.2 | 0.23 | 6/44 (COLO 205, SW48, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.48 per unit of S-phase module lfc, +0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10538. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 1.23 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 21.6× (z +10.4) | — |
| [[HS-578T (line)]] | alt | 1.67 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 26.5× (z +9.8) | — |
| [[NCI-H460 (line)]] | wt | 1.65 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 43.9× (z +15.5) | — |
| [[C32 (line)]] | wt | 2.21 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 142× (z +13.0) | — |
| [[HEC-1-A (line)]] | alt | 2.96 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 21.6× (z +12.5) | — |
| [[HOP62 (line)]] | alt | 1.30 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 43.7× (z +11.8) | — |
| [[LS 180 (line)]] | wt | 3.43 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 11.9× (z +10.7) | [[olaparib (drug)]] 0.05 µM 0.0391× (z -10.0) ⚠ unreliable plate only |
| [[PANC-1 (line)]] | alt | 2.25 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.60× (z +9.5) | — |
| [[SNU-423 (line)]] | alt | 1.48 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 54.4× (z +11.4) | — |
| [[SW480 (line)]] | alt | 3.82 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.66× (z +10.6) | — |
| [[A-172 (line)]] | wt | 1.23 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 32.1× (z +10.4) | — |
| [[hTERT-HPNE (line)]] | wt | 2.74 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 49.6× (z +11.4) | — |
| [[LoVo (line)]] | wt | 3.08 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 34.0× (z +14.5) | — |
| [[LOX-IMVI (line)]] | wt | 3.49 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 48.0× (z +13.2) | — |
| [[NCI-H1573 (line)]] | alt | 1.75 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 17.3× (z +9.3) | — |
| [[RPMI-7951 (line)]] | alt | 3.40 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 23.5× (z +10.4) | — |
| [[A-427 (line)]] | wt | 2.20 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.65 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.86 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.29 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.69 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.13 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.41 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.14 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.22 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.79 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.63 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.19 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.60 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.87 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.32 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.05 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.21 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.09 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.89 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.28 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.96 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.11 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.21 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.31 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.61 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.14 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.01 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.12 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.24 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.63 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.30 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.59 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.10 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 17.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10538), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AXDND1]] | +0.81 | +0.79 / +0.79 | both halves | 7e-06 |  |
| [[EPHA1-AS1]] | +0.79 | +0.71 / +0.81 | both halves | 7e-06 |  |
| [[IL12RB2]] | +0.79 | +0.78 / +0.79 | both halves | 7e-06 |  |
| [[NUP210L]] | +0.76 | +0.80 / +0.71 | both halves | 7e-06 |  |
| [[GRAMD2A]] | +0.75 | +0.72 / +0.75 | both halves | 7e-06 |  |
| [[SLC8A2]] | +0.74 | +0.79 / +0.63 | both halves | 7e-06 |  |
| [[TMPRSS9]] | +0.74 | +0.83 / +0.76 | both halves | 7e-06 |  |
| [[PPP1R36]] | +0.74 | +0.66 / +0.72 | both halves | 7e-06 |  |
| [[GRIK5]] | +0.74 | +0.78 / +0.65 | both halves | 7e-06 |  |
| [[USP50]] | +0.74 | +0.78 / +0.60 | both halves | 7e-06 |  |
| [[KIF17]] | +0.73 | +0.78 / +0.67 | both halves | 7e-06 |  |
| [[TRIM72]] | +0.73 | +0.75 / +0.65 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers CATSPERD's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.6% of all compounds | 0.041 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[F2]] | B | F2 activity raises CATSPERD's level | lines that do not express F2 (11) vs lines expressing it (39) | 1.29× lower at baseline in the lines without F2 | 0.097 | ⚠ within organs, on part of the lines; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 053]]; 88 genes; every member is in the + arm (projection on the module's main direction 0.868). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (38.8, -14.5); signed map (21.2, 12.3). **Vector** length 65.4, 10.2% of its response variance represented; |z| ≥ 3 in 1,229 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +8.6 | +26.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.4 | +21.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.8 | +15.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | +5.8 | +11.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.7 | +11.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.0 | +8.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.6 | +7.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.1 | +8.6 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +3.3 | +3.5 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.8 | +1.3 |
| fall | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.5 | +0.3 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.4 | -4.0 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.3 | +0.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.0 | +2.6 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.0 | +0.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.7 | -1.5 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.7 | -3.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.6 | -0.1 |

## What is on record

|  |  |
|---|---|
| Name | catsper channel auxiliary subunit delta |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.3 — chr19:5,720,637-5,778,734 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC39581; previously TMEM146 |
| Gene groups (HGNC) | CatSpermasome complex |
| Reactome | 3 pathways, smallest: Sperm Motility And Taxes; Fertilization; Reproduction |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86XM0](https://www.uniprot.org/uniprotkb/Q86XM0) (Cation channel sperm-associated auxiliary subunit delta):

> Auxiliary component of the CatSper complex, a complex involved in sperm cell hyperactivation. Sperm cell hyperactivation is needed for sperm motility which is essential late in the preparation of sperm for fertilization. Required for CATSPER1 stability before intraflagellar transport and/or incorporation of the CatSper complex channel into the flagellar membrane.

**Summary**, from NCBI Gene [257062](https://www.ncbi.nlm.nih.gov/gene/257062):

> Predicted to be involved in flagellated sperm motility and sperm capacitation. Predicted to be located in plasma membrane. Predicted to be part of CatSper complex. Predicted to be active in sperm principal piece. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:28598](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28598) · Entrez [257062](https://www.ncbi.nlm.nih.gov/gene/257062) · UniProt [Q86XM0](https://www.uniprot.org/uniprotkb/Q86XM0) · Ensembl [ENSG00000174898](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000174898)

## Data

Gene col 10538: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10538); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10538, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10538]; `tensor/DDL_lfc|DDL_z.npy` [10538]; `embed/gene_vectors.npy` [10538]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10538 or target_col == 10538). Every well: [[CATSPERD — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CATSPERD.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
