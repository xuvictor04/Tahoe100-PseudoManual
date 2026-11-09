---
symbol: "DDX56"
type: "gene"
col: 5848
ensembl_id: "ENSG00000136271"
name: "DEAD-box helicase 56"
location: "7p13"
module: 5
arm: "+"
pooled_cpm: 20.67
n_lines_expressing: 50
n_dd_up: 37
n_dd_down: 4
n_dd_up_clean: 19
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# DDX56

*DEAD-box helicase 56* — 7p13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 37 drug-doses (18 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.75× (z +14.0, q 2e-41, up in 43 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.794× (z -5.8, q 3e-06, down in 28 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MAPKAPK5]] (+0.67, fdr 9e-06), [[DHX37]] (+0.66, fdr 7e-06), [[WDR74]] (+0.66, fdr 1e-05); moves opposite to [[SVIP]] (-0.61, fdr 2e-05), [[GABARAPL2]] (-0.60, fdr 1e-05), [[GPX4]] (-0.57, fdr 2e-05).
> It sits in the **+** arm of [[Module 005]] (MYC targets v2).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 46 in all, 23 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 37 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 18 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5848.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.75×** | +14.0 | 2e-41 | 43/47 (A549, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.67×** | +8.7 | 7e-16 | 30/43 (J82, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.42×** | +8.2 | 5e-14 | 30/47 (PANC-1, LoVo, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **2.32×** | +7.8 | 7e-13 | 32/48 (LoVo, HEC-1-A, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.55×** | +7.8 | 7e-13 | 30/48 (A498, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.50×** | +7.2 | 6e-11 | 28/47 (PANC-1, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.50×** | +7.2 | 6e-11 | 33/48 (NCI-H460, AsPC-1, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.47×** | +6.8 | 8e-10 | 26/48 (SK-MEL-2, A498, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.48×** | +6.7 | 2e-09 | 26/48 (NCI-H2030, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | **1.43×** | +6.1 | 7e-08 | 18/35 (Hs 766T, LoVo, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | **1.40×** | +5.9 | 2e-07 | 23/42 (A498, LoVo, …) | all doses, flat | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **1.37×** | +5.6 | 1e-06 | 21/47 (SW480, PANC-1, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.39×** | +5.5 | 1e-06 | 23/48 (PANC-1, A498, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **1.39×** | +5.4 | 2e-06 | 19/39 (Panc 03.27, HEC-1-A, …) | all doses, flat | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~27% of this change | **1.37×** | +5.3 | 4e-06 | 22/46 (NCI-H23, A549, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.41×** | +5.3 | 5e-06 | 22/47 (HT-29, A549, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.31×** | +4.8 | 6e-05 | 24/48 (SW480, C-33 A, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.18× | +4.2 | 9e-04 | 17/48 (SNU-423, BT-474, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.26×** | +4.0 | 0.002 | 13/48 (NCI-H1792, NCI-H460, …) | top dose only |  |
| [[Belzutifan (drug)]] 5 µM |  | **1.54×** | +4.0 | 0.002 | 7/44 (LS 180, A498, …) | top dose only | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.26×** | +3.8 | 0.003 | 15/47 (HEC-1-A, BT-474, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.50×** | +3.7 | 0.004 | 6/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5848.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.794×** | -5.8 | 3e-06 | 28/48 (NCI-H460, PANC-1, …) | rises with dose |  |
| [[Gallic acid (hydrate) (drug)]] 0.5 µM |  | **0.782×** | -3.8 | 0.040 | 14/47 (hTERT-HPNE, SW 1088, …) | inconsistent across doses |  |
| [[Elagolix sodium (drug)]] 0.5 µM |  | **0.791×** | -3.6 | 0.052 | 13/47 (H4, A498, …) | inconsistent across doses | position effect removed |
| [[Gemcitabine (drug)]] 0.5 µM |  | **0.825×** | -3.5 | 0.070 | 11/48 (RPMI-7951, A498, …) | two highest doses | noisy plate (z scaled) |
| [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM |  | 0.821× | -3.3 | 0.12 | 14/46 (BT-474, HT-29, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.28 per unit of S-phase module lfc, -0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5848. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 20.0 | 0 | 1 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.361× (z -9.4) |
| [[A549 (line)]] | wt | 14.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.78× (z +9.3) | — |
| [[hTERT-HPNE (line)]] | wt | 14.5 | 0 | 1 | — | [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 5 µM 0.144× (z -9.0) |
| [[A-172 (line)]] | wt | 31.4 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 35.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 32.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 24.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 12.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 9.10 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 21.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 36.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 33.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 32.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 13.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 26.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 12.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 20.0 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 8.84 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 17.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 21.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 32.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 16.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 29.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 33.5 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 26.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5848), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAPKAPK5]] | +0.67 | +0.57 / +0.61 | both halves | 9e-06 |  |
| [[DHX37]] | +0.66 | +0.59 / +0.62 | both halves | 7e-06 | STRING 572 |
| [[WDR74]] | +0.66 | +0.57 / +0.58 | both halves | 1e-05 | STRING 975 |
| [[TBL3]] | +0.65 | +0.63 / +0.71 | both halves | 7e-06 | STRING 938 |
| [[TRMT1]] | +0.65 | +0.57 / +0.62 | both halves | 9e-06 | STRING 477 |
| [[MRTO4]] | +0.63 | +0.62 / +0.59 | both halves | 7e-06 | STRING 909 |
| [[TSR1]] | +0.63 | +0.56 / +0.58 | both halves | 1e-05 | STRING 887 |
| [[TLCD3A]] | +0.62 | +0.51 / +0.56 | both halves | 1e-05 |  |
| [[DPH2]] | +0.61 | +0.56 / +0.61 | both halves | 1e-05 | STRING 624 |
| [[GTF3C4]] | +0.61 | +0.49 / +0.57 | both halves | 1e-05 |  |
| [[PIGW]] | +0.61 | +0.46 / +0.53 | both halves | 3e-05 |  |
| [[MCM3AP]] | +0.60 | +0.58 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SVIP]] | -0.61 | -0.57 / -0.48 | both halves | 2e-05 |  |
| [[GABARAPL2]] | -0.60 | -0.57 / -0.55 | both halves | 1e-05 |  |
| [[GPX4]] | -0.57 | -0.50 / -0.48 | both halves | 2e-05 |  |
| [[MOSPD2]] | -0.57 | -0.50 / -0.41 | both halves | 4e-05 |  |
| [[TCAF1]] | -0.56 | -0.43 / -0.43 | both halves | 3e-05 |  |
| [[OAZ1]] | -0.55 | -0.37 / -0.45 | both halves | 9e-05 |  |
| [[UBE2B]] | -0.53 | -0.44 / -0.45 | both halves | 3e-05 |  |
| [[CAMK2N1]] | -0.52 | -0.43 / -0.37 | both halves | 8e-05 |  |
| [[CDKN2D]] | -0.51 | -0.45 / -0.37 | both halves | 8e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **+** arm (projection on the module's main direction 0.615). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-16.4, -32.4); signed map (0.3, -46.4). **Vector** length 77.4, 14.5% of its response variance represented; |z| ≥ 3 in 880 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *tRNA modification in the nucleus and cytosol* (reactome, mean cos +0.52 to 7).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.1 | +14.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.1 | +8.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.1 | +4.2 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.6 | +7.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +3.6 | +7.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.7 | +3.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.6 | +3.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.6 | +6.8 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -3.7 | -5.8 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.9 | -2.0 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -2.7 | +1.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.7 | -2.9 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.4 | -2.8 |
|  | [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM |  | -1.6 | -3.3 |
|  | [[Gemcitabine (drug)]] 0.5 µM |  | -1.5 | -3.5 |
|  | [[Glycyrrhizic acid (drug)]] 0.5 µM |  | -1.5 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | DEAD-box helicase 56 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p13 — chr7:44,565,804-44,575,051 (-) |
| Ensembl biotype | protein_coding |
| Also known as | NOH61 |
| Gene groups (HGNC) | DEAD-box helicases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NY93](https://www.uniprot.org/uniprotkb/Q9NY93) (Probable ATP-dependent RNA helicase DDX56):

> Nucleolar RNA helicase that plays a role in various biological processes including innate immunity, ribosome biogenesis or nucleolus organization. Plays an essential role in maintaining nucleolar integrity in planarian stem cells. Maintains embryonic stem cells proliferation by conventional regulation of ribosome assembly and interaction with OCT4 and POU5F1 complex (By similarity). Regulates antiviral innate immunity by inhibiting the virus-triggered signaling nuclear translocation of IRF3. …

**Summary**, from NCBI Gene [54606](https://www.ncbi.nlm.nih.gov/gene/54606):

> This gene encodes a member of the DEAD box protein family. DEAD box proteins, characterized by the conserved motif Asp-Glu-Ala-Asp (DEAD), are putative RNA helicases. They are implicated in a number of cellular processes involving alteration of RNA secondary structure such as translation initiation, nuclear and mitochondrial splicing, and ribosome and spliceosome assembly. Based on their distribution patterns, some members of this family are believed to be involved in embryogenesis, …

**Accessions** — [HGNC:18193](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18193) · Entrez [54606](https://www.ncbi.nlm.nih.gov/gene/54606) · UniProt [Q9NY93](https://www.uniprot.org/uniprotkb/Q9NY93) · Ensembl [ENSG00000136271](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000136271)

## Data

Gene col 5848: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5848); `tables/drug_effects.parquet` (51 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5848, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5848]; `tensor/DDL_lfc|DDL_z.npy` [5848]; `embed/gene_vectors.npy` [5848]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5848 or target_col == 5848). Every well: [[DDX56 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DDX56.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
