---
symbol: "LSS"
type: "gene"
col: 8332
ensembl_id: "ENSG00000160285"
name: "lanosterol synthase"
location: "21q22.3"
module: 86
arm: "+"
pooled_cpm: 34.17
n_lines_expressing: 50
n_dd_up: 34
n_dd_down: 6
n_dd_up_clean: 33
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/086"]
generated_by: "tahoemap"
---

# LSS

*lanosterol synthase* — 21q22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 34 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.96× (z +12.1, q 5e-31, up in 36 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 0.5 µM: 0.682× (z -4.9, q 5e-04, down in 22 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SREBF2]] (+0.65, fdr 1e-05), [[MVD]] (+0.65, fdr 7e-06), [[INSIG1]] (+0.64, fdr 1e-05); moves opposite to [[ALG8]] (-0.46, fdr 5e-05), [[SRBD1]] (-0.45, fdr 1e-04), [[LINC00467]] (-0.45, fdr 5e-05).
> It is in [[Module 086]], a single-armed module (cholesterol synthesis).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 1 with an alert ⚠; shown: the 15 strongest. 34 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8332.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.96×** | +12.1 | 5e-31 | 36/48 (A-172, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Cepharanthine (drug)]] 5 µM |  | **1.91×** | +11.6 | 8e-29 | 43/48 (LoVo, LS 180, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM |  | **2.40×** | +11.2 | 1e-26 | 43/48 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Berbamine (drug)]] 5 µM |  | **1.65×** | +9.1 | 2e-17 | 42/49 (LoVo, LS 180, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.03×** | +9.0 | 2e-17 | 38/48 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.98×** | +8.4 | 6e-15 | 35/47 (HOP62, LOX-IMVI, …) | all doses, stronger at high dose | position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **1.90×** | +8.2 | 2e-14 | 40/48 (SW480, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.76×** | +6.9 | 3e-10 | 36/47 (HT-29, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Posaconazole (drug)]] 5 µM |  | **1.67×** | +6.3 | 2e-08 | 36/48 (HEC-1-A, NCI-H1573, …) | top dose only | plate-row cell shift |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.61×** | +6.1 | 7e-08 | 28/47 (SW480, LOX-IMVI, …) | rises with dose | low cells (technical?) |
| [[Almonertinib (mesylate) (drug)]] 5 µM |  | **1.50×** | +5.0 | 3e-05 | 24/49 (C-33 A, C32, …) | top dose only | plate-row cell shift; position effect removed |
| [[Trametinib (drug)]] 5 µM |  | **1.46×** | +5.0 | 3e-05 | 28/49 (MIA PaCa-2, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **2.05×** | +4.8 | 7e-05 | 26/48 (SW480, A498, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Entrectinib (drug)]] 5 µM |  | **1.43×** | +4.5 | 2e-04 | 25/48 (A498, LS 180, …) | top dose only |  |
| [[(S)-Crizotinib (drug)]] 5 µM |  | **1.44×** | +4.5 | 3e-04 | 22/48 (HEC-1-A, HS-578T, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8332.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **0.682×** | -4.9 | 5e-04 | 22/48 (LS 180, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~21% here) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.774×** | -4.7 | 8e-04 | 31/48 (SNU-1, NCI-H1792, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.700×** | -4.6 | 8e-04 | 23/48 (PANC-1, NCI-H1573, …) | inconsistent across doses |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.702×** | -4.5 | 8e-04 | 27/48 (LoVo, MIA PaCa-2, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.714×** | -4.0 | 0.008 | 22/47 (A549, SW480, …) | inconsistent across doses | low cells (technical?) |
| [[Auranofin (drug)]] 5 µM |  | **0.753×** | -3.6 | 0.025 | 21/48 (A-172, LOX-IMVI, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.20 per unit of S-phase module lfc, -0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8332. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 26.7 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 4.47× (z +12.7) | — |
| [[HEC-1-A (line)]] | alt | 29.5 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.62× (z +10.6) | — |
| [[HOP62 (line)]] | alt | 29.8 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.62× (z +13.7) | — |
| [[LoVo (line)]] | wt | 20.5 | 3 | 0 | [[Berbamine (drug)]] 5 µM 3.23× (z +12.0) | — |
| [[NCI-H460 (line)]] | wt | 26.9 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.07× (z +13.2) | — |
| [[A-172 (line)]] | wt | 80.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.22× (z +15.3) | — |
| [[A498 (line)]] | wt | 24.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.40× (z +12.2) | — |
| [[A549 (line)]] | wt | 21.6 | 2 | 0 | [[Cepharanthine (drug)]] 5 µM 3.00× (z +9.9) | — |
| [[C-33 A (line)]] | alt | 28.9 | 2 | 0 | [[Cepharanthine (drug)]] 5 µM 4.28× (z +10.4) | — |
| [[HT-29 (line)]] | alt | 30.7 | 2 | 0 | [[Cepharanthine (drug)]] 5 µM 2.81× (z +10.3) | — |
| [[LS 180 (line)]] | wt | 30.6 | 2 | 0 | [[Cepharanthine (drug)]] 5 µM 3.56× (z +11.0) | — |
| [[NCI-H2030 (line)]] | alt | 24.4 | 2 | 0 | [[Cepharanthine (drug)]] 5 µM 3.03× (z +10.2) | — |
| [[SNU-423 (line)]] | alt | 116 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.143× (z -14.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW1417 (line)]] | alt | 24.3 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 4.23× (z +9.1) | — |
| [[C32 (line)]] | wt | 28.1 | 1 | 0 | [[Cepharanthine (drug)]] 5 µM 3.11× (z +9.1) | — |
| [[H4 (line)]] | wt | 39.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.108× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HS-578T (line)]] | alt | 54.3 | 1 | 0 | [[Cepharanthine (drug)]] 5 µM 2.63× (z +10.4) | — |
| [[J82 (line)]] | alt | 38.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.05× (z +15.1) | — |
| [[LOX-IMVI (line)]] | wt | 43.0 | 1 | 0 | [[Cobimetinib (drug)]] 5 µM 3.33× (z +8.7) | — |
| [[MIA PaCa-2 (line)]] | alt | 80.6 | 1 (1 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 1.87× (z +14.5) ⚠ position not correctable | — |
| [[NCI-H2347 (line)]] | alt | 32.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.60× (z +12.0) | — |
| [[RKO (line)]] | wt | 29.6 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 4.83× (z +9.0) | — |
| [[SW 900 (line)]] | alt | 27.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.29× (z +10.1) | — |
| [[A-427 (line)]] | wt | 25.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 54.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 53.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 31.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 31.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 29.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 40.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 19.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 40.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 52.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 8.94 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 28.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 26.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 42.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 35.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 37.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 33.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 56.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 30.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 62.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 33.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 32.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8332), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SREBF2]] | +0.65 | +0.56 / +0.63 | both halves | 1e-05 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS; STRING 914 |
| [[MVD]] | +0.65 | +0.64 / +0.60 | both halves | 7e-06 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS; STRING 918 |
| [[INSIG1]] | +0.64 | +0.69 / +0.51 | both halves | 1e-05 | pathway: Metabolism of steroids; STRING 648 |
| [[ACAT2]] | +0.63 | +0.66 / +0.59 | both halves | 7e-06 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS; STRING 758 |
| [[MVK]] | +0.62 | +0.62 / +0.58 | both halves | 7e-06 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS; STRING 817 |
| [[SCD]] | +0.61 | +0.61 / +0.57 | both halves | 1e-05 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS; STRING 512 |
| [[DHCR7]] | +0.61 | +0.57 / +0.60 | both halves | 9e-06 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS; STRING 925 |
| [[ERG28]] | +0.61 | +0.60 / +0.56 | both halves | 1e-05 | STRING 977 |
| [[CLCN6]] | +0.60 | +0.56 / +0.58 | both halves | 1e-05 | **novel candidate** |
| [[ACSS2]] | +0.60 | +0.58 / +0.57 | both halves | 9e-06 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS; STRING 434 |
| [[PCYT2]] | +0.59 | +0.60 / +0.49 | both halves | 1e-05 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS |
| [[SREBF1]] | +0.58 | +0.54 / +0.52 | both halves | 1e-05 | pathway: Activation of gene expression by SREBF (SREBP); STRING 857 |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ALG8]] | -0.46 | -0.47 / -0.39 | both halves | 5e-05 |  |
| [[SRBD1]] | -0.45 | -0.42 / -0.36 | both halves | 1e-04 |  |
| [[LINC00467]] | -0.45 | -0.40 / -0.39 | both halves | 5e-05 |  |
| [[GBX2-AS1]] | -0.44 | -0.39 / -0.42 | both halves | 5e-05 |  |
| [[TASOR2]] | -0.43 | -0.36 / -0.40 | both halves | 1e-04 |  |
| [[ASAH2B]] | -0.43 | -0.33 / -0.39 | both halves | 1e-04 |  |
| [[SPOPL-DT]] | -0.42 | -0.32 / -0.37 | both halves | 2e-04 |  |
| [[XRCC4]] | -0.42 | -0.41 / -0.39 | both halves | 5e-05 |  |
| [[SPRY4-AS1]] | -0.41 | -0.39 / -0.43 | both halves | 6e-05 |  |
| [[PA2G4]] | -0.41 | -0.42 / -0.31 | both halves | 2e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 086]] — cholesterol synthesis; 51 genes; every member is in the + arm (projection on the module's main direction 0.662). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (22.3, -48.4); signed map (-53.4, 31.6). **Vector** length 129, 39.3% of its response variance represented; |z| ≥ 3 in 1,293 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *SREBP1 lipogenesis* (control, mean cos +0.51 to 6); *androgen response* (hallmark, mean cos +0.51 to 9); *PPARA activates gene expression* (reactome, mean cos +0.52 to 6).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Cepharanthine (drug)]] 5 µM |  | +7.9 | +11.6 |
|  | [[Berbamine (drug)]] 5 µM |  | +6.2 | +9.1 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM |  | +6.0 | +6.9 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +5.8 | +6.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +5.6 | +8.4 |
|  | [[Entrectinib (drug)]] 5 µM |  | +5.0 | +4.5 |
| fall | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.8 | -0.7 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -4.7 | -4.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.6 | -1.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.2 | -4.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -4.1 | -4.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.7 | -3.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.7 | -4.0 |

## What is on record

|  |  |
|---|---|
| Name | lanosterol synthase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 21q22.3 — chr21:46,188,141-46,228,824 (-) |
| Ensembl biotype | protein_coding |
| Also known as | OSC |
| Hallmark sets | CHOLESTEROL_HOMEOSTASIS |
| Reactome | 6 pathways, smallest: Lanosterol biosynthesis; Cholesterol biosynthesis; Activation of gene expression by SREBF (SREBP) |
| Matched by | ensembl_id |

**Function**, from UniProt [P48449](https://www.uniprot.org/uniprotkb/P48449) (Lanosterol synthase):

> Key enzyme in the cholesterol biosynthesis pathway. Catalyzes the cyclization of (S)-2,3 oxidosqualene to lanosterol, a reaction that forms the sterol nucleus. Through the production of lanosterol may regulate lens protein aggregation and increase transparency.

**Summary**, from NCBI Gene [4047](https://www.ncbi.nlm.nih.gov/gene/4047):

> The protein encoded by this gene catalyzes the conversion of (S)-2,3 oxidosqualene to lanosterol. The encoded protein is a member of the terpene cyclase/mutase family and catalyzes the first step in the biosynthesis of cholesterol, steroid hormones, and vitamin D. Alternative splicing results in multiple transcript variants encoding different isoforms.[provided by RefSeq, Feb 2009]

**Accessions** — [HGNC:6708](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6708) · Entrez [4047](https://www.ncbi.nlm.nih.gov/gene/4047) · UniProt [P48449](https://www.uniprot.org/uniprotkb/P48449) · Ensembl [ENSG00000160285](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000160285)

## Data

Gene col 8332: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8332); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8332, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8332]; `tensor/DDL_lfc|DDL_z.npy` [8332]; `embed/gene_vectors.npy` [8332]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8332 or target_col == 8332). Every well: [[LSS — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LSS.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
